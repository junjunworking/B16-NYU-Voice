from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CourseReview as CourseReview1
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from .forms import UserSignupForm, UserLoginForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.views.generic import ListView, CreateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import rate as rate1
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
			return redirect("/login")
			# group = form.cleaned_data["Student"]
			# if group ==  True:
			# 	return redirect("NYUVoiceapp-home")
			# else:
			# 	return redirect("NYUVoiceapp-staffhome")
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

class CourseListView(ListView):
	model = CourseReview1
	template_name="NYUVoiceapp/CourseReview.html"
	context_object_name = 'CourseReviews'
	ordering = ['-date_posted']

class StaffCourseListView(ListView):
	model = CourseReview1
	template_name="NYUVoiceapp/staffcoursereview.html"
	context_object_name = 'CourseReviews'
	ordering = ['-date_posted']

class CourseCreateView(LoginRequiredMixin, CreateView):
	model = CourseReview1
	fields = ['title','content']
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class CourseDetailView(DetailView):
	model = CourseReview1

class CourseDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = CourseReview1
	success_url = '/NYUVoiceapp/CourseReview'
	def test_func(self):
		CourseReview1 = self.get_object()
		if self.request.user == CourseReview1.author:
			return True
		return False

def rate(request):
	context={
		'rates': rate1.objects.all()
	}
	return render(request, "NYUVoiceapp/rate.html", context)

class rateView(DetailView):
	model = rate1

class rateListView(ListView):
	model = rate1
	template_name="NYUVoiceapp/rate.html"
	context_object_name = 'rates'
	ordering = ['-date_posted']

class StaffRestaurantRating(ListView):
	model = rate1
	template_name="NYUVoiceapp/staffrestaurantrating.html"
	context_object_name = 'rates'
	ordering = ['-date_posted']

class rateCreateView(LoginRequiredMixin, CreateView):
	model = rate1
	fields = ['restaurant', 'rating']
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class rateDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = rate1
	success_url = '/NYUVoiceapp/rate'
	def test_func(self):
		rate1 = self.get_object()
		if self.request.user == rate1.author:
			return True
		return False
	
def direct_message(request, receiver):
	receiver_context = {'receiver': receiver}
	return render(request, "NYUVoiceapp/direct_message.html", receiver_context)


















