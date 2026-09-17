from django import forms

from new_app.models import Menu


class menuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['name','price','category','variety']