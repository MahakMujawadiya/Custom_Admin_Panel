from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User                      #to create user
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from app1.models import Person
from django.forms.models import model_to_dict
import re
from django.contrib.auth.hashers import make_password,check_password

# Create your views here.


def signuppage(request):
    r = re.compile(r'[a-zA-Z]+') 
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        phone = request.POST.get("phone")
        pincode = request.POST.get("pincode")
        p1=make_password(password)
        confirmpass = request.POST.get("confirmpassword")
        try:
            if (password != confirmpass):
              return render(request, "registration.html", {"error1": True})
            if not (fname.isalpha()) and len(fname)<15:
                return render(request, "registration.html", {"error3": True})
                # print("Please use only alpha charactors")
            if not (fname.isalpha()) and len(lname)<15:
                return render(request, "registration.html", {"error4": True})
                # print("Please use only alpha charactors")
            else:
                 user = Person(username=username, email=email, password=p1,
                        first_name=fname, last_name=lname, phone=phone, pincode=pincode)
                 user1=User.objects.create_user(username=username, email=email, password=p1)
                 user1.save()
                 user.save()
            return redirect("login")
        except:
            return render(request, "registration.html", {"error2": True})
    return render(request, "registration.html")


def loginpage(request):
    if request.method == 'POST':
        # global e
        user = request.POST.get("username")
        p = request.POST.get("password")
        user = authenticate(request,username=user,password=p)
        # print(user.is_staff)
        if(user.is_staff==True and user is not None):
            login(request,user)
            return redirect("admin")
        elif (user.is_staff==False and user is not None):
            login(request,user)
            return redirect("home")
        else:
            return render(request,"login.html",{"login" : True})
        
             
    return render(request,"login.html")

@login_required(login_url="login")
def homepage(request):
    user=request.user
    if(request.method=="POST"):
        username=request.POST.get("username")
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        pincode=request.POST.get("pincode")
        phone=request.POST.get("phone")
        user_m=Person.objects.get(username=user.username)
        user_m.username=username
        user_m.first_name=fname
        user_m.last_name=lname
        user_m.pincode=pincode
        user_m.phone=phone
        user.username=username
        user.save()
        user_m.save()
        
        return redirect("home")
    
    data=Person.objects.get(username=user.username)

    return render(request,"home.html",{"data":data})


def logoutPage(request):
    logout(request)
    return redirect("login")


@login_required
def adminpage(request):
    data1=request.user
    data=Person.objects.all().order_by("-id")

    return render(request,"admin.html",{"data1":data1,"data":data})


@login_required
def delete(request,id):
    user_m=Person.objects.get(id=id)
    user=User.objects.get(username=user_m.username)
    if( user_m and user):
        user_m.delete()
        user.delete()
        return redirect("admin")
    data1=request.user
    data=Person.objects.all()

    return render(request,"admin.html",{"data1":data1,"data":data})

@login_required
def editpage(request,id):
    if( request.method=="POST"):
        username=request.POST.get("username")
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        pincode=request.POST.get("pincode")
        phone=request.POST.get("phone")
        user_m=Person.objects.get(id=id)
        user=User.objects.get(username=user_m.username)
        user_m.username=username
        user_m.first_name=fname
        user_m.last_name=lname
        user_m.pincode=pincode
        user_m.phone=phone
        user.username=username
        user.save()
        user_m.save()
        return redirect("admin")
    
    data=Person.objects.get(pk=id)

    return render(request,"edit.html",{"data":data})

@login_required
def add_user(request):
    if(request.method=="POST"):
        username=request.POST.get("username")
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        email=request.POST.get("email")
        pincode=request.POST.get("pincode")
        phone=request.POST.get("phone")
        password=request.POST.get("password")
        p1=make_password(password)
        
        user = Person(username=username, email=email,
                        first_name=fname, last_name=lname, phone=phone, pincode=pincode,password=p1)
        
        user1=User.objects.create_user(username=username, email=email,password=p1)
        user1.save()
        user.save()

        return redirect("admin")
    
    return render(request,"add_user.html")