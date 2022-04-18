from django.urls import path

from lectures.views import LectureListView, LectureDetailView

urlpatterns = [
    path('/search', LectureListView.as_view()),
    path('/<int:lecture_id>', LectureDetailView.as_view()),
]