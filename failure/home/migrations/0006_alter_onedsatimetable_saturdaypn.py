# Generated by Django 4.1.3 on 2022-12-04 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_onedsatimetable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onedsatimetable',
            name='saturdaypn',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
