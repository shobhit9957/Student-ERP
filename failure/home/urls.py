from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name ='home'),
    
    # Index page of this site
    path("index.html", views.index, name='index'),
    
    # Faculty Link Path's
    path("faculty.html", views.faculty, name ='faculty'),

    # Faculty Login path
    path("login.html", views.login, name='login'),
    
    # Student Path
    path("student.html", views.student, name ='student'),

    # OneDSA Faculty Path's
    path("dsaf.html", views.dsaf, name ='dsa'),
    path("dsafsit.html", views.dsafsit, name='dsasit'),
    path("dsaftimetable.html", views.dsaftimetable, name='dsasit'),
    path("dsafportion.html", views.dsafportion, name='dsasit'),
    path("dsafselect.html", views.dsafselect, name='dsafselect'),

    # OneDSB Faculty Path's
    path("dsbf.html", views.dsbf, name ='dsbf'),

    # OneDSA Path's
    path("dsa.html", views.dsa, name='dsa'),
    path("dsaselect.html", views.dsaselect, name='dsaselect'),
    path("dsasit.html", views.dsasit, name='dsasit'),
    path("dsatimetable.html", views.dsatimetable, name='dsatimetable'),
    path("dsaportion.html", views.dsaportion, name='dsaportion'),
    # OneDSB Path's
    path("dsb.html", views.dsb, name='dsb'),
]