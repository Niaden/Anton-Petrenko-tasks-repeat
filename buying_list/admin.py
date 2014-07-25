from django.contrib import admin
from .models import Item

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
	fields = ['item_name','item_num','item_measure','item_date']
	list_filter = ['item_date']


admin.site.register(Item,ItemAdmin)
