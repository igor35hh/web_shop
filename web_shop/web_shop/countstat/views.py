from django.shortcuts import render

import datetime
import os
from shop.models import Profuct as Product
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def ReadStat(request, category_id):
    setstat = {}
    return render(request, 'countstat/detail.html', {'setstat': setstat})

@staff_member_required
def ReadStatAll(request):
    setstat = {}
    return render(request, 'countstat/detail.html', {'setstat': setstat})

def readLog():
    DirPostLog = "static/{}.log".format(datetime.date.today())
    fopen = open(DirPostLog,"r")
    for line in ff.readlines():
        sline = linefile.split(r':')
        #cat = sline[0]
        #product = get_object_or_404(Product, id=sline[1])
        #product.name
        pass
        #print(line['data'])
    #listForRender = []
    #listForRender.append('a')
    fopen.close
    pass
