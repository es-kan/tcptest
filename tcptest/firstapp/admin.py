from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from models import Item, Seller

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'seller', 'date_added')
    ordering = ('seller',)

class SellerInline(admin.StackedInline):
    model = Seller

class UserAdmin(BaseUserAdmin):
    inlines = (SellerInline, )

# Register your models here.
admin.site.register(Item, ItemAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
