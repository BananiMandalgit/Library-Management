from django.shortcuts import render,redirect
from .models import student,Book
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import login as auth_login
from django.contrib import messages

# Create your views here.

def login(request):
    if request.method == "POST":
        password = request.POST['password']
        student_id = request.POST['student_id']
        try:
            students= student.objects.get(student_id=student_id)
            if check_password(password,students.password):
                auth_login(request,students)
                return redirect('studentinfo')
            else:
                return render(request,'LOGIN.html',{'error':'Invalid password'})
        except student.DoesNotExist:
            return render(request,'LOGIN.html',{'error': "Email does not exist"})
    else:
        return render(request, "LOGIN.html")
    
def signup(request):
    if request.method =='POST':
        fname = request.POST['name']
        email = request.POST['email']
        student_id = request.POST['student_id']
        password = request.POST['password']
        hashpass = make_password(password)
        department = request.POST['department']
        gender = request.POST['gender']
        year = request.POST['year']
        Students = student(student_id=student_id, name=fname, email=email, password=hashpass, department=department, gender=gender, year=year)
        Students.save()
        return redirect('index')
    else:
        return render(request, "SIGN_UP.html")
    
def index(req):
    return render(req, "FRONT.html")

def add(request):
    if request.method == "POST":
        ftitle =request.POST['title'],
        author =request.POST['author'],
        publishDate =request.POST['publishDate'],
        isbn =request.POST['isbn'],
        in_stock =request.POST['in_stock']
        book = Book(title= ftitle, author= author, publishDate=publishDate, isbn=isbn, in_stock=in_stock)
        book.save()
        # messages.success(request, "Book added successfully!")
        return redirect('book')
    else:
        return render(request,'add.html')

def find(request):
    return render(request, 'find.html')

def help(request):
    return render(request, 'help.html')

def front(request):
    return render(request, 'front.html')

def books(request):
    books = Book.objects.all()
    return render(request, 'book.html', {'books': books})

def students(request):
    students = student.objects.all()
    return render(request, 'studentinfo.html', {'students':students})
