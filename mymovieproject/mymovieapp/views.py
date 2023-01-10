from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from mymovieapp.form import Movieform
from mymovieapp.models import Movie


def index(request):
    movie= Movie.objects.all()
    context={
        "movie_list": movie
     }
    return render(request,'index.html',context)
def detail(request,movie_id):
    movie=Movie.objects.get(id= movie_id)
    return render(request,'detail.html',{'movie':movie})
def add_movie(request):
    if request.method=="POST":
        name=request.POST.get('name', )
        des = request.POST.get('des', )
        year= request.POST.get('year', )
        pic = request.FILES['pic']
        movie=Movie(name=name,des=des,year=year,pic=pic)
        movie.save()
    return render(request, 'add.html')
def update(request,id):
    movie=Movie.objects.get(id=id)
    forms=Movieform(request.POST or None,request.FILES,instance=movie)
    if forms.is_valid():
        forms.save()
        return redirect('/')
    return render(request,'edit.html',{'forms':forms,'movie':movie})
def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')