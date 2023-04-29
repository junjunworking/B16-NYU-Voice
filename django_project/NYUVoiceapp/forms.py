from django import forms
from django.contrib.auth.models import Group,User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserSignupForm(UserCreationForm):

	email = forms.EmailField()
	Student = forms.BooleanField(required=False)
	class Meta:
		model = User
		fields = ["username","email", "password1", "password2", "Student"]

	def clean_email(self):
		email = self.cleaned_data.get('email')
		if email.endswith('@nyu.edu'):
			return email	
		raise forms.ValidationError('Please Enter your NYU email')



class UserLoginForm(AuthenticationForm):
	Student = forms.BooleanField(required=False)
	model = User
	fields = ["username","password", "Student"]