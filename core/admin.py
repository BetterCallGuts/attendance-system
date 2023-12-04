from django.contrib import admin

# Register your models here.

from .models import (
  Student,
  Faculty,
  Instructor,
  Course
  )

class StudentAdminStyle(admin.ModelAdmin):
  list_display = ("name","faculty","levels", "Date_ofj","aca_id" , "password")
  list_filter  = (
                  "levels",
                  "faculty"

                  )
  search_fields = (
    "name",
    "aca_id",
    "aca_em",
    
  )
  
  fields  = (
    "name",
    "aca_id",
    "aca_em",
    "password",
    "faculty",
    "Date_ofj",
    "levels",
    

    "Attnder",
  )
  
  readonly_fields = (
    "Attnder",
  )
class InstructorAdminStyle(admin.ModelAdmin):
  
  list_display = (
    "name",

  )
  list_filter = (
    'ins_course',
  )
  
  


admin.site.register(Student, StudentAdminStyle)
admin.site.register(Faculty)
admin.site.register(Instructor, InstructorAdminStyle)
admin.site.register(Course)