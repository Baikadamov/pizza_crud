from ninja import Router
from apps.rest.services import *
from django.shortcuts import get_object_or_404

router = Router()


@router.post("/restaurants/")
def create_restaurant(request, payload: RestaurantSchemaIn):
    restaurant = Restaurant.objects.create(**payload.dict())
    return {"id": restaurant.id}


@router.get("/restaurants/", response=List[RestaurantSchemaOut])
def get_restaurant(request):
    restaurant = Restaurant.objects.all()
    return restaurant


@router.get("/pizza/", response=List[PizzaSchemaOut])
def list_pizza(request):
    pizzas = Pizza.objects.all()
    return pizzas


@router.get("/pizza/{pizza_id}", response=PizzaSchemaOut)
def get_pizza(request, pizza_id: int):
    pizza = get_object_or_404(Pizza, id=pizza_id)
    return pizza


@router.post("/pizza/", response=PizzaSchemaOut)
def create_pizza(request, payload: PizzaSchemaIn):
    return create_pizza_service(payload)


@router.put("/pizza/{pizza_id}", response=PizzaSchemaOut)
def update_pizza(request, pizza_id: int, payload: PizzaSchemaIn):
    return update_pizza_service(pizza_id, payload)


@router.delete("/pizza/{pizza_id}")
def delete_pizza(request, pizza_id: int):
    pizza = get_object_or_404(Pizza, id=pizza_id)
    pizza.delete()
    return {"Success": True}


@router.get("/chefs/", response=List[ChefsSchemaOut])
def get_chefs(request):
    chefs = Chef.objects.select_related('restaurant').all()
    return chefs


@router.post('/chefs/', response=ChefsSchemaOut)
def create_chef(request, payload: ChefsSchemaIn):
    return create_chef_service(payload)


@router.get("/ingredients/", response=List[IngredientSchemaOut])
def get_ingredients(request):
    ingredients = Ingredient.objects.all()
    return ingredients


@router.post("/ingredients/")
def create_ingredient(request, payload: IngredientSchemaIn):
    ingredient = Ingredient.objects.create(**payload.dict())
    return {"id": ingredient.id}


@router.get("/reviews/", response=List[ReviewSchemaOut])
def get_review(request):
    reviews = Review.objects.select_related('restaurant').all()
    return reviews


@router.post("/reviews/")
def create_review(request, payload: ReviewSchemaIn):
    review = create_review_service(payload)
    return review


@router.get("/restaurants/{id}/menu/", response=RestaurantMenuSchema)
def get_restaurants_menu(request, id: int):
    return get_menu_service(id)
