from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.generic import ListView
from .forms import RegisterForm
from .models import Order

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

class OrderList(ListView):
    template_name = 'order.html'
    context_object_name = 'order_list'

    # 사용자의 주문정보를 보기 위해 queryset 사용, 하지만 사용자 정보를 알기 session을 사용해야하기에, 그냥 get_queryset 함수를 오버리이딩
    def get_queryset(self, **kwargs):
        queryset = Order.objects.filter(user__email=self.request.session.get('user'))
        return queryset