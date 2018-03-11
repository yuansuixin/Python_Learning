from django.shortcuts import render

# Create your views here.
from .models import Grades,Students
from django.http import HttpResponse

def index(request):
    return HttpResponse('macy is a good girl')

def grades(request):
    #去模板里去数据
    gradesList = Grades.objects.all()
    #将数据传递给模板，模板在渲染页面，将渲染好的页面返回浏览器
    return render(request,'myApp/grades.html',{'grades':gradesList})

def students(request):
    studentsList = Students.objects.all()
    return render(request,'myApp/students.html',{'students':studentsList})

def gradesStudents(request,num):
    grade = Grades.objects.get(pk=num)
    studentsList = grade.students_set.all()
    for item in studentsList:
        print(item.sgrade.__str__)
    return render(request,'myApp/students.html',{'students':studentsList})






