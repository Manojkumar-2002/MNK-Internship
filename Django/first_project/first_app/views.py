from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html',{'name':'Manoj'})


def add_no(request):
    no1 = request.POST['no1']
    no2 = request.POST['no2']
    res = int(no1) + int(no2)
    print("request",request)
    return render(request,'result.html',{'res':res})
