from django import forms
from filmapp.models import Filmapp
class filmform(forms.ModelForm):
    class Meta:
        model=Filmapp
        fields='__all__'