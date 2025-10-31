from django.shortcuts import render
from django.http  import HttpResponse
from app.models import *
# Create your views here.
def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        TTO=Topic.objects.get_or_create(topic_name=tn)
        if TTO[1]:
            return HttpResponse('topic is created')
        else:
            return HttpResponse('topic is alredy exit')
    return render(request,'insert_topic.html')
def display_topic(request):
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}
    return render(request,'display_topic.html',d)


def insert_webpage(request):
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}
    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get(topic_name=tn)
        n=request.POST['n']
        url=request.POST['url']
        TWO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=url)
        if TWO[1]:
            return HttpResponse('webpage is created')
        else:
            return HttpResponse('webpage is alredy exit')
    return render(request,'insert_webpage.html',d)



def display_webpage(request):
    QLWO=Webpage.objects.all()
    d={'QLWO':QLWO}
    return render(request,'display_webpage.html',d)


def insert_accessrecord(request):
    QLWO=Webpage.objects.all()
    d={'QLWO':QLWO}
    if request.method=='POST':
        
        n=request.POST['n']
        NO=Webpage.objects.get(name=n)
        a=request.POST['a']
        date=request.POST['date']
        TARO=AccessRecord.objects.get_or_create(name=NO,author=a,date=date)
        if TARO[1]:
            return HttpResponse('accessrecord is created')
        else:
            return HttpResponse('accessrecord is alredy exit')
    return render(request,'insert_accessrecord.html',d)
def display_accessrecord(request):
    QLAO=AccessRecord.objects.all()
    d={'QLAO':QLAO}
    return render(request,'display_accessrecord.html',d)

