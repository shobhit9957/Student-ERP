# Generated by Django 4.1.3 on 2022-12-04 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_rename_saturdaypn_onedsatimetable_saturdayfn1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='onedsatimetable',
            old_name='saturdayfn1',
            new_name='saturdaypn',
        ),
        migrations.RenameField(
            model_name='onedsatimetable',
            old_name='saturdayfn2',
            new_name='saturdaypt',
        ),
        migrations.AlterField(
            model_name='onedsatimetable',
            name='fridayfn',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='onedsatimetable',
            name='fridaypn',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='onedsatimetable',
            name='fridaypt',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='onedsatimetable',
            name='mondayfn',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='onedsatimetable',
            name='mondaypn',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='onedsatimetable',
            name='mondaypt',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='onedsatimetable',
            name='thursdayfn',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='onedsatimetable',
            name='thursdaypn',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='onedsatimetable',
            name='thursdaypt',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='onedsatimetable',
            name='tuesdayfn',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='onedsatimetable',
            name='tuesdaypn',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='onedsatimetable',
            name='tuesdaypt',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='onedsatimetable',
            name='wednesdayfn',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='onedsatimetable',
            name='wednesdaypn',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='onedsatimetable',
            name='wednesdaypt',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
