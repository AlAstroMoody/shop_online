from django.db import models
from django.db.models.signals import post_save

from product.models import Product
from django.dispatch import receiver


class Status(models.Model):
    name = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказа'

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    customer_name = models.CharField(max_length=50, blank=True, null=True, default=None)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=12, blank=True, null=True, default=None)
    comments = models.TextField(max_length=1000, blank=True, null=True, default=None)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f'Заказ {self.id} {self.status.name}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Номер заказа')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveSmallIntegerField(default=1, verbose_name='Количество')
    is_active = models.BooleanField(default=True)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f' {self.product.name}'

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'

    def save(self, *args, **kwargs):
        price_per_item = self.product.price
        self.price_per_item = price_per_item
        self.total_price = price_per_item * self.count
        super(ProductInOrder, self).save(*args, **kwargs)


def product_in_order_post_save(sender, instance, created, **kwargs):
    order = instance.order
    order_total_price = 0
    all_product_in_order = ProductInOrder.objects.filter(order=order, is_active=True)
    for item in all_product_in_order:
        order_total_price += item.total_price
    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)


post_save.connect(product_in_order_post_save, ProductInOrder)
