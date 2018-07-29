from django.conf.urls import url
from projectapp import views
urlpatterns=[
url(r'^studentenrollmentapp$',views.PostList.as_view(),name='PostList'),
url(r'^login$',views.Login.as_view(),name='Login'),


]

