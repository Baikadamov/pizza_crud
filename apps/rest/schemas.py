from ninja import Schema, ModelSchema
from typing import List
from apps.rest.models import *


class RestaurantSchemaIn(Schema):
    name: str
    address: str


class RestaurantSchemaOut(Schema):
    id: int
    name: str
    address: str


class PizzaSchemaIn(Schema):
    name: str
    cheese: str
    thickness: str
    secret_ingredient: str
    ingredients: List[int]
    restaurant: int


class PizzaSchemaOut(ModelSchema):
    class Config:
        model = Pizza
        model_fields = ["id", "name", "cheese", "thickness", "secret_ingredient", ]


class ChefsSchemaIn(Schema):
    name: str
    restaurant: int


class ChefsSchemaOut(Schema):
    id: int
    name: str
    restaurant: RestaurantSchemaOut


class IngredientSchemaIn(Schema):
    name: str


class IngredientSchemaOut(Schema):
    id: int
    name: str


class ReviewSchemaIn(Schema):
    restaurant: int
    rating: int
    comment: str


class ReviewSchemaOut(Schema):
    id: int
    restaurant: RestaurantSchemaOut
    rating: int
    comment: str


class RestaurantMenuSchema(Schema):
    restaurant_id: int
    restaurant_name: str
    pizzas: List[PizzaSchemaOut]


