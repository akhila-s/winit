from django.contrib import admin

# Register your models here.
from .models import Registration,Topic,Question,Userdata

class RegistrationAdmin(admin.ModelAdmin):
	# list_display = ['first_name', 'last_name', 'dateofbirth','gender','email','username','password','confirm_password','contact_number']
	class Meta:
		model = Registration
admin.site.register(Registration,RegistrationAdmin)
admin.site.register(Topic)
admin.site.register(Question)
admin.site.register(Userdata)