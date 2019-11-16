from django.db import models

# 회원 클래스
class User(models.Model):
    email = models.EmailField(verbose_name='이메일')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'django_user'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'



# 1. settings에 app 등록
# 2. python manage.py makemigrations
# 3. python manage.py migrate
