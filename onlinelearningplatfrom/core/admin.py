from django.contrib import admin
from .models import Profile, Course, Lessons, Enrollment, Progress

# Register your models here.
admin.site.register(Profile)
admin.site.register(Course)
admin.site.register(Lessons)
admin.site.register(Enrollment)
admin.site.register(Progress)
