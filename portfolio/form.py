from django import forms
from .models import Message

#creating a form

class MessageForm(forms.ModelForm):
    #creating a meta class
    class Meta:
        #specify the model
        model = Message
        #specify the fields to be used
        fields = '__all__'