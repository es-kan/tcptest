from django.contrib import admin
from models import Item, Seller

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'seller', 'date_added')
    ordering = ('seller',)

# Register your models here.
admin.site.register(Item, ItemAdmin)
admin.site.register(Seller)
