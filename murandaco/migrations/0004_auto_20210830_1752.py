# Generated by Django 3.2.6 on 2021-08-30 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('murandaco', '0003_category_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='carousel')),
                ('disc', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(null=True, upload_to='catimg'),
        ),
    ]
