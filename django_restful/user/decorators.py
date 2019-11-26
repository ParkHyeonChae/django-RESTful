from django.shortcuts import redirect
from .models import User

def login_required(function): # 로그인 안할시 order page 접근 불가
    def wrap(request, *args, **kwargs):
        user = request.session.get('user')

        if user is None or not user:
            return redirect('/login')
        return function(request, *args, **kwargs)

    return wrap

def admin_required(function): # 관리자 아닐시 product create 불가
    def wrap(request, *args, **kwargs):
        user = request.session.get('user')

        if user is None or not user:
            return redirect('/login')

        user = User.objects.get(email=user)
        if user.level != 'admin':
            return redirect('/')

        return function(request, *args, **kwargs)

    return wrap