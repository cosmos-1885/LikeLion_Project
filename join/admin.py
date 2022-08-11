from django.contrib import admin
from .models import Join

# Register your models here.

class JoinAdmin(admin.ModelAdmin):
    # list_display = ('user', 'product', 'quantity',)
    list_display = ('user', 'product',)

admin.site.register(Join, JoinAdmin)