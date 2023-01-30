from django.shortcuts import render,redirect
from.forms import RegisterForm,LoginForm,RegisterImageForm,LoginImageForm,UpdateForm,ChangePasswordForm
from django.contrib import messages
from . models import Table4,Image
from django.http import HttpResponse
from django.contrib.auth import logout as logouts
def index(request):
    name="abhin"
    return render(request,'index.html',{'data':name })
# Create your views here.

def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['Name']
            age=form.cleaned_data['Age']
            place=form.cleaned_data['Place']
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            confirmpassword=form.cleaned_data['ConfirmPassword']

            user=Table4.objects.filter(Email=email).exists()
            
            if user:
                messages.warning(request,"user already exists")
                return redirect('/register')
            elif password!=confirmpassword:
                messages.warning(request,"password missmatch")
                return redirect('/register')
            else:
                tab=Table4(Name=name,Age=age,Place=place,Email=email,Password=password)
                tab.save()
                messages.success(request,"successful")
                return redirect('/')
    else:
        form=RegisterForm(),'register.html',{'data':form};

        return render(request)
def login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']

            try:
                user=Table4.objects.get(Email=email)
            
                if not user:
                    messages.warning(request,"user doesnot exists")
                    return redirect('/login')
                elif password!=user.Password:
                    messages.warning(request,"password incorrect")
                    return redirect('/login')
                else:
                    messages.success(request,"successful")
                    return redirect('/home/%s' % user.id)
            except:
                messages.warning(request,"email/password incorrect")
                return redirect('/login')
    else:
        form=LoginForm()
    return render(request,'login.html',{'data':form})

def home(request,id):
    user=Table4.objects.get(id=id)
    return render(request,'home.html',{'user':user})

def registerimage(request):
    if request.method=='POST':
        form=registerimage(request.POST or None,request.FILES or None)
        if form.is_valid():
            name=form.cleaned_data['Name']
            age=form.cleaned_data['Age']
            place=form.cleaned_data['Place']
            email=form.cleaned_data['Email']
            photo=form.cleaned_data['Photo']
            password=form.cleaned_data['Password']
            confirmpassword=form.cleaned_data['ConfirmPassword']

            user=Image.objects.filter(Email=email).exists()
            
            if user:
                messages.warning(request,"user already exists")
                return redirect('/registerimage')
            elif password!=confirmpassword:
                messages.warning(request,"password missmatch")
                return redirect('/registerimage')
            else:
                tab=Image(Name=name,Age=age,Place=place,Photo=photo,Email=email,Password=password)
                tab.save()
                messages.success(request,"successful")
                return redirect('/')
       
            
    else:
            form=RegisterImageForm()
    return render(request,'registerimage.html',{'data':form})


def homeimage(request,id):
    user=Image.objects.get(id=id)
    return render(request,'homeimage.html',{'user':user})


def loginimage(request):
    if request.method=='POST':
        form=LoginImageForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']

            try:
                user=Image.objects.get(Email=email)
            
                if not user:
                    messages.warning(request,"user doesnot exists")
                    return redirect('/loginimage')
                elif password!=user.Password:
                    messages.warning(request,"password incorrect")
                    return redirect('/loginimage')
                else:
                    messages.success(request,'successful')
                    return redirect('/homeimage/%s' % user.id)
            
            
            except:
                messages.warning(request,"email/password incorrect")
                return redirect('/loginimage')
    else:
        form=LoginImageForm()

    return render(request,'loginimage.html',{'data':form})

def update(request,id):
    user=Table4.objects.get(id=id)
    if request.method=='POST':
        form=UpdateForm(request.POST or None,request.FILES or None,instance=user)
        if form.is_valid():
            form.save()
            messages.success(request,"updation succesful")
            return redirect('/show_users')
    else:
        form=UpdateForm(instance=user)
    return render(request,'update.html',{'user':user,'form':form})

def show_users(request):
    users=Image.objects.all()
    return render(request,'show_users.html',{'users':users})


def delete(request,id):
    users=Image.objects.get(id=id)
    users.delete()
    messages.success(request, 'deleted successfully')
    return redirect('/show_users')


def changepassword(request,id):
    user=Table4.objects.get(id=id)
    if request.method=='POST':
        form=ChangePasswordForm(request.POST)
        if form.is_valid():
            oldpassword=form.cleaned_data['OldPassword']
            newpassword=form.cleaned_data['NewPassword']
            confirmpassword=form.cleaned_data['ConfirmPassword']
            if oldpassword!=user.Password:            
                messages.warning(request,"password incorrect")
                return redirect('/changepassword/% '% user.id)
            elif newpassword==oldpassword:
                messages.warning(request,"password same")
                return redirect('/changepassword/% '% user.id)
            elif newpassword!=confirmpassword:
                messages.warning(request,"incorrect password")
                return redirect('/password/%'% user.id)
                
            else:
                user.Password=newpassword
                user.save()
                messages.success(request,'succesful')
                return redirect('/login')
       
            
    else:
            form=ChangePasswordForm()
    return render(request,'changepassword.html',{'data':form ,'user':user})

def logout(request):
    logouts(request)
    messages.success(request,'logout succesful')
    return redirect('/')