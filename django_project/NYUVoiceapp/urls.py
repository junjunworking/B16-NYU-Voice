from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="NYUVoiceapp-home"),
    path("CourseReview/", views.CourseReview, name="NYUVoiceapp-CourseReview"),
    path('login_failed/', views.login_failed, name='login_failed'),

]
