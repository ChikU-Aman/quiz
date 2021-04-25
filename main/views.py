from django.shortcuts import render
from .models import Question
# Create your views here.
def index(request):
    question = Question.objects.all() 
    return render(request,"index.html",{'exam':question})