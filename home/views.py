from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm


def homepage(request):
    return render(request,
     'homepage.html',
		 {}
		 )

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				#messages.info(request, "You are now logged in as {{user.username}}.")
				return redirect("homepage")
			else:
				messages.error(request,"Usuario o contraseña invalido.")
		else:
			messages.error(request,"Usuario o contraseña invalido.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "Has cerrado sesión exitosamente.") 
	return redirect("login")