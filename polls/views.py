
from django.shortcuts import render , redirect
from polls.forms import registrationform
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, PasswordResetForm 
from polls.models import uuprofile
from django.contrib.auth import authenticate, login as alogin, views as auth_views
from django.contrib.auth.views import LoginView, PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from django.contrib.auth import update_session_auth_hash, logout
from django.core.mail import EmailMessage
from django.contrib import messages
import json

# Create your views here.


def mandaremail(request,args):
	if(request.GET.get('mybtn')):
		emailcliente=str(request.GET.get('emailend'))
		emailtext=str(request.GET.get('emailtext'))
		email = EmailMessage('Cliente: ' + emailcliente, emailtext, to=['jh_gcc@hotmail.com'])
		email.send()
		modelo = True
		args['modelo']=modelo
	return args


def register(request):
	nomeoulogin, logout, profile, email,pais, nome, nome2 = checarlogin(request)
	args={'nomeoulogin':nomeoulogin,'logout':logout, 'profile':profile}
	req=request.POST.get('username')
	if request.method =='POST':
		form = registrationform(request.POST)
		args['form']=form
		if form.is_valid():
			username=form.save()
			mudanca=uuprofile.objects.get(usuario=username)
			mudanca.save()
			modelo2 = True
			args['modelo2']=modelo2
			return redirect('login')
		else:
			return render(request,"register.html",args)

	else:
		form = registrationform()
		args['form']=form
		return render(request,"register.html",args)

def home(request):
	nomeoulogin, logout, profile, email, pais, nome, nome2 = checarlogin(request)
	args={'nomeoulogin':nomeoulogin,'logout':logout, 'profile':profile}
	return render(request,"main.html",args)
    
def about(request):
	nomeoulogin, logout, profile, email, pais, nome, nome2 = checarlogin(request)
	args={'nomeoulogin':nomeoulogin,'logout':logout, 'profile':profile}
	return render(request,"main.html",args)

def checarlogin(request):
	if request.user.is_authenticated:
		nomeoulogin='Welcome, ' + str(request.user)
		logout='Logout'
		profile='Profile'
		email=str(request.user.email)
		nome=str(request.user.first_name)
		nome2=str(request.user.last_name)
		pegarperfil= uuprofile.objects.get(usuario=request.user)
		pais=str(pegarperfil.country)
	else:
		nomeoulogin=''
		logout='Login'
		profile=''
		email=''
		nome=''
		nome2=''
		pais=''
		
	return nomeoulogin, logout, profile, email, pais, nome, nome2
def login(request):
	args={}
	if request.method =='POST':
		form = loginform(request.POST)
		if form.is_valid():
			nome=request.POST.get('nome')
			senha=request.POST.get('senha')

			user = authenticate(request,username=nome, password=senha)
			if user is not None:
				alogin(request,user)
				
				return redirect('home')
			else:
				args["errorLogin"]="initial"
				return render(request,"login.html",args)
	else:
		return render(request,"login.html",args)