from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="NYUVoiceapp-home"),
    path("CourseReview/", views.CourseReview, name="NYUVoiceapp-CourseReview"),

]
