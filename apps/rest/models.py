from django.db import models


# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Restaurant(BaseModel):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Ресторан'
        verbose_name_plural = 'Рестораны'

    def __str__(self):
        return self.name


class Chef(BaseModel):
    name = models.CharField(max_length=100)
    restaurant = models.OneToOneField(Restaurant, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Шеф'
        verbose_name_plural = 'Шефы'

    def __str__(self):
        return self.name


class Ingredient(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'


class Pizza(BaseModel):
    name = models.CharField(max_length=100)
    cheese = models.CharField(max_length=100)

    THICKNESS_CHOICES = [
        ('thin', 'Тонкое'),
        ('classic', 'Классическое')
    ]

    thickness = models.CharField(max_length=100, choices=THICKNESS_CHOICES)
    secret_ingredient = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(Ingredient)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="pizzas")

    class Meta:
        verbose_name = 'Пицца'
        verbose_name_plural = 'Пиццы'

    def __str__(self):
        return self.name


class Review(BaseModel):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    RATE_CHOICES = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
    rating = models.IntegerField(choices=RATE_CHOICES)
    comment = models.TextField()

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.comment
