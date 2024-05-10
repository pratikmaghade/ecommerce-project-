from django.shortcuts import render, redirect
from django.http import HttpResponse
from .import views
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage
import traceback
from django.http import JsonResponse
from django.conf import settings
import stripe

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')

def login(request):
    return render(request, 'login.html')

@csrf_exempt
def login_check(request):
    email= request.POST.get('email')
    password= request.POST.get('password')
    
    if user.objects.filter(email=email,password=password).exists():
        user_obj = user.objects.get(email=email,password=password)
        request.session['user_id'] = str(user_obj.id)

        return HttpResponse("success")
    else:
        return HttpResponse("error")
    
@csrf_exempt
def send_message(request):
    if request.method == "POST":
        print("..........................")
        user_id = request.POST.get("user_id")
        email= request.POST.get("email") 
        name = request.POST.get("name")        
        mobile = request.POST.get("mobile")        
        Category = request.POST.get("Category")        
        colour = request.POST.get("colour") 
        cloth_type = request.POST.get("cloth_type")        
        size = request.POST.get("size")        

        
        obj = customer.objects.create(email=email,name=name, mobile=mobile,Category=Category,colour=colour,cloth_type=cloth_type,size=size)
        obj.save()
        try:
            subject = 'welcome to SB Creations Outlet'
            message = 'Your Booking Is Completely'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail( subject, message, email_from, recipient_list )          
            return JsonResponse({"msg": "success", "message":message})            
        except:
            print(traceback.print_exc())
            return HttpResponse("error")
        else:
            return HttpResponse("error")
    
def lehenga(request):
    return render(request, "lehenga.html")

def saree(request):
    return render(request, "saree.html")

def navari(request):
    return render(request, "navari.html")

def suit(request):
    return render(request, "suit.html")

def redimade(request):
    obj = View_more.objects.all().order_by("-id")
    list=[]
    dict={}
    for i in obj:
        dict["id"]=i.id
        dict["dress_name"]=i.dress_name
        dict["category"]=i.category
        dict["size"]=i.size
        dict["price"]=i.price
        dict["img"]=i.img
        list.append(dict)
        dict={}
    return render(request, "redimade.html",{"list":list})
  

def edit_check(request,id):
    obj = View_more.objects.get(id=id)
    return render(request, "check.html",{"obj":obj})

def get_context_data(self, **kwargs):
    context =  super().get_context_data(**kwargs)
    context['key'] = settings.STRIPE_PUBLISHABLE_KEY
    return context   

def charge(request):
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=500,
            currency='usd',
            description = 'Payment Gateway',
            source= request.POST['stripeToken']
        )
        return render(request, 'charge.html')


