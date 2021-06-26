from django.contrib import admin
from .models import NewUser, Departement, Roles
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput,Textarea
# Register your models here.

class UserAdminConfig(UserAdmin):
    model = NewUser #Providing Model to be customise
    ordering = ('-create_at',)  #This will make users in models appear in a certain order
    search_fields = ('email','username','first_name') #This will tell what you can search through search bar
    list_filter = ('email','username','first_name','is_active','is_staff')
    #django filter which appears in the admin section, make it filter according which fields
    list_display = ('id','email','username','first_name','is_active','is_staff')
    #What to display on NewUser model table
    fieldsets = (
        (None,{'fields':('email','username','first_name',)}),
        ('permissions',{'fields':('is_active','is_staff',)}),
        ('personals',{'fields':('about','password','born_at', 'gender', 'role', 'departement')}),
    )
    #What to display on particular user and in which order and in which section
    formfield_overrides = {
        NewUser.about:{'widget':Textarea(attrs={'rows':10 , 'cols':40})},
    }
    #adding widget to about section
    add_fieldsets = (
        (None,{
            'classes':('wide',),
            'fields':('email','username','first_name','password1','password2','is_active','is_staff',),
        }),
    )
    #What to as when click add in New user model

admin.site.register(NewUser,UserAdminConfig)
admin.site.register(Departement)
admin.site.register(Roles)