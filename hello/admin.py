from django.contrib import admin
from hello.models import *

# Register your models here.

@admin.register(Property)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name','computer','display','keyboard','mouse','memory','status')
    search_fields = ('name', 'computer', 'display', 'keyboard', 'mouse', 'memory', 'status')
#
@admin.register(hardware)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('number','address','product_name','commodity_brand','unit_price','quantity','amount','tis','status','norc')
    search_fields = ('number','address','product_name','commodity_brand','unit_price','quantity','amount','tis','status','norc')
