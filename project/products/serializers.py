from rest_framework import serializers

from .models import Image, Product


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('image_link',)


class ProductSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'name', 'images')

    def get_images(self, obj):
        request = self.context.get('request')
        city_id = request.headers.get('city')
        if city_id:
            try:
                # валидация на целое число
                city_id = int(city_id)
            except ValueError:
                city_id = None

        # Если есть фотографии для конкретного города, показываем только их
        images = obj.product_images.filter(city__id_number=city_id)

        # Если фотографий для конкретного города нет или параметр не передан,
        # показываем только фотографии без привязки к городу
        if not images.exists():
            images = obj.product_images.filter(city_id__isnull=True)

        return ImageSerializer(images, many=True).data
