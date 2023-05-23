from django import forms
from cherry.models import *


class TopicForm(forms.ModelForm):
    class Meta():
        model=Topic
        fields='__all__'


class WebpageForm(forms.ModelForm):
    class Meta():
        model=Webpage
        fields=['name','email']


class AccessRecordForm(forms.ModelForm):
    class Meta():
        model=AccessRecord
        fields=['author','date']