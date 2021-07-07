from django.contrib import admin
from .models import Lecon, Matter, Classe, ClassRoom, Program, Question, Reponse, TestResults

# Register your models here.
# admin.site.register(Speciality)
admin.site.register(Matter)
admin.site.register(Classe)
# admin.site.register(Level)
admin.site.register(Program)
admin.site.register(Lecon)
admin.site.register(Reponse)
admin.site.register(ClassRoom)
admin.site.register(Question)
admin.site.register(TestResults)
