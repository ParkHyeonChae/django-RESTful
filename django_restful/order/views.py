from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .forms import RegisterForm

class OrderCreate(FormView):
    form_class = RegisterForm
    success_url = '/product/'

    def form_invalid(self, form):
        return redirect('/product/' + str(form.product))

    def get_form_kwargs(self, **kwargs): # form을 생성할때 어떤 인자값을 전달할지 결정
        kw = super().get_form_kwargs(**kwargs) #  기존 자동으로 생성되는 인자값에 request도 포함시켜 생성
        kw.update({
            'request': self.request
        })
        return kw