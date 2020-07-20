from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.forms import ValidationError
from django.shortcuts import render , redirect

class changepass(PasswordChangeForm):	
    
	class Meta:
		model = User
		fields = ('old_password',
		'new_password2',
		'new_password1')
		#'extra_field')
		
	def __init__(self, *args, **kwargs):
		super(changepass, self).__init__(*args, **kwargs)
		for x in self.fields:
			self.fields[x].widget.attrs.update({'class' : 'form-control'})
		#self.fields['old_password'].widget.attrs.update({'class' : 'form-control'})
		#self.fields['extra_field'].label = "Country:"
		#for fieldname in ['username', 'password1', 'password2']:
			#ajaja=1
			#self.fields[fieldname].help_text =
 		
	def save(self, commit=True,*args, **kwargs):
		user = super(changepass, self).save(commit=False)
		
		#user.extra_field = request.POST.get('pais')
		
	
		
		if commit:
			user.save()	
			
			return user


class registrationform(UserCreationForm):	
    
	class Meta:
		model = User
		fields = ('username',
		'first_name',
		'last_name',
		'email',
		'password1',
		'password2')
		#'extra_field')
		
	def __init__(self, *args, **kwargs):
		super(registrationform, self).__init__(*args, **kwargs)
		#self.fields['extra_field'].label = "Country:"
		for fieldname in ['username', 'password1', 'password2']:
			ajaja=1
			#self.fields[fieldname].help_text =
		for x in self.fields:
			self.fields[x].widget.attrs.update({'class' : 'form-control'})


	def clean_email(self):
		email = self.cleaned_data.get('email')
		if User.objects.filter(email=email).exists():
			raise ValidationError("This email address is already in use. Please supply a different email address.")
		return email


	def save(self, commit=True,*args, **kwargs):
		user = super(registrationform, self).save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']	
		username= self.cleaned_data['username']
		#user.extra_field = request.POST.get('pais')
		if commit:
			user.save()	
			
			return user