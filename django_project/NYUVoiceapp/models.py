from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone



# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Student = models.BooleanField(default=True)

    @property
    def is_student(self):
        return self.Student

class CourseReview(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	date_posted = models.DateTimeField(default=timezone.now)
	created_at = models.DateTimeField(default=timezone.now)

	def get_absolute_url(self):
		return reverse('course-detail', kwargs={'pk':self.pk})


class rate(models.Model):
	RATING_CHOICES = (
		(1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
	restaurant = models.CharField(max_length=100)
	rating = models.IntegerField(choices=RATING_CHOICES)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	date_posted = models.DateTimeField(default=timezone.now)
	created_at = models.DateTimeField(default=timezone.now)

	def get_absolute_url(self):
		return reverse('res-detail', kwargs={'pk':self.pk})

class BannedWord(models.Model):
    word = models.CharField(max_length=100)

    def __str__(self):
        return self.word