from django.contrib import admin
# Register your models here.

from .models import School_User, Project, Project_assign

##@admin.register(Project_assign)
#class Project_Submissions(admin.ModelAdmin):
 #   list_filter = ['project_status']
    #list_display = ['get_products']


@admin.register(Project)
class Project(admin.ModelAdmin):
    list_display = ['project_name', 'date_of_submission']


@admin.register(School_User)
class Student(admin.ModelAdmin):
    list_display = ['name', 'email', 'profession']


@admin.register(Project_assign)
class PA(admin.ModelAdmin):
    list_display = [ 'st_name','pr_name', 'project_status']