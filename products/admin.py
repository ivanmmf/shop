from  django.contrib import admin
from .models import*

class ProductImageInline(admin.TabularInline):
    model = ProductImages
    extra = 0


class ProductAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    inlines = [ProductImageInline]
    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)

class ProductImagesAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ProductImages._meta.fields]

    class Meta:
        model = ProductImages

admin.site.register(ProductImages, ProductImagesAdmin )