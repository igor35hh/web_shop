from django.contrib import admin

from django.contrib.admin import ModelAdmin

from .models import Statistic
from django.shortcuts import render

from django.shortcuts import redirect

class StatisticModel(ModelAdmin):

    def view_on_site(self, obj):
        return 'https://example.com'
    
    def get_urls(self):
        from django.conf.urls import patterns, url
        
        urls = super(StatisticModel, self).get_urls()
        my_urls = patterns ('',
            url(r'^countstat/all/$', self.ReadStatAll),
        )
        return my_urls + urls

    def ReadStatAll(self, request):
        setstat = {}
        context = dict(
            self.admin_site.each_context(request),
            key=value,
        )
        return render(request, 'countstat/detail.html', context)
        #return redirect('admin/')


admin.site.register(Statistic, StatisticModel)

