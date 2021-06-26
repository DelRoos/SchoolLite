from django.contrib import admin
from .models import Speciality, Matter, Classe, Level, ClassRoom

# Register your models here.
admin.site.register(Speciality)
admin.site.register(Matter)
admin.site.register(Classe)
admin.site.register(Level)
admin.site.register(ClassRoom)