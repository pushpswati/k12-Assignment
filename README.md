# k12-Assignment
# Installation and setup
```
pip install django==1.11.0
pip install djangorestframework
```
# Setup DB
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
# API Documentaion

## Add User API
http://0.0.0.0:8001/adduser
```
payload={"username":"",
    "password":"",
    "email":"",
    "course_id":3}
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
