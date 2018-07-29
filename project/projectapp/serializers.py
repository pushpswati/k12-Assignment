from rest_framework import serializers
from projectapp.models import StudentEnroll
from projectapp.models import Course
from projectapp.models import StudentEnrollCourse

class StudentEnrollSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentEnroll
        fields=('created','username','password')


class CourseSerializer(serializers.ModelSerializer):
     class Meta:
         model=Course
         fields=('course_name','created')



class StudentEnrollCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentEnrollCourse
        fields=('studentenroll_id','course_id','course','created')
