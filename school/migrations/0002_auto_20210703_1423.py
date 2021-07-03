# Generated by Django 3.2 on 2021-07-03 14:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matter',
            name='matter',
            field=models.CharField(blank=True, choices=[('math', 'Mathematique'), ('phy', 'Physique'), ('chim', 'Chimie'), ('hist', 'Histoire'), ('svt', 'Science'), ('geo', 'Geographie'), ('eng', 'Anglais'), ('fr', 'Francais'), ('ecm', 'ECM'), ('stud', 'student'), ('eps', 'sport'), ('inf', 'Informatique')], max_length=7, null=True),
        ),
        migrations.CreateModel(
            name='TestResults',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.FloatField()),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='note_test', to='school.lecon')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='note_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
