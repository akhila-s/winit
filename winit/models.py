from django.db import models
from django.utils.encoding import smart_unicode
import datetime

# Create your models here.
class Registration(models.Model):

	Firstname = models.CharField(max_length = 30,null = True,blank = True)
	Lastname = models.CharField(max_length = 30,null = True,blank = True)
	dateofbirth = models.DateField(max_length = 30,blank = True, null = True)
	address = models.CharField(max_length = 50,null = True,blank = True)
	# gender = models.CharField(max_length = 10, choices = GENDER_CHOICE, null = True, blank = True)
	email = models.EmailField()
	username = models.CharField(max_length = 30,blank = True, primary_key=True)
	password=models.CharField(max_length=20)
	contactnumber = models.CharField(max_length=12)
	def __unicode__(self):
		return smart_unicode(self.email)

class Topic(models.Model):
	topic = models.CharField(max_length = 300, primary_key=True)
	def __unicode__(self):
		return smart_unicode(self.topic)

class Question(models.Model):
	queno =  models.IntegerField(primary_key=True)
	question = models.CharField(max_length = 50)
	topic = models.ForeignKey(Topic)

class Userdata(models.Model):
	queno = models.ForeignKey(Question)
	username = models.ForeignKey(Registration)
	answer = models.TextField(max_length = 500)
	date = models.DateField()
	score = models.IntegerField(default = 0)

		