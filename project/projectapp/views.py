from projectapp.models import StudentEnroll,Courses,StudentEnrollCourse
from projectapp.serializers import StudentEnrollSerializer,CourseSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from rest_framework import generics,permissions
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class AddUser(APIView):
     """
     This view for add new User
     Send username , password and slected course for add new usre
     """
     def post(self, request, format=None):
         password = request.data['password']
         username = request.data['username']
         email = request.data['email']
         course_id=request.data['course_id']

         # Before adding the USer check Course limit for the Student
         student_course_obj = StudentEnrollCourse.objects.filter(course_id=course_id)
         student_course_count = len(student_course_obj)  # Count exixting number of student_course
         if student_course_count < 5:  # Enroll  Course to student if student_course_count less then 5
             user_obj = StudentEnroll.objects.create(username=username, password=password, useremail=email)
             # Getting Course model object using course_id
             course_obj = Courses.objects.get(id=course_id)

             if course_obj:  # check course_id is availabel then insert course_id and student_id in StudentEnrollCourse
                 student_id = user_obj.id  # get student_id form  StudentEnroll model
                 course_id = course_obj.id  # get course_id from Course model
                 # Befor enroll Course check limit of the course
                 studentenrollcourse = StudentEnrollCourse.objects.create(studentenroll_id=student_id,
                                                                      course_id=course_id)
                 msg_response = "Enrollment done Successfully"

                 # Custom response dict
                 response_dict={"student_id":str(student_id),
                                "course_id":str(course_id),
                                "response":msg_response}

                 # Final rensponse to send
                 RESPONSE={"success":True,
                           "response":response_dict}

                 return Response(RESPONSE, status=status.HTTP_201_CREATED)

         else:
             msg_response = "This Course id alraeady exceed limit of students, Please select"

             # Final rensponse to send
             RESPONSE = {"success": True,
                         "response": msg_response}
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserList(APIView):
    """
    This view for add new course
    Send username , password and slected course for add new user
    """

    def get(self, request, format=None):
        user_obj = StudentEnroll.objects.all()
        serializer = StudentEnrollSerializer(user_obj,many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class AddCourses(APIView):
    """
    This view for add new course
    Send username , password and slected course for add new user
    """

    def post(self, request, format=None):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CoursesList(APIView):
    """
    This view for add new course
    Send username , password and slected course for add new user
    """

    def get(self, request, format=None):
        course_obj = Courses.objects.all()
        serializer = CourseSerializer(course_obj,many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)



class Login(APIView):
     
      # This is login api
      def post(self,request, format=None):
          print("Checkpoint 1")
          serializer = StudentEnrollSerializer(data=request.data)
          username = request.data['username']
          print("Checkpoint 2 l",username)
          password = request.data['password']
          print("Checkpoint 3 password==",password)

          # Write your code for check email sssst in db
          try:
              user = StudentEnroll.objects.get(username=username)
              
              if user is not None:
                  if (user.password==password):
                      print("Student Registration successfull: ",)

                      return Response({"sucess":"true","message":"Loging successfull"}, status=status.HTTP_200_OK)
                  else:
                      return Response({"sucess":"false","message":"Login not successfull"}, status=status.HTTP_400_BAD_REQUEST)

              else:
                  return Response({"sucess":"false","message":"Login not successfull"}, status=status.HTTP_400_BAD_REQUEST)

          except:
              return Response({"sucess":"false","message":"username does not exist"}, status=status.HTTP_400_BAD_REQUEST)





