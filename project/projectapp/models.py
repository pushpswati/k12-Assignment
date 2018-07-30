from django.db import models

class StudentEnroll(models.Model):
      created = models.DateTimeField(auto_now_add=True)
      username = models.CharField(max_length=100, blank=True, default='')
      useremail=models.EmailField(null=True,blank=True)
      password = models.CharField(max_length=10,blank=True,default='')
      

      class Meta:
          ordering = ('created',)

class Courses(models.Model):
      course_name = models.CharField(max_length=30,blank=True,default='')
      created = models.DateTimeField(auto_now_add=True)
      class Meta:
          ordering = ('created',)


class StudentEnrollCourse(models.Model):
      studentenroll_id = models.CharField(max_length=100)
      course_id = models.CharField(max_length=100)
      created = models.DateTimeField(auto_now_add=True)


      class Meta:
          ordering = ('created',)





