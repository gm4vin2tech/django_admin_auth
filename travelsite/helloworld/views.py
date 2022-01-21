from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def homepage(request):
	return render(request, 'index.html')


# @login_required(login_url='/login/')

def features(request):
	# if(user.is_authenticated):
		# print("user authentication")
		# print(user)
		# return reder(request, 'feature.html')
	# return render(request, 'login.html')
	return render(request, 'feature.html')

