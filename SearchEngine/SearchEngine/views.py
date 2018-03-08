from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def mainpage(request):
    return render(request,'search_engine.html')
	
def mai(request):
    return HttpResponse("<h1>heyyy</h1>")

def see(request):
    return render(request,'search_engine.html')