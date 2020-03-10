from django.urls import path

from . import views

urlpatterns = [
    # Pessoa Jurídica URLs
    path("", views.ListView.as_view(), name="unidadeorganizacional-list"),
    path("create", views.CreateView.as_view(), name="unidadeorganizacional-create"),
    path("<int:pk>/", views.DetailView.as_view(), name="unidadeorganizacional-detail"),
    path(
        "<int:pk>/edit", views.UpdateView.as_view(), name="unidadeorganizacional-update"
    ),
    path(
        "<int:pk>/del", views.DeleteView.as_view(), name="unidadeorganizacional-delete"
    ),
]
