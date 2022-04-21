from django.urls import path

from reviews.views import ReviewView

urlpatterns = [
    path('/<int:review_id>', ReviewView.as_view()),
    path('/lecture/<int:lecture_id>', ReviewView.as_view()),
]
