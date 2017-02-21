from django.contrib import admin

from .models import Category, Profuct as Product

from django.utils.html import format_html
from django.core.urlresolvers import reverse

from django.http import HttpResponse, HttpResponseRedirect

def ShowStatistic(modeladmin, request, queryset):
    #response = HttpResponse(content_type='text/html')
    #response.write("<p>Here's the text of the Web page.</p>")
    #return response
    category_id = str(queryset[:1][0])
    #print(category_id)
    category_id='1'
    return HttpResponseRedirect(reverse('countstat:ReadStat', args=[category_id]))
    
ShowStatistic.short_description = 'Show statistic per this day'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}
    actions = [ShowStatistic]
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
