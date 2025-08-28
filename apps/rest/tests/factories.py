import factory
from apps.rest.models import *


class RestaurantFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Restaurant

    name = factory.Faker("name")
    address = factory.Faker("address")



class IngredientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ingredient

    name = factory.Faker("word")


class PizzaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Pizza

    name = factory.Faker("word")
    cheese = factory.Faker("word")
    thickness = factory.Iterator(["thin", "classic"])
    secret_ingredient = factory.Faker("word")
    ingredients = factory.Faker("ingredients")
    restaurant = factory.SubFactory(RestaurantFactory)

    @factory.post_generation
    def ingredients(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for ingredient in extracted:
                self.ingredients.add(ingredient)
        else:
            for _ in range(3):
                self.ingredients.add(IngredientFactory())
