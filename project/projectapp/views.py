from projectapp.models import StudentEnroll
from projectapp.serializers import StudentEnrollSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import generics,permissions
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class PostList(APIView):
 
    

     def post(self, request, format=None):
        serializer = StudentEnrollSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class Login(APIView):
     
      # This is login api
      def post(self,request, format=None):
          print("Checkpoint 1")
          serializer = StudentEnrollSerializer(data=request.data)
         
          password = request.data['password']
          print("Checkpoint 3 password==",password)

          # Write your code for check email sssst in db
          try:
              
              user = Post.objects.get(password=' ')
              print(user)
              if user is not None:
                  if user.password==password:
                      print("Login successfull: ",)

                      #token

                      return Response({"sucess":"true","message":"Loging successfull"}, status=status.HTTP_200_OK)
                  else:
                      return Response({"sucess":"false","message":"Login not successfull"}, status=status.HTTP_400_BAD_REQUEST)

          except:
                  return Response({"sucess":"false","message":"Login password not successfull"}, status=status.HTTP_400_BAD_REQUEST)

          
              


  




