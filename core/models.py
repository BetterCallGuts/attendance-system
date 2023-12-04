from django.db import models
import datetime
from django.utils.html  import mark_safe
from django.urls import reverse

class StudentCourseRel(models.Model):
  student = models.ForeignKey('Student',on_delete=models.CASCADE)
  course  = models.ForeignKey('Course', on_delete=models.CASCADE)
  attend    = models.TextField( null=True, blank=True)

  def __str__(self):
    return f"{self.student.name}"
  
  

class Days(models.Model):
  name = models.CharField(max_length=255)

  def __str__(self):
    return f"{self.name}"

class Level(models.Model):
  name = models.CharField(max_length=255)

  def __str__(self):
    return f"{self.name}"

try:
  i = Days.objects.all()
  days  = [
      "Monday", "Tuesday", "Wednesday", "Thursday",
      "Friday", "Saturday", "Sunday"
            ]
  if len(i) ==0:
    for s in days:
      x = Days.objects.create(name=s)

      x.save()
  
except:
  pass

try:
  i = Level.objects.all()
  lvls  = [
    "LEVEL 1", "LEVEL 2", 
    "LEVEL 3", "LEVEL 4", 
    "LEVEL 5", 
            ]
  if len(i) ==0:
    for s in lvls:
      x = Level.objects.create(name=s)

      x.save()
  
except:
  pass

class Instructor(models.Model):
  
  name    = models.CharField(max_length=255, verbose_name="Intructor name")
  ins_course  = models.ManyToManyField('core.Course', blank=True, )

  def __str__(self):
    return f"{self.name}"


class  Course(models.Model):


  
  li = (
    ("1", "First term"),
    ("2", "Second term"),
  )



  name          = models.CharField(max_length=255, verbose_name="Course name")
  coden         = models.CharField(max_length=255,   verbose_name="Code name", default="palce holder")
  inst          = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True, blank=True)
  Term          = models.CharField(choices=li, max_length=255, blank=True, null=True)
  starting_date = models.DateField(default=datetime.datetime.now, blank=True, null=True, editable=False)
  ending_date   = models.DateField(default=datetime.datetime.now, blank=True, null=True, editable=False)
  Days          = models.ManyToManyField(Days, blank=True)
  level         = models.ForeignKey(Level, null=True, blank=True, on_delete=models.SET_NULL)
  faculty       = models.ForeignKey('core.Faculty', null=True, blank=True, on_delete=models.SET_NULL)
  
  # 
  def __str__(self):
    return f"{self.coden}"

  # 
  def save(self):
    super().save()
    cur_year = datetime.datetime.now().year
    if self.Term == "1":

      self.starting_date = f"{cur_year}-10-01"
      self.ending_date   = f"{cur_year  +1}-1-30"

    if self.Term == "2":

      cur_month = datetime.datetime.now().month
      if cur_month  >= 8 :
        cur_year += 1



      self.starting_date = f"{cur_year}-2-15"
      self.ending_date   = f"{cur_year}-5-30"





    super().save()
  
  # 
  def save_model(self,  request, obj, form, changed):
    super().save_model(request, obj, form, changed)
    cur_year = datetime.datetime.now().year
    if self.Term == "1":

      self.starting_date = f"{cur_year}-10-01"
      self.ending_date   = f"{cur_year  +1}-1-30"

    if self.Term == "2":

      cur_month = datetime.datetime.now().month
      if cur_month  >= 8 :
        cur_year += 1



      self.starting_date = f"{cur_year}-2-15"
      self.ending_date   = f"{cur_year}-5-30"


      super().save_model(request, obj, form, changed)
  # 
  
  
  


  


class Faculty(models.Model):
  name = models.CharField(max_length=255,)

  def __str__(self):
    
    return f'{self.name}'

class Student(models.Model):

  #  choices
  
    
  name      = models.CharField(max_length=255, verbose_name="Student name")
  aca_id    = models.CharField(max_length=255, verbose_name="ID", blank=True, null=True, )
  aca_em    = models.EmailField(verbose_name="Student email", blank=True, null=True)
  password  = models.CharField(
    blank=True, null=True,
    verbose_name="Student password",
    max_length=255,
    help_text="Will be id if blank"
    )
  faculty   = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True, blank=True)
  Date_ofj  = models.DateField(default=datetime.datetime.now, blank=True, null=True, verbose_name="Date of join")
  levels    = models.ForeignKey(Level, blank=True, null=True, on_delete=models.SET_NULL)

  
  def save(self):
    super().save()
    if self.password == None:
      self.password = self.aca_id
    
    courses  = Course.objects.filter(level=self.levels, faculty=self.faculty)
    month    = datetime.datetime.now().month

    if month >= 6:
      courses.filter(Term="1")
    
    else:
      courses.filter(Term="2")
    

    for i in courses:
      the_c = StudentCourseRel.objects.filter(
        student=self,
        course=i
        )
      if the_c.exists():
        continue
      x     = StudentCourseRel.objects.create(
        student=self,
        course=i,
        
        )
      x.save()

    
    
    
    super().save()
  
  
  def save_model(self,  request, obj, form, changed):
    super().save_model( request, obj, form, changed)
    if self.password == None:
      self.password = self.aca_id
    
    
    courses  = Course.objects.filter(level=self.levels, faculty=self.faculty)
    month    = datetime.datetime.now().month

    if month >= 6:
      courses.filter(Term="1")
    
    else:
      courses.filter(Term="2")
    

    for i in courses:
      the_c = StudentCourseRel.objects.filter(
        student=self,
        course=i
        )
      if the_c.exists():
        continue
      x     = StudentCourseRel.objects.create(
        student=self,
        course=i,
        
        )
      x.save()

    
    super().save_model( request, obj, form, changed)
  
  def __str__(self):
    return f"{self.name}"
  
  def Attnder(self):
    my_ = StudentCourseRel.objects.filter(student=self)

    div = '''
    
    <div>
    
          '''
    
    for i in my_:

      try:
        
        days = i.attend.split(',')
      except:
        days = None
      

        days_html = f"""
      <hr>
      <h2>
        {i.course.name}
      </h2> 
      <a 
        href='{reverse("attend",args=(i.pk,))}' 
        target='popup'
        >
          Edit it
        </a>
        <br>
        You havn't set it up yet  
        <hr
        > <br>"""
     
      

      if days is not None:
        the_cours_name = i.course.name
        days_html = f''' 
        
        <hr>
        <h2>
        {the_cours_name}
        </h2>
        <a 
        href='{reverse("attend",args=(i.pk,))}' 
        target='popup'
        >
          Edit it
        </a>
        '''
        for m in days:
          days_html += f"<p> {m}</p>"

        days_html += '<hr>'
        days_html = mark_safe(days_html)

      div += mark_safe(days_html)
    
  
    div += mark_safe("</div>")
    div += mark_safe( ''' 
          <script>
    links = document.querySelectorAll('a[target=popup]');
    
    for ( link of links) {
        link.addEventListener('click', ()=>{
            window.open(link.getAttribute("href"), 'popup',' width=600,height=600'); return false; 
        }) 
    }
          </script>''')
    return mark_safe(div)
  
  
