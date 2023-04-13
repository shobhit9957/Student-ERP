# Generated by Django 4.1.3 on 2022-12-04 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_onedsaportion_date8_remove_onedsaportion_por8_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OneDsaTimeTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mondaypn', models.CharField(max_length=500)),
                ('mondaypt', models.CharField(max_length=500)),
                ('mondayfn', models.CharField(max_length=500)),
                ('tuesdaypn', models.CharField(max_length=500)),
                ('tuesdaypt', models.CharField(max_length=500)),
                ('tuesdayfn', models.CharField(max_length=500)),
                ('wednesdaypn', models.CharField(max_length=500)),
                ('wednesdaypt', models.CharField(max_length=500)),
                ('wednesdayfn', models.CharField(max_length=500)),
                ('thursdaypn', models.CharField(max_length=500)),
                ('thursdaypt', models.CharField(max_length=500)),
                ('thursdayfn', models.CharField(max_length=500)),
                ('fridaypn', models.CharField(max_length=500)),
                ('fridaypt', models.CharField(max_length=500)),
                ('fridayfn', models.CharField(max_length=500)),
                ('saturdaypn', models.CharField(max_length=500)),
                ('saturdaypt', models.CharField(max_length=500)),
                ('saturdayfn', models.CharField(max_length=500)),
            ],
        ),
    ]
