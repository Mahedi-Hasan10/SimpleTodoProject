from django.shortcuts import render,redirect
from todoapp.forms import todoForm
from todoapp.models import todoModel
# Create your views here.
def home(request):
    formdata = todoModel.objects.all()
    if request.method == "POST":
        form = todoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("homepage")
    else:
        form = todoForm()
    return render(request,"todo.html",{'form':form,'formdata':formdata})
    
def delete_todo(request,id):
    todo = todoModel.objects.get(pk=id).delete()
    return redirect('homepage')