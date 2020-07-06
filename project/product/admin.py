from django.contrib import admin

from .models import Product, ProductImage, CategoryProduct


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    inlines = [ProductImageInline]

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'image')

    class Meta:
        model = ProductImage


admin.site.register(ProductImage, ProductImageAdmin)


class CategoryProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CategoryProduct._meta.fields]

    class Meta:
        model = CategoryProduct


admin.site.register(CategoryProduct, CategoryProductAdmin)
