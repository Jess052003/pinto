from django.shortcuts import render
from django.http import *
from .db import *
from polls import *
from .file import *
# Create your views here.
def launch(request):
    write_file("notverified")
    if request.method == 'POST':
        user=request.POST.get('user')
        passw=request.POST.get('pass')
        print(user,passw)
        if verify(user,passw):
            write_file("verified")
            return HttpResponseRedirect("home")
    return render(request,"Login.html")

def home(request):
    if read_file():
        return render(request,'home.html')
    return HttpResponseRedirect("")

