# Generated by Django 3.2.6 on 2021-08-29 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('murandaco', '0002_auto_20210829_0819'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(height_field=200, max_length=300, null=True, upload_to='catimg', width_field=300),
        ),
    ]
