from django.urls import path

from carts.views import CartView

urlpatterns = [
    path('/like', CartView.as_view())
]