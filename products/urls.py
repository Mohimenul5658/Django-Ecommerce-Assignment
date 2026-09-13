from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("", views.product_list, name="product_list"),
    path("cart/", views.cart, name="cart"),

    path("add-to-cart/<int:id>/", views.add_to_cart, name="add_to_cart"),

    path("increase/<int:id>/", views.increase_quantity, name="increase_quantity"),
    path("decrease/<int:id>/", views.decrease_quantity, name="decrease_quantity"),
    path("remove/<int:id>/", views.remove_from_cart, name="remove_from_cart"),

    path("<int:id>/", views.product_detail, name="product_detail"),
    path("checkout/", views.checkout, name="checkout"),
]