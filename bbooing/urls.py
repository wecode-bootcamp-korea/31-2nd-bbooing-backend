from django.urls import path, include 

urlpatterns = [
    path('users', include('users.urls')),
    path('main', include('lectures.urls')),
    path('lectures', include('lectures.urls')),
    path('carts', include('carts.urls')),
    path('reviews', include('reviews.urls'))
]
