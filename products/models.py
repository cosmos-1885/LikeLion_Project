from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 32, verbose_name="상품명")
    target = models.IntegerField(max_length = 11, verbose_name = "목표 인원", null = True)
    people = models.IntegerField(default = 0, max_length = 11, verbose_name = "참여 인원", null = True) 
    price = models.IntegerField(verbose_name = "상품가격")
    place = models.TextField(verbose_name = "수령 장소", null = True)
    buy_link = models.TextField(verbose_name = "구매 페이지", null = True)
    description = models.TextField(verbose_name="상품 설명")
    product_image = models.ImageField(upload_to = 'images/', blank = True, null = True)
    registered_date = models.DateTimeField(verbose_name="등록 시간", auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "products"
        verbose_name = "상품"
        verbose_name_plural = "상품"