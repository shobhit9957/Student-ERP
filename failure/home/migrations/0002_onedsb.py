# Generated by Django 4.1.3 on 2022-11-27 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Onedsb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50)),
                ('two', models.CharField(max_length=50)),
                ('three', models.CharField(max_length=50)),
                ('four', models.CharField(max_length=50)),
                ('five', models.CharField(max_length=50)),
                ('six', models.CharField(max_length=50)),
                ('seven', models.CharField(max_length=50)),
                ('date', models.DateField()),
            ],
        ),
    ]
