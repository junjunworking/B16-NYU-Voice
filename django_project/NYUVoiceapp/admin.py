from django.contrib import admin

from .models import CourseReview
from .models import rate
from .models import UserProfile



admin.site.register(CourseReview)
admin.site.register(rate)
admin.site.register(UserProfile)