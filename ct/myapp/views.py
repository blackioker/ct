from django.shortcuts import render
from .models import movie
from .get import get_message

# Create your views here.
from django.http import HttpResponse
def show(request):
    movies=get_message()
    if movie.objects.count()==0:
        for each in movies:
            addition = movie(mname=each['title'], actor=each['actor'])
            addition.save()

    data=movie.objects
    return render(request,'movie.html',{'data':data})