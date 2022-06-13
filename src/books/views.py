import numpy as np
import pandas as pd

from django.views import generic
from .models import Author, Book


rng = np.random.default_rng()


class AuthorsListView(generic.ListView):
    template_name = "authors.html"
    context_object_name = "authors"

    def get_queryset(self):
        return Author.objects.all()


class AuthorsOptimizedListView(generic.ListView):
    template_name = "authors.html"
    context_object_name = "authors"

    def get_queryset(self):
        return Author.objects.prefetch_related("books")


class BooksListView(generic.ListView):
    template_name = "books.html"
    context_object_name = "books"

    def get_queryset(self):
        return Book.objects.all()


class BooksOptimizedListView(generic.ListView):
    template_name = "books.html"
    context_object_name = "books"

    def get_queryset(self):
        return Book.objects.select_related("author")


class PandasView(generic.TemplateView):
    template_name = "pandas.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        df = pd.DataFrame(rng.integers(0, 100, size=(10_000_000, 1)), columns=list("A"))
        df["B"] = df["A"].apply(lambda x: x**2)
        context["result"] = df["B"].sum()
        return context


class PandasOptimizedView(generic.TemplateView):
    template_name = "pandas.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        df = pd.DataFrame(rng.integers(0, 100, size=(10_000_000, 1)), columns=list("A"))
        df["B"] = df["A"] ** 2
        context["result"] = df["B"].sum()
        return context
