from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ShopUser
from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'available']
    list_filter = ['available', 'category']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

class ShopUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'phone', 'balance')
    fieldsets = UserAdmin.fieldsets + (
        ('Дополнительная информация', {'fields': ('phone', 'address', 'balance')}),
    )

admin.site.register(ShopUser, ShopUserAdmin)