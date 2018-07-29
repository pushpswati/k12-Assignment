from django.conf.urls import url
from projectapp import views
urlpatterns=[
    # API for adding courses
    url(r'^addcourse$', views.AddCourses.as_view(), name='AddCourses'),
    # API for adding user and enroll course
    url(r'^adduser$',views.AddUser.as_view(),name='AddUser'),
    ## API for List of all registered user or student
    url(r'^userlist', views.UserList.as_view(), name='UserList'),
    # API for list of all available course
    url(r'^courselist', views.CoursesList.as_view(), name='CoursesList'),
    # API for login user via username and password
    url(r'^login$',views.Login.as_view(),name='Login'),

]

