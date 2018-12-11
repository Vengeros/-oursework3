from django import forms
from mainApp.models import Clients

class ClientForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('email','password','name', 'surname','age','creditcard')
