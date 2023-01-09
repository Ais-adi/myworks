from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy

from mytodoapp.models import task
from. forms import Todoform
from django.views.generic import ListView, UpdateView,DeleteView
from django.views.generic.detail import DetailView





# def demo(request):
#     Task1 = task.objects.all()
#     if request.method=='POST':
#         name=request.POST.get('task')
#         priority=request.POST.get('priority')
#         date=request.POST.get('date')
#         Task=task(name=name,priority=priority,date=date)
#         Task.save()
#     return render(request,'form.html',{'task':Task1})
# def details(request):
#
#     return render(request,'details.html',)
def delete(request,taskid):
    Task2=task.objects.get(id=taskid)
    if request.method=='POST':
        Task2.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,id):
    Task3=task.objects.get(id=id)
    f=Todoform(request.POST or None, instance=Task3)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'Task3':Task3})


class Taskview(ListView):
    model = task
    template_name = 'form.html'
    context_object_name = 'task'
class TaskDetailView(DetailView):
    model=task
    template_name = 'details.html'
    context_object_name = 'Task'
class TaskUpdateView(UpdateView):
    model=task
    template_name = 'update.html'
    context_object_name = 'totask'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})
class TaskDeleteView(DeleteView):
    model = task
    template_name = 'delete.html'
    success_url=reverse_lazy('cbvhome')
