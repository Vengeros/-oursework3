from django.urls import include, path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('help/',views.help_button,name='help'),
]
