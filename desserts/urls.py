from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create_order/", views.create_order, name="create_order"),
    path("cake_options/", views.CakesOptionListView.as_view(), name="cake_options"),
    path("cakes/<int:pk>", views.CakeListView.as_view(), name="cakes"),
    path("cake/<int:pk>", views.CakeDetailView.as_view(), name="cake_details"),
    path("cookies/", views.CookiesListView.as_view(), name="cookies"),
    path("cookies/<int:pk>", views.CookiesDetailView.as_view(), name="cookies_details"),
    path("orders/", views.OrdersListView.as_view(), name="orders"),
    path("orders/<int:pk>", views.OrderDetailView.as_view(), name="order_details"),
    path("cake_pops/", views.CakePopsListView.as_view(), name="cake_pops"),
    path("cake_pops/<int:pk>", views.CakePopsDetailView.as_view(), name="cake_pops_details"),
    path("contacts/", views.contacts, name="contacts")
]


