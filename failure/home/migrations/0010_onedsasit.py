# Generated by Django 4.1.3 on 2022-12-04 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_rename_saturdayfn1_onedsatimetable_saturdaypn_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OneDsaSit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classname1', models.CharField(max_length=500, null=True)),
                ('rollno1', models.CharField(max_length=500, null=True)),
                ('classname2', models.CharField(max_length=500, null=True)),
                ('rollno2', models.CharField(max_length=500, null=True)),
                ('classname3', models.CharField(max_length=500, null=True)),
                ('rollno3', models.CharField(max_length=500, null=True)),
                ('classname4', models.CharField(max_length=500, null=True)),
                ('rollno4', models.CharField(max_length=500, null=True)),
                ('classname5', models.CharField(max_length=500, null=True)),
                ('rollno5', models.CharField(max_length=500, null=True)),
            ],
        ),
    ]