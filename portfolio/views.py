from django.shortcuts import render
from .models import Message
from .form import MessageForm


# Create your views here.


#creating a view for the messages from the user
def messages(request):
    form = MessageForm(request.POST)
    if form.is_valid():
        form.save()
    context = {'form':form}
    return render(request,'index.html',context)
def thanks(request):
    return render(request,'thanks.html')
def home(request):
    return render(request,'index.html')