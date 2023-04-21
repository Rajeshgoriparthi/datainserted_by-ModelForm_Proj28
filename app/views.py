from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.

def topic_form(request):
    TF=TopicForm()
    d={'TF':TF}
    if request.method=='POST':
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('Data inserted successfully')
    return render(request,'topic_form.html',d)


def webpage_form(request):
    WF=WebpageForm()
    d1={'WF':WF}
    if request.method=='POST':
        WFD=WebpageForm(request.POST)
        if WFD.is_valid():
            WFD.save()
            return HttpResponse('Webpage data inserted successfully')
    return render(request,'webpage_form.html',d1)