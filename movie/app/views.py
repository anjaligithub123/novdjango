from django.shortcuts import render
from app.models import Movie
from app.forms import movieform
def home(request):
   m=Movie.objects.all()
   return render(request, 'home.html', {'m': m})


def detail(request,n):
   m = Movie.objects.get(id=n)
   return render(request, 'detail.html', {'m': m})
def addmovie(request):
    if(request.method=="POST"):
         form=movieform(request.POST,request.FILES)
         if form.is_valid():
            form.save()
            return home(request)

    form=movieform()
    return render(request, 'add.html', {'form': form})
def update(request,n):
    m = Movie.objects.get(id=n)
    if (request.method == "POST"):
        form = movieform(request.POST, request.FILES,instance=m)
        if form.is_valid():
            form.save()
            return home(request)

    form = movieform(instance=m)
    return render(request, 'add.html', {'form': form})
def delete(request,n):
    m = Movie.objects.get(id=n)
    m.delete()
    return home(request)