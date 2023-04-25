from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CourseReview as CourseReview1
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm


def home(request): 
	#return what we want user to see
	return render(request, "NYUVoiceapp/home.html")

def CourseReview(request):
	context={
		'CourseReviews': CourseReview1.objects.all()
	}
	return render(request, "NYUVoiceapp/CourseReview.html" ,context)

def signup(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("NYUVoiceapp-home")
	else:
		form = UserCreationForm()

	return render(request, "NYUVoiceapp/signup.html", {'form':form})

def login_failed(request):
    return render(request, 'login_failed.html')