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
def register(request):
    
    return render(request,'reg.html')
        
"""
 <div class="input-name">
                <label class="form-text">Email :</label>
                <input type="text" name="email" id="email" class="input-info" >
                <label class="form-text">Phone :</label>
                <input type="text" name="phone" id="phone" class="input-info">
                <label class="form-text">DOB :</label>
                <input type="text" name="dob" id="dob" class="input-info">
            </div>

            <div class="input-name">
                <label class="form-text">Gender :</label>
                <label class="form-text">Male</label>
                <input type="radio" name="male" id="gender">
                <label class="form-text">Female</label>
                <input type="radio" name="female" id="gender">
            </div>

            <div class="input-name">
                <label class="form-text">Address :</label>
                <input type="text" name="Address" id="address" class="input-info">
            </div>

            <div class="input-name">
                <label class="form-text">Create password:</label>
                <input type="text" name="crpass" id="create_pass" class="input-info">
                <label class="form-text">Confirm password :</label>
                <input type="text" name="cnpass" id="confirm_pass" class="input-info" >
            </div>
            <button type="submit"id="register" class="btn">Register</button>
            <button type="reset" id="cancel" class="btn">Cancel</button>

"""