from django.db import models


class City(models.Model):

    id_number = models.PositiveSmallIntegerField(
        'ID города',
        blank=False,
        null=False
    )
    name = models.CharField(
        'Название города',
        max_length=255
    )

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.name


class Product(models.Model):

    name = models.TextField(
        'Наименование товара'
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        default_related_name = 'products'

    def __str__(self):
        return self.name


class Image(models.Model):

    image_link = models.ImageField(
        upload_to='products/images/',
        verbose_name='Изображение',
        blank=False,
        null=False
    )
    product = models.ForeignKey(
        Product,
        related_name='product_images',
        on_delete=models.CASCADE,
        verbose_name='Товар',
        null=False,
        blank=False
    )
    city = models.ForeignKey(
        City,
        related_name='city_images',
        on_delete=models.SET_NULL,
        verbose_name='Город',
        null=True,
        blank=False
    )

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
