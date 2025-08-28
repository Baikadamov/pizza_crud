import pytest

from apps.rest.tests.factories import PizzaFactory


@pytest.mark.django_db
def test_pizza_creation_random():
    pizza = PizzaFactory()

    assert isinstance(pizza.name,str)
    assert isinstance(pizza.cheese,str)
    assert pizza.thickness in ["thin", "classic"]
    assert isinstance(pizza.secret_ingredient,str)
    assert pizza.ingredients.count() == 3

    assert all(isinstance(ing.name, str) for ing in pizza.ingredients.all())

    assert isinstance(pizza.restaurant.id, int)
