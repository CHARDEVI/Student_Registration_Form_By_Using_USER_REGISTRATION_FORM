from django.shortcuts import render
from django.http import HttpResponse
from cherry.models import *
from cherry.forms import *
# Create your views here.
def registerall(request):
    d={'TFO':TopicForm(),'WFO':WebpageForm(),'AFO':AccessRecordForm()}
    if request.method=='POST':
        TFO=TopicForm(request.POST)
        WFO=WebpageForm(request.POST)
        AFO=AccessRecordForm(request.POST)
        if TFO.is_valid() and WFO.is_valid() and AFO.is_valid():
            STFO=TFO.save()
            NSWO=WFO.save(commit=False)
            NSWO.topic_name=STFO
            NSWO.save()

            NSAO=AFO.save(commit=False)
            NSAO.name=NSWO
            NSAO.save()
            return HttpResponse('Registration is Done Successfully')
        else:
            return HttpResponse('Data is Invalid')



    return render(request,'registerall.html',d)