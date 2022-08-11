from django.db import models

# Create your models here.

class Join(models.Model):
    user = models.ForeignKey('users.Users', verbose_name = "사용자", on_delete = models.CASCADE)
    product = models.ForeignKey('products.Product',verbose_name = "상품", on_delete = models.CASCADE)
    registered_date = models.DateTimeField(auto_now_add=True, verbose_name="등록시간")

    def __str__(self):
        return str(self.user) + ' ' + str(self.product)
    
    class Meta:
        db_table = "together"
        verbose_name = "주문"
        verbose_name_plural = "주문"