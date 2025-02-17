from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create_order", views.create_order, name="create_order"),
    path("cakes/", views.cakes, name="cakes"),
    path("cakes/<int:pk>", views.cake_details, name="cake_details"),
    path("cookies/", views.CookiesListView.as_view(), name="cookies"),
    path("cookies/<int:pk>", views.CookiesDetailView.as_view(), name="cookies_details"),
    path("orders/", views.OrdersListView.as_view(), name="orders"),
    path("orders/<int:pk>", views.OrderDetailView.as_view(), name="order_details"),
]
