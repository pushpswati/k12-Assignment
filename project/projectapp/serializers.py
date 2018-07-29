from rest_framework import serializers
from projectapp.models import StudentEnroll
from projectapp.models import Courses
from projectapp.models import StudentEnrollCourse

class StudentEnrollSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentEnroll
        fields=('id','created','username','password')


class CourseSerializer(serializers.ModelSerializer):
     class Meta:
         model=Courses
         fields=('id','course_name','created')



class StudentEnrollCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentEnrollCourse
        fields=('id','studentenroll_id','course_id','course','created')
