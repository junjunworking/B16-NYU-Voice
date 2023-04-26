from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CourseReview as CourseReview1
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from .forms import UserSignupForm, UserLoginForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
 

def home(request): 
	#return what we want user to see
	return render(request, "NYUVoiceapp/home.html")

def staffhome(request): 
	#return what we want user to see
	return render(request, "NYUVoiceapp/staffhome.html")

def CourseReview(request):

	context={
		'CourseReviews': CourseReview1.objects.all()
	}
	return render(request, "NYUVoiceapp/CourseReview.html" ,context)


def staffcoursereview(request):

	context={
		'CourseReviews': CourseReview1.objects.all()
	}
	return render(request, "NYUVoiceapp/staffcoursereview.html" ,context)


def signup(request):
	if request.method == "POST":
		form = UserSignupForm(request.POST)
		if form.is_valid():
			form.save()
			group = form.cleaned_data["Student"]
			if group ==  True:
				return redirect("NYUVoiceapp-home")
			else:
				return redirect("NYUVoiceapp-staffhome")
	else:
		form = UserSignupForm()

	return render(request, "NYUVoiceapp/signup.html", {'form':form})

def profile(request):
	return render(request, "NYUVoiceapp/profile.html")


def login(request):
	if request.method == 'POST':
		form = UserLoginForm(request,data = request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is None:
				return render(request, "NYUVoiceapp/login.html", {'form':form})
			else:
				auth_login(request, user)
				group = form.cleaned_data["Student"]
				if group == True:
					return redirect("NYUVoiceapp-home")
				else:
					return redirect("NYUVoiceapp-staffhome")
	else:
		form = UserLoginForm()

	return render(request, "NYUVoiceapp/login.html", {'form':form,  'error': 'Username and password did not match'})
