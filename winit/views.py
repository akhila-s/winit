from django.shortcuts import render,render_to_response
from .models import Registration,Topic,Question
import datetime
from django.contrib.auth import logout
from django.http import HttpResponse
def home(request):
	return render(request,"signup.html")
	# fields = '__all__'
def start(request):
	return render(request,"start.html")

def exam(request):
	return render(request,"exam.html")

def store(request):
	context = {}
	Firstname = request.POST.get('fname','')
	Lastname = request.POST.get('lname','')
	d = request.POST.get('dob','')
	dateofbirth = datetime.datetime.strptime(d,"%Y-%m-%d").date()
	address = request.POST.get('addr','')
	email = request.POST.get('usremail','')
	username = request.POST.get('username','')
	password = request.POST.get('password','')
	contactnumber =  request.POST.get('number','')
	# context['fname'] = Firstname
	similar = Registration.objects.filter(username = username)
	if similar:
		context['error']='Username already exists'
		return render(request,"signup.html",context)
	else:
		obj = Registration(Firstname=Firstname,Lastname=Lastname,dateofbirth=dateofbirth,address=address,
				email=email,username=username,password=password,contactnumber=contactnumber)
		obj.save()
		return render(request,"signin.html")

def check(request):
	username = request.POST.get('username','')
	password = request.POST.get('password','')
	similar = Registration.objects.filter(username = username)
	if similar:
		similar.password = password
		return render(request,"Rules.html")
	else:
		context = {}
		context['error'] = 'Inavlid username or password'
		return render(request,'signin.html',context)



def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
 
# def next(request):


# Create your views here.
