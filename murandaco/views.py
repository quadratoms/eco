from paystack.resource import TransactionResource
from django.shortcuts import render
import random
import string

# import stripe
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Carousel, Order, OrderItem, Product, Category, Comment


def home(request):

    cat = Category.objects.all()
    top = Product.objects.all()[:2]
    carousel = [each for each in Carousel.objects.all()]
    for each in carousel:
        each.index = carousel.index(each)
        print(each.index)

    context = {
        'cat': cat,
        'top': top,
        'carousel': carousel
    }
    return render(request, 'home.html', context)


def category(request, pk):

    cat = Category.objects.all()
    products = Product.objects.filter(category=Category.objects.get(id=pk))
    context = {
        'cat': cat,
        'products': products,
    }
    return render(request, 'category.html', context)


def product(request, pk):

    cat = Category.objects.all()
    product = Product.objects.get(id=pk)
    context = {
        'cat': cat,
        'product': product,
    }
    return render(request, 'product.html', context)


def cart(request):
    context = {}
    cat = Category.objects.all()

    # order=Order.objects.get(user=request.user, ordered=False)
    od = Order.objects.filter(user=request.user, ordered=False)
    old_order = Order.objects.filter(user=request.user, ordered=True)
    if od.count() > 0:
        print('korder', od)
        order = od[0]

        context = {
            'cat': cat,
            'order': order,
            'old_order': old_order
        }

    return render(request, 'cart.html', context)


@login_required
def add_to_cart(request, id):
    item = get_object_or_404(Product, id=id)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(id=item.id).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated.")
            return redirect("/cart")
        else:
            order.items.add(order_item)
            messages.info(request, "This item was added to your cart.")
            return redirect("/cart")
    else:
        ordered_date = timezone.now()
        rand = ''.join(
            [random.choice(
                string.ascii_letters + string.digits) for n in range(16)])
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date, ref_code=rand)
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart.")
        return redirect("/cart")


@login_required
def remove_from_cart(request, id):
    item = get_object_or_404(Product, id=id)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(id=item.id).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            order_item.delete()
            messages.info(request, "This item was removed from your cart.")
            return redirect("/cart")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("/product/"+str(id))
    else:
        messages.info(request, "You do not have an active order")
        return redirect("/product/"+str(id))


@login_required
def remove_single_item_from_cart(request, id):
    item = get_object_or_404(Product, id=id)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(id=item.id).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)
            messages.info(request, "This item quantity was updated.")
            return redirect("/cart")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("/product/"+str(id))
    else:
        messages.info(request, "You do not have an active order")
        return redirect("/product/"+str(id))


def verify_payment(request, pk):

    secret_key = 'sk_test_ac7e6b6b04b712d76676cd40230e4db141f8b9e6'

    client = TransactionResource(secret_key, pk)

    verify = client.verify()  # Verify client credentials
    print(verify)
    status = verify['data']['status']

    if status == 'success':
        order = Order.objects.get(ref_code=pk)
        order.ordered = True
        order.ordered_date = timezone.now()
        order.save()

    return redirect('/cart')


# Create your views here.
