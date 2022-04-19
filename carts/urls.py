from django.urls import path

from carts.views import CartView

urlpatterns = [
    path('/like', CartView.as_view()),
    path('/like/<int:lectures_id>', CartView.as_view()),
]
