from django import forms
from .models import Join
from users.models import Users
from products.models import Product

class JoinForm(forms.Form):
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    product = forms.IntegerField(
        error_messages={'required':"상품을 입력하세요."},
        label = "상품", widget = forms.HiddenInput
    )

    def clean(self):
        cleaned_data = super().clean()
        product = cleaned_data.get('product')
        user = self.request.session.get('user')

        if not(product and user):
            self.add_error('product', "상품이 없습니다.")