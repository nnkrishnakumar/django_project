from django.db import models

# Create your models here.

# step 2: python manage.py makemigrate   # it is used to create database
# step 3: python manage.py migrate     # it create a lot of table in database.
# step 4: python manage.py createsuperuser  # we have to create superuser to keep our data into db
# step 5: super user create with user name "admin" and password "admin"

class Student(models.Model):
    name=models.CharField(max_length=100)
    roll=models.IntegerField()
    city=models.CharField(max_length=100)

