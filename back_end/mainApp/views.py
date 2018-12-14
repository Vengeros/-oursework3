from django.shortcuts import render
from django.core.exceptions import ValidationError
from mainApp.models import *
from django.contrib.auth.models import User
from django.contrib import auth
# from django.contrib.auth.decorators import login_required
#TODO:prefetch_related - for one-to-many

def index(request):
    # global user
    request.session["how_much_can_see"] = 14
    limit= request.session["how_much_can_see"]
    good_type_id = request.GET.get("type","")
    firm_name_id = request.GET.get("firm","")
    is_filter = request.GET.get("is_filter","")
    my_login = request.POST.get('my_login',"")
    # goods = Goods.objects.values('uniquecode').distinct()
    # if is_filter is not "":
    #     limit = 100
    if good_type_id is "" and firm_name_id is "" and is_filter is "":
        goods = Goods.objects.select_related('firmid','goodtypeid')[0:limit]
    elif good_type_id is not "":
        goods = Goods.objects.select_related('firmid','goodtypeid').filter(goodtypeid = good_type_id)#[0:limit]#better than all()
    elif firm_name_id is not "":
        goods = Goods.objects.select_related('firmid','goodtypeid').filter(firmid = firm_name_id)#[0:limit]#better than all()
    elif is_filter is not "":
        goods = my_site_filter(request)
    products_type = Goodstype.objects.all()
    firms_name = Firms.objects.all()
    if my_login is not "" :
        try:
            User.objects.create_user(
            username = request.POST.get('my_login_nik',''),
            first_name = request.POST.get('my_login_name',''),
            last_name = request.POST.get('my_login_surname',''),
            email = request.POST.get('my_login_email',''),
            password = request.POST.get('my_login_password','')
            )
        except:
            print("EROR")
        user = auth.authenticate(username=request.POST.get('my_login_nik',''), password=request.POST.get('my_login_password',''))
        if user is not None and user.is_active:
            auth.login(request, user)

    return render(request,'front_end/index.html',{'firms_name':firms_name,'products_type':products_type,'goods':goods,'help':'help/'})

def help_button(request):
    return render(request,'front_end/index.html',{'values':['Questions by tv-phone','(666) 666-66-66'],'help':'../'})

def my_site_filter(request):
    # TODO: do not forget set filtering from to price diapazone
    return Goods.objects.select_related('firmid','goodtypeid').filter(name__icontains =request.GET.get("good_name_by_regular",""))


def test_call():
    a = Test(testcol = 12,testcol1 = '55gjkkskdg')
    try:
        a.full_clean()
        a.save()
    except ValidationError as e:
        print("EROR")
        pass
