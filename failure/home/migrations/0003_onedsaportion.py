# Generated by Django 4.1.3 on 2022-12-02 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_onedsb'),
    ]

    operations = [
        migrations.CreateModel(
            name='OneDsaPortion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date1', models.DateField()),
                ('sub1', models.CharField(max_length=50)),
                ('por1', models.CharField(max_length=500)),
                ('date2', models.DateField()),
                ('sub2', models.CharField(max_length=50)),
                ('por2', models.CharField(max_length=500)),
                ('date3', models.DateField()),
                ('sub3', models.CharField(max_length=50)),
                ('por3', models.CharField(max_length=500)),
                ('date4', models.DateField()),
                ('sub4', models.CharField(max_length=50)),
                ('por4', models.CharField(max_length=500)),
                ('date5', models.DateField()),
                ('sub5', models.CharField(max_length=50)),
                ('por5', models.CharField(max_length=500)),
                ('date6', models.DateField()),
                ('sub6', models.CharField(max_length=50)),
                ('por6', models.CharField(max_length=500)),
                ('date7', models.DateField()),
                ('sub7', models.CharField(max_length=50)),
                ('por7', models.CharField(max_length=500)),
                ('date8', models.DateField()),
                ('sub8', models.CharField(max_length=50)),
                ('por8', models.CharField(max_length=500)),
            ],
        ),
    ]
