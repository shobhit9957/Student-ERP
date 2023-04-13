from django.db import models

# Create your models here.
# Stores the onedsa daily test marks
class Onedsa(models.Model):
    subject = models.CharField(max_length=50, null=True)
    two = models.CharField(max_length=50, null=True)
    three = models.CharField(max_length=50, null=True)
    four = models.CharField(max_length=50, null=True)
    five = models.CharField(max_length=50, null=True)
    six = models.CharField(max_length=50, null=True)
    seven = models.CharField(max_length=50, null=True)
    eight = models.CharField(max_length=50, null=True)
    nine = models.CharField(max_length=50, null=True)
    ten = models.CharField(max_length=50, null=True)
    eleven = models.CharField(max_length=50, null=True)
    twelve = models.CharField(max_length=50, null=True)
    thirteen = models.CharField(max_length=50, null=True)
    fourteen = models.CharField(max_length=50, null=True)
    fifteen = models.CharField(max_length=50, null=True)
    date = models.DateField()

    def __str__(self):
        return self.subject

# Stores the onedsa daily test portion
class OneDsaPortion(models.Model):
    date1 = models.DateField()
    sub1 = models.CharField(max_length=50)
    por1 = models.CharField(max_length=500)
    date2 = models.DateField()
    sub2 = models.CharField(max_length=50)
    por2 = models.CharField(max_length=500)
    date3 = models.DateField()
    sub3 = models.CharField(max_length=50)
    por3 = models.CharField(max_length=500)
    date4 = models.DateField()
    sub4 = models.CharField(max_length=50)
    por4 = models.CharField(max_length=500)
    date5 = models.DateField()
    sub5 = models.CharField(max_length=50)
    por5 = models.CharField(max_length=500)
    date6 = models.DateField()
    sub6 = models.CharField(max_length=50)
    por6 = models.CharField(max_length=500)
    date7 = models.DateField()
    sub7 = models.CharField(max_length=50)
    por7 = models.CharField(max_length=500)

# Stores the onedsa time table 
class OneDsaTimeTable(models.Model):
    mondaypn = models.CharField(max_length=500, null=True)
    mondaypt = models.CharField(max_length=500, null=True)
    mondayfn = models.CharField(max_length=500, null=True)
    tuesdaypn = models.CharField(max_length=500, null=True)
    tuesdaypt = models.CharField(max_length=500, null=True)
    tuesdayfn = models.CharField(max_length=500, null=True)
    wednesdaypn = models.CharField(max_length=500, null=True)
    wednesdaypt = models.CharField(max_length=500, null=True)
    wednesdayfn = models.CharField(max_length=500, null=True)
    thursdaypn = models.CharField(max_length=500, null=True)
    thursdaypt = models.CharField(max_length=500, null=True)
    thursdayfn = models.CharField(max_length=500, null=True)
    fridaypn = models.CharField(max_length=500, null=True)
    fridaypt = models.CharField(max_length=500, null=True)
    fridayfn = models.CharField(max_length=500, null=True)
    saturdaypn = models.CharField(max_length=500, null=True)
    saturdaypt = models.CharField(max_length=500, null=True)
    saturdayfn = models.CharField(max_length=500, null=True)

# Stores the onedsa sitting allotments  
class OneDsaSit(models.Model):
    classname1 = models.CharField(max_length=500, null=True)
    rollno1 = models.CharField(max_length=500, null=True)
    classname2 = models.CharField(max_length=500, null=True)
    rollno2 = models.CharField(max_length=500, null=True)
    classname3 = models.CharField(max_length=500, null=True)
    rollno3 = models.CharField(max_length=500, null=True)
    classname4 = models.CharField(max_length=500, null=True)
    rollno4 = models.CharField(max_length=500, null=True)
    classname5 = models.CharField(max_length=500, null=True)
    rollno5 = models.CharField(max_length=500, null=True)

# Stores the onedsb daily test marks
class Onedsb(models.Model):
    subject = models.CharField(max_length=50)
    two = models.CharField(max_length=50)
    three = models.CharField(max_length=50)
    four = models.CharField(max_length=50)
    five = models.CharField(max_length=50)
    six = models.CharField(max_length=50)
    seven = models.CharField(max_length=50)
    date = models.DateField()
    def __str__(self):
        return self.subject