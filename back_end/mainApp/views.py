from django.shortcuts import render

def index(request):
    return render(request,'front_end/index.html',{'help':'help/'})

def help_button(request):
    return render(request,'front_end/index.html',{'values':['Questions by tv-phone','(666) 666-66-66'],'help':'../'})
