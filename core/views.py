from django.shortcuts import render, redirect
from .models import Student, Course, StudentCourseRel
from datetime import date
from django.http  import HttpResponse
from django.utils.html import mark_safe
# Create your views here.


def attend_grid(req, pk):
    the_course = Course.objects.get(pk=pk)
    
    rel_in = StudentCourseRel.objects.filter(course=the_course)
    
    
    
    
    if req.method == "POST":
            a = True
            ds = ""
            
            studentss = Student.objects.all()
            for i in studentss:
              ds = ""
              for k in req.POST:
                
                if i.name in k:
                    print("We are in bby")
                    #  name = k.split("$")[1]
              
                    day  = k.split("$")[0].replace("|","-")
                    ds += f"{day},"
                    print(day)
              rel = StudentCourseRel.objects.get(student=i,course=the_course)
              rel.attend = ds
              rel.save()
            # for i in req.POST:
            #   if a:
            #     a = False
            #     continue

            #   name = i.split("$")[1]
              
            #   day  = i.split("$")[0]

            #   ds += f"{day},"

            #   st  = Student.objects.get(name=name)
            #   rel =rel_in.get(student=st)
            #   rel.attend = ds
            #   rel.save()

                
            
            for s in req.POST.values():
              print(s)
            
            
            # the_student = StudentCourseRel.objects.get(pk=pk)
            # the_student.attend = ds
            # the_student.save()

            return HttpResponse("<script>window.close()</script>")
      
    first__ = True
    returned_date = []
    for s in rel_in:

      the_course = s
      if the_course.attend is None:
        ds = []
      else:
        ds = the_course.attend.split(",")[:-1]

      student_list = []
      
      start_date = str(the_course.course.starting_date).split("-")
      end_date   = str(the_course.course.ending_date).split("-")
      start_date = [int(x) for x in start_date]
      end_date   = [int(x) for x in end_date]
      temp       = start_date
      start_date = date(*start_date)
      end_date   = date(*end_date)
      
      days       = end_date - start_date
      days       = int(str(days).split(',')[0].replace('days', "").replace("day", ""))
      
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

            sentance = f"{date_by_num} | {date_by_num.strftime('%A')}"
            if f"{date_by_num} - {date_by_num.strftime('%A')}" in ds:
              ch = True
            if date_by_num.strftime('%A') in if_in:
              student_list.append({"name": sentance , 'ch':ch})

            
            if end_date == date_by_num:
              if first__:
                first__ = False

                p  = []
                for i in student_list:
                  temp_3 = i["name"]
                  i["name"] = i['name'].split("|")[0] +"<br>" +i['name'].split("|")[1][0:3] 
                  p.append( mark_safe(i['name']))
                  i['name'] = temp_3

                returned_date.append([p])

              returned_date.append([student_list, s.student.name])
              break
          
          except ValueError:
            add_month +=1
            
            temp_2[2]  = 0
            remove_from_days = i
          
          i +=1
          
      except ValueError:

          pass
    

  # 
    return render(req, "attend-grid.html", {'data' : returned_date, "stu" : returned_date[1:]})

def import_ex(req,pk):
  
  
  return render(req, "imexexcel.html")


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


''' 
l ={
  "name" : "omarrrar",
  "age" : 19





}

for i in l:
  print(f"key is {i}  and value is {l[i]}")


  "name
  "age
'''