from django import forms
from todoapp.models import todoModel

class todoForm(forms.ModelForm):
    class Meta:
        model = todoModel
        fields = "__all__"