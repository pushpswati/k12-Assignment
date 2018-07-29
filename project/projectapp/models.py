from django.db import models

class StudentEnroll(models.Model):
      created = models.DateTimeField(auto_now_add=True)
      username = models.CharField(max_length=100, blank=True, default='')
      password = models.CharField(max_length=10,blank=True, default='')
      

      class Meta:
          ordering = ('created',)

class Course(models.Model):
      course_name = models.CharField(max_length=30)
      created = models.CharField(max_length=30)
    

      def __str__(self):
          return self.course_name

class StudentEnrollCourse(models.Model):
      studentenroll_id = models.CharField(max_length=100)
      course_id = models.CharField(max_length=100)
     # many to many relation
      
      created = models.DateTimeField(auto_now_add=True)

      def __str__(self):
          return self.created

      class Meta:
          ordering = ('created',)





