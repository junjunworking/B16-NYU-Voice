from django.contrib import admin

from .models import CourseReview
from .models import rate
from .models import UserProfile
from .models import BannedWord



admin.site.register(CourseReview)
admin.site.register(rate)
admin.site.register(UserProfile)
admin.site.register(BannedWord)
