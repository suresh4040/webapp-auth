from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm 
from django.core.mail import EmailMessage
from . models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from . forms import *

def index(request):
	# if request.user.is_anonymous:
		# return redirect("/home")

	return render(request,'index.html')

def about(request):
    return render(request,'about.html')

# def contact(request):
# 	if request.method == 'POST':
# 		form = ContactForm(request.POST)
# 		if form.is_valid():
# 			print(form.cleaned_data['name'])
		# send email code goes here
		# Less secure app access in gmail settings
			# sender_name = form.cleaned_data['name']
			# sender_email = form.cleaned_data['email']

			# email = EmailMessage('Subject', 'Body', to=['sureshkumar.sm@rediffmail.com'])
			# email.send()
	# 		return HttpResponse('Thanks for contacting us!')
	# else:
	# 	form = ContactForm()
	# return render(request, 'contact.html', {'form': form})

def contact(request):
	if request.method == 'POST':
		name = request.POST.get('name','')
		email = request.POST.get('email','')
		phone = request.POST.get('phone','')
		desc = request.POST.get('desc','')
		n = Contact.objects.filter(email=email)
		

		contact = Contact(name=name,email=email,phone=phone,desc=desc)
		contact.save()
		contact.uno = contact.id
		contact.save()
		messages.success(request, 'Your message has been sent successfully!')
		return HttpResponseRedirect(reverse('webapp:home'))
		""" email Validation  """
		# for each in n:
		# 	if email == each.email:
		# 		messages.success(request, 'email already exists.')
		# 	else:
		# 		contact = Contact(name=name,email=email,phone=phone,desc=desc)
		# 		contact.save()
		# 		messages.success(request, 'Your message has been sent successfully.')
		# 		return HttpResponseRedirect(reverse('webapp:home'))
		# or
		# if Contact.objects.filter(email=email).exists():
		# 	messages.success(request, 'email already exists.')
	return render(request,'contact.html')

def register_user(request):
	form = NewUserCreationForm()
	if request.method == 'POST':
		form = NewUserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username') # get user from the form
			#query the group & attch a role 
			messages.success(request,'Account was created  for ' + username)
			return redirect('/login')
	context = {'form':form}		
	return render(request,'register.html',context)
	


def login_user(request):
	if request.method == 'POST':
		#check if user has entered correct credentials
		username = request.POST.get('username')
		password = request.POST.get('password')
		#authenticate
		user = authenticate(username=username, password=password)

		if user is not None:
			login(request, user)
		
			user = request.user
			messages.success(request,"Welcome :" + str(user))
			return redirect('/home')
		else:
			messages.error(request,'Bad credentials!, Username OR Password is incorrect')
			return HttpResponseRedirect(reverse('webapp:login'))
	# No backend authenticated the credentials
	return render(request,'login.html')

def logout_user(request):
	logout(request)
	messages.success(request,"You have successfully logged out!")
	return redirect("/home")

