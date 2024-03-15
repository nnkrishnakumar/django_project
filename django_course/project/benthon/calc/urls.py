from django.urls import path
from . import views
urlpatterns = [
    path("",views.hello,name="hello"),
    path("hello/",views.home,name="home"),
    path("hello/add",views.add,name="add")
]
