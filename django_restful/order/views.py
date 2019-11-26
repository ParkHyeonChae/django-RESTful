from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from user.decorators import login_required
from .forms import RegisterForm
from .models import Order
from django.db import transaction # transaction : 일련의 동작을 하나의 동작으로 처리, 전체가 다 성공하면 성공, 하나라도 실패하면 롤백 (주문시 제고도 감소)
from product.models import Product
from user.models import User

@method_decorator(login_required, name='dispatch')
class OrderCreate(FormView):
    form_class = RegisterForm
    success_url = '/product/'
    
    def form_valid(self, form):
        with transaction.atomic():
            prod = Product.objects.get(pk=form.data.get('product'))
            order = Order(
                quantity=form.data.get('quantity'),
                product=prod,
                user=User.objects.get(email=self.request.session.get('user'))
            )
            order.save()
            prod.stock -= int(form.data.get('quantity'))
            prod.save()
        
        return super().form_valid(form)

    def form_invalid(self, form):
        return redirect('/product/' + str(form.data.get('product')))

    def get_form_kwargs(self, **kwargs): # form을 생성할때 어떤 인자값을 전달할지 결정
        kw = super().get_form_kwargs(**kwargs) #  기존 자동으로 생성되는 인자값에 request도 포함시켜 생성
        kw.update({
            'request': self.request
        })
        return kw

@method_decorator(login_required, name='dispatch')
class OrderList(ListView):
    template_name = 'order.html'
    context_object_name = 'order_list'

    # 사용자의 주문정보를 보기 위해 queryset 사용, 하지만 사용자 정보를 알기 session을 사용해야하기에, 그냥 get_queryset 함수를 오버리이딩
    def get_queryset(self, **kwargs):
        queryset = Order.objects.filter(user__email=self.request.session.get('user'))
        return queryset