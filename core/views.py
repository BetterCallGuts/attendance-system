from django.shortcuts import render, redirect
from .models import Student, Course, StudentCourseRel
from datetime import date
from django.http  import HttpResponse
# Create your views here.

def attender(req, pk):
    if req.method == "POST":
          a = True
          ds = ""
          for i in req.POST:
            if a:
              a = False
              continue
            ds += f"{i},"
          
          the_student = StudentCourseRel.objects.get(pk=pk)
          the_student.attend = ds
          the_student.save()

          return HttpResponse("<script>window.close()</script>")
    
    
    

    the_course = StudentCourseRel.objects.get(pk=pk)
    if the_course.attend is None:
      ds = []
    else:
      ds = the_course.attend.split(",")[:-1]
    
    
    start_date = str(the_course.course.starting_date).split("-")
    end_date   = str(the_course.course.ending_date).split("-")

    start_date = [int(x) for x in start_date]
    end_date   = [int(x) for x in end_date]
    temp       = start_date
    start_date = date(*start_date)
    end_date   = date(*end_date)
    
    days       = end_date - start_date
    days       = int(str(days).split(',')[0].replace('days', "").replace("day", ""))
    returned_date = []
    try:
      add_month = 0 
      remove_from_days = 0
      temp_2 = temp
      i = 0
      b = 0
      if_in = []
      for g in the_course.course.Days.all():
        if_in.append(g.name)
      while True:
        b+=1
        ch = False
        if temp_2[1 ]+ add_month > 12:
          temp_2[1] = 1
          add_month = 0
          temp_2[0] += 1

        try:
          date_by_num = date(temp_2[0], temp_2[1 ]+ add_month, temp_2[2]+i - remove_from_days)

          sentance = f"{date_by_num} - {date_by_num.strftime('%A')}"
          if sentance in ds:
            ch = True
          if date_by_num.strftime('%A') in if_in:
            returned_date.append({"name": sentance , 'ch':ch})

           
          if end_date == date_by_num:
            break
        
        except ValueError:
          add_month +=1
          
          temp_2[2]  = 0
          remove_from_days = i
        
        i +=1
        
    except ValueError:

        pass


    return render(req, "atten.html", {"data":returned_date})


  


def index(req):
  
  
  
  return redirect('/admin')