# Generated by Django 4.2.5 on 2024-03-08 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_unitvariant_weightvariant_alter_product_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='unit_variant',
            field=models.ManyToManyField(blank=True, null=True, to='products.unitvariant'),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight_variant',
            field=models.ManyToManyField(blank=True, null=True, to='products.weightvariant'),
        ),
    ]
