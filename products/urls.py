"""design routes for products app."""
from django.urls import path

from .views import (
    ProductDetailView,
    SubstitutesListView,
    SearchListView,
    FavoritesListView,
    admin_favorite,
    CategoryListView,
    CategoriesListView
)

urlpatterns = [
    path('<slug:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('search/', SearchListView.as_view(), name='search'),
    path('substitutes/<slug:pk>', SubstitutesListView.as_view(),
         name='substitutes'),
    path('substitutes/favorites/', FavoritesListView.as_view(),
         name='favorites'),
    path('favorite/<str:pk>/<str:action>/', admin_favorite,
         name='admin_favorite'),
    path('category/<str:pk>', CategoryListView.as_view(), name="category"),
    path('categories/', CategoriesListView.as_view(), name="categories"),
]
