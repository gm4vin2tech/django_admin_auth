from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth


# Create your views here.

def register(request):
	print(request.method)
	print('request meth')
	if request.method == 'POST':
		username = request.POST['user_name']
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		password = request.POST['password']
		confirm_password = request.POST['confirm_password']

		user = User.objects.create_user(username = username, password = password, email = email, first_name = first_name, last_name = last_name)
		user.save()

		print('user created')
		return redirect('/') #homepage

	print("user not created")
	return render(request, 'register.html')

def login(request):
	if request.method == 'POST':
		username = request.POST['user_name']
		password = request.POST['password']
		user = auth.authenticate(username = username, password = password)

		print(user)
		print("ccccccccccccccccccccccccccc")
		if user.is_authenticated:
			auth.login(request, user)
			# messages.info(request, "Successful User")
			return redirect("/")
		else:	
			# messages.info(request, "invalid User")
			return redirect("login")

	return render(request, 'login.html')

def logout(request):
	auth.logout(request)
	return render(request, 'logout.html')
