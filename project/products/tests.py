import pytest

from django.urls import reverse
from http import HTTPStatus

MAIN_URL = reverse('products:products_list')
IMAGE_URL = '/media/products/images/'


# Проверка доступности страницы
@pytest.mark.django_db
def test_page_availability(client):
    response = client.get(MAIN_URL)
    assert response.status_code == HTTPStatus.OK


# Проверка доступности полного списка продуктов
@pytest.mark.django_db
def test_objects_in_list(client, products_list):
    response = client.get(MAIN_URL)
    object_list = response.json()
    assert len(object_list) == len(products_list)


# Когда ID города не указан:
# возвращаются только фотографии без привязки к городу
@pytest.mark.django_db
@pytest.mark.usefixtures('products_list')
def test_images_empty_city_id(client):
    response = client.get(MAIN_URL)
    object_list = response.json()
    first_object = object_list[0].get('images')
    second_object = object_list[1].get('images')
    assert len(first_object) == 1
    assert len(second_object) == 1
    assert first_object[0].get('image_link') == IMAGE_URL + 'base_1.png'
    assert second_object[0].get('image_link') == IMAGE_URL + 'base_2.png'


# Когда ID города указан:
# если у товара есть снимки без привязки к конкретному городу, то показываем
# их, только если у товара нет снимков для запрашиваемого города.
@pytest.mark.django_db
@pytest.mark.usefixtures('products_list')
def test_images_with_city_id(client):
    response = client.get(MAIN_URL, headers={'city': 101})
    object_list = response.json()
    first_object = object_list[0].get('images')
    second_object = object_list[1].get('images')
    assert len(first_object) == 1
    assert len(second_object) == 1
    assert first_object[0].get('image_link') == IMAGE_URL + 'base_1.png'
    assert second_object[0].get('image_link') == IMAGE_URL + 'city_101.png'


# Когда ID города указан некорректно:
# обрабатывается случай когда ID города не указан.
@pytest.mark.django_db
@pytest.mark.usefixtures('products_list')
def test_images_with_invalid_city_id(client):
    response = client.get(MAIN_URL, headers={'city': 'slug'})
    object_list = response.json()
    first_object = object_list[0].get('images')
    second_object = object_list[1].get('images')
    assert len(first_object) == 1
    assert len(second_object) == 1
    assert first_object[0].get('image_link') == IMAGE_URL + 'base_1.png'
    assert second_object[0].get('image_link') == IMAGE_URL + 'base_2.png'
