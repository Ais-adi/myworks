from django import forms

from mytodoapp.models import task


class Todoform(forms.ModelForm):
    class Meta:
        model=task
        fields=['name','priority','date']
