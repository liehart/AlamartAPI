from django.contrib import admin

# Register your models here.
from django.db.models import Count

from AlamartAPI.items.forms import ItemForm
from AlamartAPI.items.models import Item, Maker


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['maker', 'name', 'price', 'sold', 'stock', 'is_available', ]
    list_display_links = ['name']
    form = ItemForm


@admin.register(Maker)
class MakerAdmin(admin.ModelAdmin):
    list_display = ['name']
