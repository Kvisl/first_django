from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def home(request):
    return HttpResponse('Hello')


def recipe(request, dish):
    servings = request.GET.get('servings')
    if servings:
        try:
            servings = int(servings)
        except ValueError:
            return HttpResponse('Ошибка, введите целое число.')
    else:
        servings = 1

    recipe_data = DATA.get(dish)
    if not recipe_data:
        context = {
            'not_found': True
        }
    else:
        recipes = {k: v * servings for k, v in recipe_data.items()}
        context = {
            'recipe': recipes
        }

    return render(request, 'calculator/index.html', context)
