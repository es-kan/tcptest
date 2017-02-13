from django.contrib import admin
from models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'date_added')
    ordering = ('-date_added', 'price')

# Register your models here.
admin.site.register(Item, ItemAdmin)
