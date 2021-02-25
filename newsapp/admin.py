from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(Teacher)
# admin.site.register(Category)
# admin.site.register(News)
# admin.site.register(Student)

admin.site.register([Teacher,Student,Category,News,Album,Photo])