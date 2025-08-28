import pytest

from apps.rest.schemas import PizzaSchemaIn
from apps.rest.services import update_pizza_service
from apps.rest.tests.factories import *


@pytest.mark.django_db
def test_update_pizza_service_success():
    pizza = PizzaFactory(name="Old Pizza")
    new_restaurant = RestaurantFactory()
    ingredient1 = IngredientFactory()
    ingredient2 = IngredientFactory()

    payload = PizzaSchemaIn(
        name="New Pizza",
        cheese="Mozzarella",
        thickness="classic",
        secret_ingredient="Love ❤️",
        restaurant=new_restaurant.id,
        ingredients=[ingredient1.id, ingredient2.id]
    )

    result = update_pizza_service(pizza.id, payload)

    # проверяем только поля, которые есть в PizzaSchemaOut
    assert result.name == "New Pizza"
    assert result.cheese == "Mozzarella"
    assert result.thickness == "classic"

