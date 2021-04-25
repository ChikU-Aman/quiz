from django.db import models

# Create your models here.
class Question(models.Model):
    Question = models.CharField(max_length=200)
    opt1 = models.CharField(max_length=100)
    opt2 = models.CharField(max_length=100)
    opt3 = models.CharField(max_length=100)
    opt4 = models.CharField(max_length=100)
    ans = models.CharField(max_length=100)
