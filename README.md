# k12-Assignment
# Installation and setup
pip install django==1.11.0
 #How TO RUN  Djangosingup
# How TO RUN  Djangosingup
python manage.py runserver
 # how to migrate the project
python manage.py migrate
 # how to migrations the project
python manage.py migrations

# API Documentaion

## Add User API
http://0.0.0.0:8001/adduser
```
payload={"username":"",
    "password":"",
    "email":""}
```
## Add Course API
http://0.0.0.0:8001/addcourse
```
payload={"course_name":""}
```
## list of all registred USer
http://0.0.0.0:8001/userlist
## List of all Registered courses
http://0.0.0.0:8001/courselist
## User Login API
http://0.0.0.0:8001/login
```
payload={"username":"",
    "password":"",
     }
```
