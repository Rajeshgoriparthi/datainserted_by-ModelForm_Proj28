from django import forms
from app.models import *

class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'


class WebpageForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'
        #fields=['topic_name','name']
        #exclude=['email']
        labels={'name':'User Name'}
        widgets={'password':forms.PasswordInput,'adress':forms.Textarea,'gender':forms.RadioSelect}
