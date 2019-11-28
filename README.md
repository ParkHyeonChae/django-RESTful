# django-RESTful
django DRF 사용 RESTful API 프로젝트

### 1. 기본 개발환경, 프로젝트 설정
```
가상환경 설정
virtualenv django_env
django_env/Scripts/activate
```
```
django 설치
pip install django
```
```
Project, App 생성
django-admin startproject django_restful
cd django_restful
django-admin startapp user
django-admin startapp produt
django-admin startapp order
```
### 2. Model 설정
```
각 APP의 model class 생성 후
1. settings에 app 등록
2. python manage.py makemigrations
3. python manage.py migrate
```
### 3. Admin 구성 후 관리자 계정 생성
```
python manage.py createsuperuser
```

### 4. DRF 설치
```
pip install djangorestframework
INSTALLED_APPS 'rest_framework' 추가
```