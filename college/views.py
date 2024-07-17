from django.shortcuts import render
from django.http import HttpResponse

def handler404(request,exception):
    return render(request,'backend/404.html',status=404)