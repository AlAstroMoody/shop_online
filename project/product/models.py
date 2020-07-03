from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, default=None)
    description = models.TextField(max_length=500, blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    uid = models.CharField(max_length=30, unique=True)
    brand = models.CharField(max_length=30, blank=True, null=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f' {self.name}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products_images/')
    is_main_image = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f' {self.product.name}'

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
