# models.py
from django.db import models

class DetectedFace(models.Model):
    image = models.BinaryField()

