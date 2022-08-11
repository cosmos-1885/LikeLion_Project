from django.db import models

# Create your models here.
class Users(models.Model):
    # verbose_name: admin 페이지에서 사용자가 이용하기 쉽도록 모델 객체의 이름을 지정
    email = models.CharField(verbose_name = "이메일", max_length = 128)
    password = models.TextField(verbose_name = "비밀번호")
    name = models.TextField(verbose_name = "이름", null = True)
    phone = models.CharField(max_length = 11, verbose_name = "휴대폰 번호", null = True)
    address = models.TextField(verbose_name = "주소", null = True)
    registered_date = models.DateTimeField(auto_now_add=True, verbose_name="등록시간")
    
    # class가 admin 페이지에서 출력되는 형태를 정의
    def __str__(self):
        return self.email
    
    # Meta: ??
    class Meta:
        # db_table: 테이블명
        db_table = "users"
        verbose_name = "사용자"
        verbose_name_plural = "사용자"