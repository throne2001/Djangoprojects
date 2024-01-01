from django.shortcuts import render
from filmapp.models import Filmapp
from filmapp.forms import filmform

# Create your views here.
def home(request):
    b=Filmapp.objects.all()
    return render(request, 'home.html', {'movie': b})
def addmovie(request):
    form=filmform()
    if(request.method=="POST"):
        form=filmform(request.POST,request.FILES)
        if(form.is_valid()):
           form.save()
           return home(request)
    return render(request,'editmovie.html',{'form':form})
def viewmovie(request,p):
    b=Filmapp.objects.get(id=p)
    return render(request,'viewmovie.html',{'movie':b})
def editmovie(request,p):
    b=Filmapp.objects.get(id=p)
    form=filmform(instance=b)
    if(request.method=="POST"):
        form=filmform(request.POST,request.FILES,instance=b)
        if(form.is_valid()):
            form.save()
            return home(request)
    return render(request,'editmovie.html',{'form':form})

def deletemovie(request,p):
    b=Filmapp.objects.get(id=p)
    b.delete()
    return home(request)

