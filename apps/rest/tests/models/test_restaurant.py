import pytest
from apps.rest.tests.factories import RestaurantFactory



# Тут мы пишем вручную данные и проверяем их на выходе что они такие же.
# но можно использовать фейкер чтобы он генерил данные и проверял есть ли строка айди и тд
@pytest.mark.django_db
def test_restaurant_creation():
    restaurant = RestaurantFactory(name="Burger King", address="Some address idk")
    assert restaurant.name == "Burger King"
    assert restaurant.address == "Some address idk"



#Второй вариант
@pytest.mark.django_db
def test_restaurant_creation_random():
    restaurant = RestaurantFactory()
    assert isinstance(restaurant.name, str)
    assert isinstance(restaurant.address, str)


