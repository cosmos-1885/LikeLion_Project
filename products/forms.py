from django import forms
from .models import Product

class RegisterForm(forms.Form):
    name = forms.CharField(
        error_messages={'required':"상품명을 입력하세요."},
        max_length = 32, label = "상품명"
    )
    target = forms.IntegerField(
        error_messages={'required':"목표 인원을 입력하세요"},
        label = "목표 인원"
    )
    price = forms.IntegerField(
        error_messages={'required' : "가격을 입력하세요."},
        label = "가격"
    )
    place = forms.CharField(
        error_messages={'required':"수령 장소를 입력하세요"},
        label = "수령 장소"
    )
    buy_link = forms.CharField(
        error_messages={'required':"구매 페이지를 입력하세요"},
        label = "구매 페이지"
    )
    description = forms.CharField(
        error_messages={'required':"상품 설명을 입력하세요"},
        label = "상품 설명"
    )
    product_image = forms.ImageField(
        error_messages={'required':"이미지를 등록하세요"},
        label = "이미지"
    )

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        target = cleaned_data.get('target')
        price = cleaned_data.get('price')
        place = cleaned_data.get('place')
        buy_link = cleaned_data.get('buy_link')
        description = cleaned_data.get('description')
        product_image = cleaned_data.get('product_image')

        if not (name and target and price and place and buy_link and description and product_image):
            self.add_error('name', "값이 없습니다.")
            self.add_error('target', "값이 없습니다.")
            self.add_error('price', "값이 없습니다.")
            self.add_error('place', "값이 없습니다.")
            self.add_error('buy_link', "값이 없습니다.")
            self.add_error('description', "값이 없습니다.")
            self.add_error('product_image', "값이 없습니다.")