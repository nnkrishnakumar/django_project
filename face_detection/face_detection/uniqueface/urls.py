from django.urls import path
from . import views



urlpatterns = [
    path('', views.unique_face_detection),
    path('detected_faces/', views.detected_faces, name='detected_faces')
]

