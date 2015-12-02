from django.shortcuts import render,render_to_response
from .models import Registration,Question,Userdata
import datetime
from django.http import HttpResponse
def home(request):
	return render(request,"mystyle.html")
	# fields = '__all__'
def comp(request):
	return render(request,"competitions.html")
def tc(request):
	return render(request,"termsandconditions.html")
def disc(request):
	return render(request,"disclaimer.html")
def start(request):
	username =  request.POST.get("username")
	# top = Topic.objects.all()
	return render(request,"start.html",{"username":username})
		#{"top":top})

def answer(request):
	text = {}
	if request.method == "POST":
		Ans = request.POST.get('essay','')
		queno = int(request.POST.get('qno',''))
		queno = Question.objects.get(queno = queno)
		username = str(request.POST.get('username',''))
		username = Registration.objects.get(username = username)
		date = datetime.datetime.now()
		score = 0
		data = Userdata(queno=queno,username=username,answer=Ans,date=date,score=score)
		data.save()
	return render(request,"thanku.html")

def thanku(request):
	return render(request,"thanku.html")
def exam(request):
	username = request.POST.get('username','')
	question = Question.objects.all().order_by('?')[:1]
	return render(request,"exam.html",{'question':question,'username':username})
def store(request):
	context = {}
	if request.method =="POST" :
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
	else :
		return render(request,"signup.html",context)

def check(request):
	context = {}
	if request.method == 'POST':
		username = request.POST.get('username','')
		password = request.POST.get('password','')
		similar = Registration.objects.get(username = username)
		if similar:
			if similar.password == password:
				return render(request,"Rules.html",{"username":username})
		else:
			context['error'] = 'Inavlid username or password'
	return render(request,'signin.html',context)
# Create your views here.
