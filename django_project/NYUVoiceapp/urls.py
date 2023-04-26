from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="NYUVoiceapp-home"),
    path("CourseReview/", views.CourseListView.as_view(), name="NYUVoiceapp-CourseReview"),
    path('course/<int:pk>/', views.CourseDetailView.as_view(), name='course-detail'),
    path('course/new/', views.CourseCreateView.as_view(), name='course-create'),
    path('course/<int:pk>/delete/', views.CourseDeleteView.as_view(), name='course-delete'),
    path("staffhome/",views.staffhome, name="NYUVoiceapp-staffhome"),
    path("staffcoursereview/", views.staffcoursereview, name= "NYUVoiceapp-staffcoursereview"),

]
