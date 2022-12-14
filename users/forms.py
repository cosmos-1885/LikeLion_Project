from email.headerregistry import Address
from django import forms
from .models import Users
from django.contrib.auth.hashers import check_password

class RegisterForm(forms.Form):
    email = forms.EmailField(
        error_messages={'required':"이메일을 입력하세요."},
        max_length=64, label = "이메일"
    )
    password = forms.CharField(
        error_messages={'required' : "비밀번호를 입력하세요"},
        widget = forms.PasswordInput, label = "비밀번호"
    )
    # re_password = forms.CharField(
    #     error_messages={'required' : "비밀번호를 입력하세요"},
    #     widget = forms.PasswordInput, label = "비밀번호 재입력"
    # )
    name = forms.CharField(
        error_messages={'required' : "이름을 입력하세요"},
        max_length=10, label = "이름"
    )
    phone = forms.CharField(
        error_messages={'required' : "휴대폰 번호를 입력하세요"},
        max_length=11, label = "휴대폰 번호"
    )
    address = forms.CharField(
        error_messages={'required' : "주소를 입력하세요"},
        max_length=150, label = "주소"
    )
    
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        # re_password = cleaned_data.get('re_password')
        name = cleaned_data.get('name')
        phone = cleaned_data.get('phone')
        address = cleaned_data.get('address')

        # if password and re_password:
        #     if password != re_password:
        #         self.add_error('password', '비밀번호가 서로 다릅니다.')

class LoginForm(forms.Form):
    email = forms.EmailField(
        error_messages={'required':'이메일을 입력하세요'},
        max_length=64, label = "이메일"
    )
    password = forms.CharField(
        error_messages = {'required' : "비밀번호를 입력하세요"},
        max_length = 128, label = "비밀번호", widget = forms.PasswordInput
    )
    
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        
        if email and password :
            try:
                user = Users.objects.get(email = email)
            except Users.DoesNotExist:
                self.add_error('email', "존재하지 않는 이메일입니다.")
                return
            
            if not check_password(password, user.password):
                self.add_error('password', '비밀번호가 일치하지 않습니다.')