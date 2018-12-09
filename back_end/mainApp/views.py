from django.shortcuts import render
from django.core.exceptions import ValidationError
from mainApp.models import *

#TODO:prefetch_related - for one-to-many

def index(request):
    limit=12
    good_type_id = request.GET.get("type","")
    firm_name_id = request.GET.get("firm","")
    goods = Goods.objects.values('uniquecode').distinct()

    if good_type_id is "":
        goods = Goods.objects.select_related('firmid','goodtypeid')[0:limit]
    else:
        goods = Goods.objects.select_related('firmid','goodtypeid').filter(goodtypeid=good_type_id)#[0:limit]#better than all()

    if firm_name_id is "":
        goods = Goods.objects.select_related('firmid','goodtypeid')[0:limit]
    else:
        goods = Goods.objects.select_related('firmid','goodtypeid').filter(firmid=firm_name_id)#[0:limit]#better than all()
    products_type = Goodstype.objects.all()
    firms_name = Firms.objects.all()
    return render(request,'front_end/index.html',{'firms_name':firms_name,'products_type':products_type,'goods':goods,'help':'help/'})

def help_button(request):
    return render(request,'front_end/index.html',{'values':['Questions by tv-phone','(666) 666-66-66'],'help':'../'})

def display_one_good_type():
    pass


def test_call():
    a = Test(testcol = 101,testcol1 = '55')
    try:
        a.full_clean()
        a.save()
    except ValidationError as e:
        print("EROR")
        pass
