from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('email',) # 주의사항 : 튜플 안에 ,를 써주어야 튜플로 인식 안쓰면 문자열로 인식

admin.site.register(User, UserAdmin)


# python manage.py createsuperuser (hc, 2510)