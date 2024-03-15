from django.contrib import admin
#step5: import from .models import database
from .models import Student
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','roll','city']
