from django.contrib import admin

from .models import City, Image, Product


@admin.register(City)
class CityAdmin(admin.ModelAdmin):

    list_display = (
        'id_number',
        'name'
    )
    list_display_links = ('name',)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):

    list_display = (
        'image_link',
        'product',
        'city'
    )
    list_filter = (
        'product',
    )
    list_display_links = ('image_link',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'name',
    )
    list_display_links = ('name',)
