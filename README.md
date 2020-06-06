
  assignment
---------



<p align="center">
<a href=""><img src="https://img.shields.io/github/issues/tokyodevs/django3scaffold" alt="Build Status"></a>
<a href=""><img src="https://img.shields.io/github/forks/tokyodevs/django3scaffold" alt="Build Status"></a>
<a href=""><img src="https://img.shields.io/github/stars/tokyodevs/django3scaffold" alt="Build Status"></a>
<a href=""><img src="https://img.shields.io/github/license/tokyodevs/django3scaffold" alt="Build Status"></a>
<a href="https://img.shields.io/twitter/url?url=https%3A%2F%2Fgithub.com%2Ftokyodevs%2Fdjango3scaffold"><img src="https://img.shields.io/twitter/url?url=https%3A%2F%2Fgithub.com%2Ftokyodevs%2Fdjango3scaffold" alt="Build Status"></a>
</p>

Overview
---------
blah blah blah 


## clone 
```
git clone https://github.com/tokyodevs/-assignment-.git && cd -assignment-
```


## install packages from pip (python3)

```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt 
```


#### another version install pks brew


## migrate 
```
python manage.py makemigrations
python manage.py migrate
```

## test 
```
python manage.py test
```



## usage 

### create super user
```
python manage.py createsuperuser
```
output: 
```
Username: root
Error: That username is already taken.
Username: admin
Email address: admin@admin.admin
Password: 
Password (again): 
The password is too similar to the username.
This password is too short. It must contain at least 8 characters.
This password is too common.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.

```

## run  
```
python manage.py runserver 0.0.0.0:9000
```

### do a login and get jwt 

```
curl -X "POST" "http://localhost:9000/api/token/" \
     -H 'Content-Type: application/json; charset=utf-8' \
     -d $'{
  "username": "admin",
  "password": "admin"
}'

```

### get the access token from previous command and request a list 
```
curl "http://localhost:9000/api/news" \
     -H 'Authorization: Bearer YOUR_JWT' \
     -H 'Content-Type: application/json; charset=utf-8'
```

### do a search request
```
curl "http://localhost:9000/api/news?q=trump" \
     -H 'Authorization: Bearer YOUR_JWT' \
     -H 'Content-Type: application/json; charset=utf-8'
```





## docs (swagger)
```
http://localhost:9000/
```

## TODO
- [ ] another branch or maybe another tag for using background tasks or maybe celery 
- [ ] write to work/test like https://github.com/tokyodevs/simple_django/blob/master/lesgo.sh 

- [ ] use https://pypi.org/project/django3scaffold/ for no reason

- [x] do the task
