from django.http import HttpResponse
from django.shortcuts import render
from .models import Change, team


# Create your views here.
#def home(request):
    #return render(request,"HOME.html")
#def about(request):
    #return render(request,"ABOUT.html")
#def contact(request):
    #return HttpResponse("Please contact for more details")
#def details(request):
    #return HttpResponse("details are given in the description link")
#def thanks(request):
    #return HttpResponse("THANKYOU VERY MUCH")
#def input(request):
    #return render(request,'input.html')
#def result(request):
   # x=int(request.GET['num1'])
    #y=int(request.GET['num2'])
    #ad=x+y
    #sub=x-y
    #mul=x*y
    #div=x/y
    #return render(request,'result.html',{'addition':ad,'subtraction':sub,'product':mul,'division':div})
def webpage(request):
    #obj=Change.objects.all()
    #return render(request,'index.html',{'result':obj})
    obj1 =team.objects.all()
    return render(request, 'index.html', {'new': obj1})