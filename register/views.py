import email
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from account.models import Accounts
import os
from twilio.rest import Client
# Create your views here.
def loginn(request):
    if request.user.is_authenticated:
        
      if request.user.is_admin==False:
         return redirect('home')
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')
global rotp
global user 
def signedup(request):
    if request.method=='POST':
        print("signedup")
        email=request.POST.get('email')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2') 
        phone_number=request.POST.get('phone_number')
        if email=="" or first_name=="" or last_name=="" or username=="" or password1=="" or password2=="" or phone_number=="":
            messages.info(request,"Require all fields")
            return render(request,'signup.html')
        if password1==password2: 
            if Accounts.objects.filter(username=username).exists():
                messages.info(request,"User exist")
                print("1st")
                return render(request,'signup.html')
            elif Accounts.objects.filter(email=email).exists():
                messages.info(request,"Email exist")
                print("2nd")
                return render(request,'signup.html')
            else:
                
                global user 
                
                user={'first_name':first_name,'last_name':last_name,'phone_number':phone_number,'username':username,'email':email,'password':password1}
                #user= Accounts.objects.create_user(first_name=first_name,last_name=last_name,phone_number=phone_number,username=username,email=email,password=password1)
                
                
                return redirect('signed_up')

        else:
             return render(request,'signup.html')


def signed_up(request):
    global rotp
    rotp=getotp()
    #print("user created but not saved")
    global user
    
    return render(request,'otp.html')



def verify(request):
    if request.method=='POST':
        first=request.POST.get('first')
        second=request.POST.get('second')
        third=request.POST.get('third')
        fourth=request.POST.get('fourth')
        number=first+second+third+fourth
        global rotp
        
        if(number==str(rotp)):
            #print("correct")
            global user
            if user is not None:
                print(user)
                
                first_name=user["first_name"]
                last_name=user["last_name"]
                phone_number=user["phone_number"]
                username=user["username"]
                email=user["email"]
                password1=user["password"]
                user= Accounts.objects.create_user(first_name=first_name,last_name=last_name,phone_number=phone_number,username=username,email=email,password=password1)
                return redirect('home')
        
        else:
            #print('thettipoi')
            messages.info(request,"Incorrect OTP")
            return render(request,'otp.html')

    return redirect('/')

def getotp():
    import random

    # prints a random value from the list
    
    list=range(1000,9999)
    otp=random.choice(list)
    

    account_sid ='AC55ee27ce60089f5fb5d3dedca4e23b0f'
    auth_token = 'c52ee31548bebb7b098a1b004856125e'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    body = otp,
    from_ = '+13252214515',
    to    = '+919746701683' 
    )
    print("otp poytind")
    return otp
    #print(message.sid)

def forgotpassword(request):
    return render(request,'forgotpassword.html')

def loggedin(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=authenticate(request,email=email,password=password)
        if user is None: 
            print("no user")
            messages.info(request,"Invalid credentials")
        elif user is not None:
            print("user is present")
            if user.is_staff==True:
                login(request,user)
        
                return redirect('home')
            else:
                messages.info(request,"Blocked by admin")
    return render(request,'login.html') 

def landingpage(request):
    if request.user.is_authenticated:
        
      if request.user.is_admin==False:
         return redirect('home')
    return render(request,'index.html')

@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated and request.user.is_staff == True: 
        return render(request,'home.html')
    else:
        return redirect("landingpage")



def adminlogin(request):
    if request.user.is_authenticated:
      if request.user.is_admin==True:
        print("redirection didnt worked")
        return redirect('adminhome')
     
    return render(request,'adminlogin.html')

def adminloggedin(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=authenticate(request,email=email,password=password)
        if user.is_admin:
            if user is None: 
                print("no user")
            elif user is not None:
                print("user is present")
                login(request,user)
                return redirect('adminhome')
        else:
            print("admin alla")
    return render(request,'adminlogin.html') 

def logout1(request):
    logout(request)
    return redirect("landingpage")

@login_required(login_url='login')
def  adminhome(request):
    if request.user.is_admin==False:
         return redirect("login")

    name= request.user.username
    key1=Accounts.objects.all().order_by('id')
    context={'name':name,'key1':key1}
    return render(request,'adminhome.html',context)

@login_required(login_url='login')
def createadminuser(request):
    name= request.user.username
    return render(request,'createadmin.html',{'name':name})

@login_required(login_url='login')
def addadminuser(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        phone_number=request.POST.get('phone_number')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2') 
        if email=="" or first_name=="" or last_name=="" or username=="" or password1=="" or password2=="" or phone_number=="":
            messages.info(request,"Require all fields")
            return render(request,'createadmin.html')
        if password1==password2: 
            if Accounts.objects.filter(username=username).exists():
                messages.info(request,"User exist")
                print("user exitsst")
                name= request.user.username
                return render(request,'createadmin.html',{'name':name})

            elif Accounts.objects.filter(email=email).exists():
                messages.info(request,"Email exist")
                name= request.user.username
                return render(request,'createadmin.html',{'name':name})
            else:
                user= Accounts.objects.create_superuser(first_name=first_name,last_name=last_name,phone_number=phone_number,username=username,email=email,password=password1)
        return redirect('adminhome')
    
    else:
        return redirect('adminhome')

def edit1(request,pk):
   get_data=Accounts.objects.get(id=pk)
   if get_data.is_staff == True:
    get_data.is_staff=False
    get_data.save()
   else:
    get_data.is_staff=True
    get_data.save()
   return redirect(adminhome)

def delete(request,pk):
    get_data=Accounts.objects.get(id=pk)
    get_data.delete()
    return redirect(adminhome)
