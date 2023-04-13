from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Onedsa, Onedsb,OneDsaPortion, OneDsaTimeTable, OneDsaSit
from django.contrib import messages

# Create your views here.
# The index page of this application
def index(request):
    return render(request, 'index.html')

# This is for faculties to select the concern year, course and section of the student's for providing concern details that will be accessed by the students.
def faculty(request):
    return render( request, 'faculty.html')

# This is for faculty login
def login(request):
    return render(request, 'login.html')

# This is for students to select their concern year, course and section!
def student(request):
    return render( request, 'student.html')


# Allows the student of OneDSA to choose an option and obtain it's result ex: daily test marks, weekend portion, sitting allotments, time table etc.
def dsaselect(request):
    return render( request, 'dsaselect.html')
    
# This page will render and represent the daily test marks to the students of One DSA
def dsa(request):
    mark_list = Onedsa.objects.all().last()
    return render(request, 'dsa.html', {'mark_listonedsa': mark_list})
# This page will render and represent the Sitting Allotments to the students of One DSB
def dsasit(request):
    sit_alot = OneDsaSit.objects.all().last()
    return render( request, 'dsasit.html',{'sit_alot': sit_alot})

# This page is for faculties to provide the sitting allotments to the students of OneDSA
def dsafsit(request):
    if request.method == "POST":
        classname1 = request.POST.get('classname1')
        rollno1 = request.POST.get('rollno1')
        classname2 = request.POST.get('classname2')
        rollno2 = request.POST.get('rollno2')
        classname3 = request.POST.get('classname3')
        rollno3 = request.POST.get('rollno3')
        classname4 = request.POST.get('classname4')
        rollno4 = request.POST.get('rollno4')
        classname5 = request.POST.get('classname5')
        rollno5 = request.POST.get('rollno5')
        
        onedsasit = OneDsaSit(classname1 = classname1, rollno1 = rollno1 , classname2 = classname2, rollno2 = rollno2, classname3 = classname3, rollno3 = rollno3, classname4 = classname4, rollno4 = rollno4, classname5=classname5, rollno5 = rollno5)
        onedsasit.save()
        messages.success(request, 'The Sitting Allotments has been provided for the concern batch according to the information given by you!')
    return render(request, "dsafsit.html")

# This page will render and represent the timetable to the students of OneDSA
def dsatimetable(request):
    timetable_onedsa = OneDsaTimeTable.objects.all().last()
    return render( request, 'dsatimetable.html', {'timetable_onedsa': timetable_onedsa})
# This page is for faculties to provide the timetable to the students of OneDSA

# This page will render and represent the portion to the students of OneDSA
def dsaportion(request):
    portion_onedsa = OneDsaPortion.objects.all().last()
    return render( request, 'dsaportion.html',{'portion_onedsa': portion_onedsa} )
def dsaftimetable(request):
    if request.method == "POST":
        mondaypn = request.POST.get('mondaypn')
        mondaypt = request.POST.get('mondaypt')
        mondayfn = request.POST.get('mondayfn')
        tuesdaypn = request.POST.get('tuesdaypn')
        tuesdaypt = request.POST.get('tuesdaypt')
        tuesdayfn = request.POST.get('tuesdayfn')
        wednesdaypn = request.POST.get('wednesdaypn')
        wednesdaypt = request.POST.get('wednesdaypt')
        wednesdayfn = request.POST.get('wednesdayfn')
        thursdaypn = request.POST.get('thursdaypn')
        thursdaypt = request.POST.get('thursdaypt')
        thursdayfn = request.POST.get('thursdayfn')
        fridaypn = request.POST.get('fridaypn')
        fridaypt = request.POST.get('fridaypt')
        fridayfn = request.POST.get('fridayfn')
        saturdaypn = request.POST.get('saturdaypn')
        saturdaypt = request.POST.get('saturdaypt')
        saturdayfn = request.POST.get('saturdayfn')
        
        onedsatimetable = OneDsaTimeTable(mondaypn = mondaypn, mondaypt = mondaypt , mondayfn = mondayfn, tuesdaypn = tuesdaypn, tuesdaypt = tuesdaypt, tuesdayfn = tuesdayfn, wednesdaypn = wednesdaypn, wednesdaypt = wednesdaypt, wednesdayfn=wednesdayfn, thursdaypn=thursdaypn, thursdaypt = thursdaypt, thursdayfn = thursdayfn, fridaypn = fridaypn, fridaypt = fridaypt, fridayfn = fridayfn , saturdaypn = saturdaypn , saturdaypt=saturdaypt, saturdayfn = saturdayfn)
        onedsatimetable.save()
        messages.success(request, 'The timetable has been entered for the concern batch according to the information given by you!')
    return render(request, "dsaftimetable.html")

# Allows the faculty to provide the details that can be accessed by students of OneDSA ex: daily test marks, weekend portion, sitting allotments, time table etc.
def dsafselect(request):
    return render( request, 'dsafselect.html')

# This page is for faculties to provide the protion to the students of OneDSA
def dsafportion(request):
    if request.method == "POST":
        date1 = request.POST.get('date1')
        sub1 = request.POST.get('sub1')
        por1 = request.POST.get('por1')
        date2 = request.POST.get('date2')
        sub2 = request.POST.get('sub2')
        por2 = request.POST.get('por2')
        date3 = request.POST.get('date3')
        sub3 = request.POST.get('sub3')
        por3 = request.POST.get('por3')
        date4 = request.POST.get('date4')
        sub4 = request.POST.get('sub4')
        por4 = request.POST.get('por4')
        date5 = request.POST.get('date5')
        sub5 = request.POST.get('sub5')
        por5 = request.POST.get('por5')
        date6 = request.POST.get('date6')
        sub6 = request.POST.get('sub6')
        por6 = request.POST.get('por6')
        date7 = request.POST.get('date7')
        sub7 = request.POST.get('sub7')
        por7 = request.POST.get('por7')
        onedsaportion = OneDsaPortion(date1 = date1, sub1 = sub1 , por1 = por1, date2 = date2, sub2 = sub2, por2 = por2, date3 = date3, sub3 = sub3, por3=por3, date4=date4, sub4 = sub4, por4 = por4, date5 = date5, sub5 = sub5, por5 = por5 , date6 = date6 , sub6=sub6, por6 = por6, date7 = date7, sub7 = sub7 , por7 = por7)
        onedsaportion.save()
        messages.success(request, 'The portion has been entered for the concern batch according to the dates and subjects given by you!')
    return render(request, "dsafportion.html")

# This page will render and represent the daily test marks to the students of OneDSB
def dsb(request):
    mark_list = Onedsb.objects.all().last()
    return render(request, 'dsb.html', {'mark_listonedsb': mark_list})

# This page is for the faculties to provide the OneDSB Daily Test Marks which will be accessed by students of OneDSB
def dsbf(request):
    if request.method == "POST":
        subject = request.POST.get('subject')
        two = request.POST.get('two')
        three = request.POST.get('three')
        four = request.POST.get('four')
        five = request.POST.get('five')
        six = request.POST.get('six')
        seven = request.POST.get('seven')
        onedsb = Onedsb(subject = subject, two = two, three = three, four = four, five = five, six = six, seven = seven, date = datetime.today() )
        onedsb.save()
        messages.success(request, 'The marks has been entered for the concern students!')
    return render(request, "dsbf.html")

# This page is for the faculties to provide the OneDSB Daily Test Marks which will be accessed by students of OneDSB
def dsaf(request):
    if request.method == "POST":
        subject = request.POST.get('subject')
        two = request.POST.get('two')
        three = request.POST.get('three')
        four = request.POST.get('four')
        five = request.POST.get('five')
        six = request.POST.get('six')
        seven = request.POST.get('seven')
        eight = request.POST.get('eight')
        nine = request.POST.get('nine')
        ten = request.POST.get('ten')
        eleven = request.POST.get('eleven')
        twelve = request.POST.get('twelve')
        thirteen = request.POST.get('thirteen')
        fourteen = request.POST.get('fourteen')
        fifteen = request.POST.get('fifteen')
        onedsa = Onedsa(subject = subject, two = two, three = three, four = four, five = five, six = six, seven = seven, eight=eight,nine=nine,ten=ten,eleven=eleven,twelve=twelve,thirteen=thirteen,fourteen=fourteen,fifteen=fifteen,date = datetime.today() )
        onedsa.save()
        messages.success(request, 'The marks has been entered for the concern students!')
    return render(request, "dsaf.html")