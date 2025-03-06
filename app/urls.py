from django.urls import path
from . import views

urlpatterns=[
    path("",views.index, name="index"),
    path("login/",views.login, name='login'),
    path("signup/",views.signup, name="signup"),
    path("add/",views.add, name="add"),
    path("find/",views.find, name="find"),
    path("help/",views.help, name="help"),
    path("front/",views.front, name="front"),
    path("book/",views.books, name="book"),
    path("studentinfo/",views.students, name="studentinfo")

]
