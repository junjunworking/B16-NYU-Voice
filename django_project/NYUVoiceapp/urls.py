from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="NYUVoiceapp-home"),
    path("CourseReview/", views.CourseReview, name="NYUVoiceapp-CourseReview"),
    path("staffhome/",views.staffhome, name="NYUVoiceapp-staffhome"),
    path("staffcoursereview/", views.staffcoursereview, name= "NYUVoiceapp-staffcoursereview"),
]
