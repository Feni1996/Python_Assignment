from django import forms
from . models import Person

class Person_Form(forms.ModelForm):
    class Meta:
        model=Person
        fields = "__all__"
