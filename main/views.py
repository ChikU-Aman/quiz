from django.shortcuts import render, HttpResponseRedirect
from .models import Question
# Create your views here.
def index(request):
    if request.method=="POST":
        start = int(request.POST['start'])
        end = int(request.POST['end']) 
        question = Question.objects.all()[start:end+1]
        #print(question)
        f = open("set.txt", "w")
        j = 1
        for i in question:
            f.write(str(j)+") ")
            f.write(i.Question)
            f.write("\n")
            f.write(i.opt1)
            f.write("\n")
            f.write(i.opt2)
            f.write("\n")
            f.write(i.opt3)
            f.write("\n")
            f.write(i.opt4)
            f.write("\n")
            f.write(i.ans)
            f.write("\n")
            j+=1
        f.close()
        return render(request,"index.html",{'exam':question})
    else:
        question = Question.objects.all() 
        return render(request,"index.html",{'exam':question})