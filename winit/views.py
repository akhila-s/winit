from django.shortcuts import render,render_to_response
<<<<<<< HEAD
from .models import Registration,Topic,Question
import datetime
from django.contrib.auth import logout
=======
from .models import winit
import datetime
>>>>>>> 214f5e505f066e8928b8c039fa1209fd1b263aae
from django.http import HttpResponse
def home(request):
	return render(request,"signup.html")
	# fields = '__all__'
<<<<<<< HEAD
def start(request):
	return render(request,"start.html")

def exam(request):
	return render(request,"exam.html")

=======
>>>>>>> 214f5e505f066e8928b8c039fa1209fd1b263aae
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
<<<<<<< HEAD
	similar = Registration.objects.filter(username = username)
=======
	similar = winit.objects.filter(username = username)
>>>>>>> 214f5e505f066e8928b8c039fa1209fd1b263aae
	if similar:
		context['error']='Username already exists'
		return render(request,"signup.html",context)
	else:
<<<<<<< HEAD
		obj = Registration(Firstname=Firstname,Lastname=Lastname,dateofbirth=dateofbirth,address=address,
=======
		obj = winit(Firstname=Firstname,Lastname=Lastname,dateofbirth=dateofbirth,address=address,
>>>>>>> 214f5e505f066e8928b8c039fa1209fd1b263aae
				email=email,username=username,password=password,contactnumber=contactnumber)
		obj.save()
		return render(request,"signin.html")

def check(request):
	username = request.POST.get('username','')
	password = request.POST.get('password','')
<<<<<<< HEAD
	similar = Registration.objects.filter(username = username)
	if similar:
		similar.password = password
		return render(request,"Rules.html")
=======
	similar = winit.objects.filter(username = username)
	if similar:
		similar.password = password
		return render(request,"start.html")
>>>>>>> 214f5e505f066e8928b8c039fa1209fd1b263aae
	else:
		context = {}
		context['error'] = 'Inavlid username or password'
		return render(request,'signin.html',context)
<<<<<<< HEAD



def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
 
# def next(request):


=======
>>>>>>> 214f5e505f066e8928b8c039fa1209fd1b263aae
# Create your views here.
