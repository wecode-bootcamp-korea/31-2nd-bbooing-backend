from django.urls import path
from lectures.views import LectureView, LectureListView, LectureDetailView 

urlpatterns = [
    path('', LectureView.as_view()),
    path('/search', LectureListView.as_view()),
    path('/<int:lecture_id>', LectureDetailView.as_view()),
]