from django.shortcuts import render
from django.core.exceptions import ValidationError
from mainApp.models import *
# from django.contrib.auth.decorators import login_required
#TODO:prefetch_related - for one-to-many

def index(request):
    limit=12
    good_type_id = request.GET.get("type","")
    firm_name_id = request.GET.get("firm","")
    is_filter = request.GET.get("is_filter","")
    # goods = Goods.objects.values('uniquecode').distinct()
    # if is_filter is not "":
    #     limit = 100
    if good_type_id is "" and firm_name_id is "" and is_filter is "":
        goods = Goods.objects.select_related('firmid','goodtypeid')[0:limit]
    elif good_type_id is not "":
        goods = Goods.objects.select_related('firmid','goodtypeid').filter(goodtypeid=good_type_id)#[0:limit]#better than all()
    elif firm_name_id is not "":
        goods = Goods.objects.select_related('firmid','goodtypeid').filter(firmid=firm_name_id)#[0:limit]#better than all()
    elif is_filter is not "":
        goods = my_site_filter(request)
    products_type = Goodstype.objects.all()
    firms_name = Firms.objects.all()
    return render(request,'front_end/index.html',{'firms_name':firms_name,'products_type':products_type,'goods':goods,'help':'help/'})

def help_button(request):
    return render(request,'front_end/index.html',{'values':['Questions by tv-phone','(666) 666-66-66'],'help':'../'})

def my_site_filter(request):
    return Goods.objects.select_related('firmid','goodtypeid').filter(name__icontains =request.GET.get("good_name_by_regular",""),price__lte = 900 ).filter(price__gte = 300)


def test_call():
    a = Test(testcol = 101,testcol1 = '55')
    try:
        a.full_clean()
        a.save()
    except ValidationError as e:
        print("EROR")
        pass
