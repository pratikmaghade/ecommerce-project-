from django.contrib import admin
from .models import *

# Register your models here.
class user_class(admin.ModelAdmin):
	list_display = ('id','email','password')
admin.site.register(user, user_class)	

class customer_class(admin.ModelAdmin):
	list_display = ('id','name','email','mobile','Category','colour','cloth_type','size')
admin.site.register(customer, customer_class)	

class View_more_class(admin.ModelAdmin):
	list_display = ('id','dress_name','category','size','price','img')
admin.site.register(View_more, View_more_class)
