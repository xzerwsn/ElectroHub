from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ShopUser

class ShopUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'phone', 'balance')
    fieldsets = UserAdmin.fieldsets + (
        ('Дополнительная информация', {'fields': ('phone', 'address', 'balance')}),
    )

admin.site.register(ShopUser, ShopUserAdmin)