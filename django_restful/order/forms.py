from django import forms
from .models import Order
from product.models import Product
from user.models import User
from django.db import transaction # transaction : 일련의 동작을 하나의 동작으로 처리, 전체가 다 성공하면 성공, 하나라도 실패하면 롤백 (주문시 제고도 감소)

class RegisterForm(forms.Form):
    def __init__(self, request, *args, **kwargs): # request를 전달할 수 있게 생성자 함수 생성
        super().__init__(*args, **kwargs)
        self.request = request

    quantity = forms.IntegerField(
        error_messages={
            'required': '수량을 입력해주세요'
        },
        label='수량'
    )
    product = forms.IntegerField(
        error_messages={
            'required': '상품설명을 입력해주세요'
        }, label='상품설명', widget=forms.HiddenInput  
    )

    def clean(self):
        cleaned_data = super().clean()
        quantity = cleaned_data.get('quantity')
        product = cleaned_data.get('product')
        user = self.request.session.get('user')

        if quantity and product and user:
            with transaction.atomic():
                prod = Product.objects.get(pk=product)
                order = Order(
                    quantity=quantity,
                    product=prod,
                    user=User.objects.get(email=user)
                )
                order.save()
                prod.stock -=quantity
                prod.save()
        else:
            self.product = product
            self.add_error('quantity', '값이 없습니다.')
            self.add_error('product', '값이 없습니다.')

        # print(self.request.session) # 사용자 세션 접근