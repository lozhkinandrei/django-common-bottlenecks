from django.urls import path
from . import views

urlpatterns = [
    path("authors", views.AuthorsListView.as_view(), name="authors-list"),
    path(
        "authors-optimized",
        views.AuthorsOptimizedListView.as_view(),
        name="authors-list-optimized",
    ),
    path("books", views.BooksListView.as_view(), name="books-list"),
    path(
        "books-optimized",
        views.BooksOptimizedListView.as_view(),
        name="books-list-optimized",
    ),
    path("pandas", views.PandasView.as_view(), name="pandas"),
    path(
        "pandas-optimized", views.PandasOptimizedView.as_view(), name="pandas-optimized"
    ),
]
