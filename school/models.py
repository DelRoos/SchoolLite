from enum import unique
from django.db import models
from users.models import NewUser

# Create your models here.
# class Speciality(models.Model):
#     letter = models.CharField(max_length=10, unique=True)
#     describe = models.TextField(blank=True)
    
# class Level(models.Model):
#     num = models.IntegerField(unique=True)
#     describe = models.TextField(blank=True)
    
# class Classe(models.Model):
#     level = models.ForeignKey(Level, on_delete=models.CASCADE)
#     speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE, related_name='spec_class')

class Classe(models.Model):
    SPECIALITIES = [
        ('C', 'Mathematique'),
        ('D', 'Physique'),
        ('TI', 'Chimie'),
        ('ALL', 'Histoire'),
        ('ESP', 'Science'),
        ('CH', 'ECM'),
    ]
    LEVELS = [
        ('6', '6 eime'),
        ('5', '5 eime'),
        ('4', '4 eime'),
        ('3', '3 eime'),
        ('2', 'seconde'),
        ('1', 'premiere'),
        ('0', 'terminale'),
    ]
    level = models.CharField(
        max_length=2,
        choices=LEVELS,
        null=True, 
        blank=True
        # Level, on_delete=models.CASCADE
    )
    speciality = models.CharField(
        # Speciality, on_delete=models.CASCADE, related_name='spec_class'
        max_length=7,
        choices=SPECIALITIES,
        null=True, 
        blank=True
    )


class ClassRoom(models.Model):
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE, related_name="classroom_user") 
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE, related_name="classroom_classe") 
    
class Matter(models.Model):
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE, related_name='class_matter')
    credit = models.IntegerField()

class Program(models.Model):
    matter = models.ForeignKey(Matter, on_delete=models.CASCADE, related_name='matter_program')
    title = models.CharField(max_length=255, unique=True)
    describe = models.TextField()
    limit_day = models.DateField()
    course_day = models.DateField()
    begin_time = models.TimeField()
    duration = models.IntegerField()
    status = models.BooleanField(default=False, blank=True)

class Lecon(models.Model):
    program = models.ForeignKey(Program, unique=True, on_delete=models.CASCADE, related_name="program_lecon")
    content = models.TextField()

class Question(models.Model):
    lesson = models.ForeignKey(Lecon, on_delete=models.CASCADE, related_name="lecon_question")
    content = models.CharField(max_length=10000)

class Reponse(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="question_response")
    content = models.CharField(max_length=1000)
    verify = models.BooleanField()
