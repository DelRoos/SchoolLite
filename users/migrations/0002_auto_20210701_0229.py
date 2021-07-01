# Generated by Django 3.2 on 2021-07-01 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='departement',
            field=models.CharField(blank=True, choices=[('math', 'Mathematique'), ('phy', 'Physique'), ('chim', 'Chimie'), ('hist', 'Histoire'), ('svt', 'Science'), ('ecm', 'ECM'), ('stud', 'student'), ('eps', 'sport')], max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='role',
            field=models.CharField(blank=True, choices=[('stud', 'Student'), ('teach', 'Teacher'), ('admin', 'Administrator')], max_length=7, null=True),
        ),
        migrations.DeleteModel(
            name='Departement',
        ),
        migrations.DeleteModel(
            name='Roles',
        ),
    ]
