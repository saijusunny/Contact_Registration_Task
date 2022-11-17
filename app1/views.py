from django.shortcuts import render, redirect

# Create your views here.
from .models import Contact
from .forms import ContactForm

from  django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
from urllib.request import Request


def signup(request):
    return render(request, 'contact/signup.html')

def loginpage(request):
    return render(request, 'contact/login.html')

def usercreate(request):
    if request.method=="POST":
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        username=request.POST['username']
        password=request.POST['password']
        cpass=request.POST['cpassword']
        email=request.POST['email']

        if password==cpass:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'This Username Is Already Exists!!!!!')
                return redirect('signup')
            else:
                user=User.objects.create_user(
                    first_name=fname,
                    last_name=lname,
                    username=username,
                    password=password,
                    email=email,
                )
                user.save()
        else:
            messages.info(request, 'Password doesnot match!!!!!')
            return redirect('signup')
        return redirect('adminlogin')
    else:
        return render(request, 'contact/signup.html')

def adminlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request,username=username, password=password)
       
        if user is not None:
            
            auth.login(request, user)
            messages.info(request, f'Welcome {username}')#pass users name to welcome page
            return redirect('allcont')
        else:
            messages.info(request, 'invalid username and password, try again')
            return redirect('loginpage')
    else:
        return redirect('loginpage')

@login_required(login_url='adminlogin')
def all_cont(request):
    conts = Contact.objects.filter(user=request.user.id)
    context = {
        'conts': conts
    }
    return render(request, 'contact/index.html', context)


from django.contrib import messages

@login_required(login_url='adminlogin')
def add_cont(request):
    form = ContactForm()
    print(request.user.id)
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            Contact.objects.create(
                user=request.user,
                name=form.cleaned_data['name'],
                pic=form.cleaned_data['pic'],
                mobile=form.cleaned_data['mobile'],
                email=form.cleaned_data['email'],
                

            )
            messages.add_message(request, messages.INFO, f"Contact {form.cleaned_data.get('name')} has been added")
            return redirect('allcont')
    context = {
        'form': form,
    }
    return render(request, 'contact/addCont.html', context)

@login_required(login_url='adminlogin')
def edit_cont(request, id=None):
    
    
        one_emp = Contact.objects.get(id=id)
        form = ContactForm(request.POST or None, request.FILES or None, instance=one_emp)
        if form.is_valid():
            form.save()

            messages.add_message(request, messages.INFO, f"{form.cleaned_data.get('name')} has been added")
            return redirect('allcont')

        context = {
            'form': form,
        }
        return render(request, 'contact/editCont.html', context)
    

@login_required(login_url='adminlogin')
def one_cont(request, id=None):
    cot = Contact.objects.get(id=id)
    context = {
        'cot': cot
    }
    return render(request, 'contact/viewCont.html', context)

@login_required(login_url='adminlogin')
def delete_cont(request, id=None):
    cont = Contact.objects.get(id=id)
    if request.method == "POST":
        cont.delete()
        messages.add_message(request, messages.INFO, f"{cont.name} Contact Deleted")
        return redirect('allcont')
    context = {
        'cont': cont
    }
    return render(request, 'contact/delete.html', context)


@login_required(login_url='adminlogin') #login  session method
def adminlogout(request):
    auth.logout(request)
    return redirect('loginpage')







