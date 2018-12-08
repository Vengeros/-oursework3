from django.shortcuts import render
from django.core.exceptions import ValidationError
from mainApp.models import Test


def index(request):
    return render(request,'front_end/index.html',{'help':'help/'})

def help_button(request):
    return render(request,'front_end/index.html',{'values':['Questions by tv-phone','(666) 666-66-66'],'help':'../'})

def test_call():
    a = Test(testcol = 101,testcol1 = '55')
    try:
        a.full_clean()
        a.save()
    except ValidationError as e:
        pass
