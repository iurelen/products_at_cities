import pytest

from products.models import City, Image, Product

IMAGE_URL = 'products/images/'


@pytest.fixture
def products_list():
    city = City.objects.create(id_number=101, name='Астана')

    products = [
        Product(name='Кружка'),
        Product(name='Футболка')
    ]
    products_list = Product.objects.bulk_create(products)

    images = [
        Image(
            image_link=IMAGE_URL + 'base_1.png',
            product=products_list[0],
            city=None
        ),
        Image(
            image_link=IMAGE_URL + 'base_2.png',
            product=products_list[1],
            city=None
        ),
        Image(
            image_link=IMAGE_URL + 'city_101.png',
            product=products_list[1],
            city=city
        )
    ]
    Image.objects.bulk_create(images)

    return products_list
