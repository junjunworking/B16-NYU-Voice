from django.contrib import admin

from .models import CourseReview
from .models import rate


admin.site.register(CourseReview)
admin.site.register(rate)