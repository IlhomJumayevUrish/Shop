from django.shortcuts import render,redirect,reverse
from django.views.generic import View
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from users.models import*
# Create your views here.
class UserView(View):
    def get(self,retquest):
        
        return render(retquest,"sign-in.html")
    def post(self,request):
        if request.POST["temp"]=="end":
            password=request.POST["password"]
            login1=request.POST["login"]
            user=authenticate(request,username=login1,password=password)
            if user is not None:
                login(request,user)
                return redirect("myshop:home")
            else:
                messages.add_message(request,messages.SUCCESS,"Name yoki password xato!")
                return render(request,"sign-in.html")
        else:
            email=request.POST["email"]
            password=request.POST["password"]
            password1=request.POST["password1"]
            login1=request.POST["login"]
            phone=request.POST["phone"]
            if password == password1:
                try:
                    user = User.objects.create_user(username=login1,email=email,password=password)
                    user.save()
                    klent=Klent(user=user,phone=phone)
                    klent.save()
                    return redirect("myshop:home")
                except:
                    messages.add_message(request,messages.SUCCESS,"Bu login band iltimos yangi login kiriting!")
                    return render(request,"sign-in.html")               

                    
            else:
                messages.add_message(request,messages.SUCCESS,"Parollar mos emas!")
                return render(request,"sign-in.html")               

           
            
