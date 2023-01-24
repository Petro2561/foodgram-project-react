from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import IngredientViewSet, RecipeViewSet, TagViewSet, UserViewSet

app_name = 'api'

router = DefaultRouter()
router.register('ingredients', IngredientViewSet, 'ingredients')
router.register('tags', TagViewSet, 'tags')
router.register('recipes', RecipeViewSet, 'recipes')
router.register('users', UserViewSet, 'users')


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    # JWT-эндпоинты, для управления JWT-токенами:
    path('auth/', include('djoser.urls.jwt'))
]
