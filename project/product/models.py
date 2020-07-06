import csv

import httplib2
from django.db import models
from django.shortcuts import reverse


class CategoryProduct(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True, default=None)

    def __str__(self):
        return f' {self.name}'

    class Meta:
        verbose_name = 'Тип товара'
        verbose_name_plural = 'Типы товара'


class Product(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, default=None)
    description = models.TextField(max_length=500, blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    uid = models.CharField(max_length=30, unique=True)
    brand = models.CharField(max_length=30, blank=True, null=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE)
    discount = models.IntegerField(blank=True, null=True, default=None, verbose_name='скидка в процентах')

    def __str__(self):
        return f' {self.name}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def get_absolute_url(self):
        return reverse('product_details_url', kwargs={'id': self.id})

    @staticmethod
    def load_detail():
        h = httplib2.Http('.cache')

        with open('./media/detail.csv', 'r') as file:
            reader = csv.reader(file)
            lst = list(reader)
            for row in lst:
                if row[0] != 'name':
                    CategoryProduct.objects.get_or_create(name=row[6])
                    query_category = CategoryProduct.objects.filter(name=row[6]).values_list('id', flat=True)[0]
                    Product.objects.get_or_create(name=row[0], brand=row[1],
                                                  uid=row[2], price=row[3], description=row[4],
                                                  category_id=query_category, is_active=True)
                    query_product = Product.objects.filter(uid=row[2]).values_list('id', flat=True)[0]

                    response, content = h.request(row[5])
                    filename = row[2] + '.jpeg'
                    out = open('media/' + filename, 'wb')
                    out.write(content)
                    ProductImage.objects.get_or_create(image=filename, is_main_image=True,
                                                       is_active=True, product_id=query_product)
                    out.close()


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='')
    is_main_image = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f' {self.product.name}'

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
