from typing import Dict

from apps.rest.schemas import *
from django.shortcuts import get_object_or_404


def create_pizza_service(payload: PizzaSchemaIn) -> PizzaSchemaOut:
    pizza = Pizza.objects.create(
        name=payload.name,
        cheese=payload.cheese,
        thickness=payload.thickness,
        secret_ingredient=payload.secret_ingredient,
        restaurant_id=payload.restaurant,
    )
    return PizzaSchemaOut.from_orm(pizza)


def create_chef_service(payload: ChefsSchemaIn) -> ChefsSchemaOut:
    chef = Chef.objects.create(
        name=payload.name,
        restaurant_id=payload.restaurant,
    )
    return ChefsSchemaOut.from_orm(chef)


def create_review_service(payload: ReviewSchemaIn) -> ReviewSchemaOut:
    review = Review.objects.create(
        restaurant_id=payload.restaurant,
        rating=payload.rating,
        comment=payload.comment
    )

    return ReviewSchemaOut.from_orm(review)


def update_pizza_service(pizza_id: int, payload: PizzaSchemaIn) -> PizzaSchemaOut:
    pizza = get_object_or_404(Pizza, id=pizza_id)
    data = payload.model_dump()

    ingredients = data.pop("ingredients", None)
    restaurant_id = data.pop("restaurant", None)

    for attr, value in data.items():
        setattr(pizza, attr, value)

    if restaurant_id is not None:
        pizza.restaurant = get_object_or_404(Restaurant, id=restaurant_id)

    pizza.save()

    if ingredients is not None:
        pizza.ingredients.set(ingredients)

    return PizzaSchemaOut.from_orm(pizza)


def get_menu_service(id: int):
    restaurant = get_object_or_404(Restaurant, id=id)
    result = {
        "restaurant_id": restaurant.id,
        "restaurant_name": restaurant.name,
        "pizzas": [
            {
                "id": pizza.id,
                "name": pizza.name,
                "cheese": pizza.cheese,
                "thickness": pizza.thickness,
                "ingredients": [
                    {"id": ing.id, "name": ing.name}
                    for ing in pizza.ingredients.all()
                ],
                "secret_ingredient": pizza.secret_ingredient,
            }
            for pizza in restaurant.pizzas.all()
        ]
    }

    return result

