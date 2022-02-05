from django.contrib import admin
from .models import  *

@admin.register(Product)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name','price']


admin.site.register(Consumer)
admin.site.register(Order)
admin.site.register(Payment)

