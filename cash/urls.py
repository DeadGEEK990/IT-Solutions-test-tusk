from django.urls import path
from .admin import SubcategoryAutocomplete, CategoryAutocomplete

urlpatterns = [
    # Путь для получения подкатегорий связанных с категорией
    path(
        "subcategory-autocomplete/",
        SubcategoryAutocomplete.as_view(),
        name="subcategory-autocomplete",
    ),
    # Путь для получения подкатегорий связанных с категорией
    path(
        "category-autocomplete/",
        CategoryAutocomplete.as_view(),
        name="category-autocomplete",
    ),
]
