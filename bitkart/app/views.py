from django.shortcuts import render
from .models import Customer,Product,Cart,OrderPlaced
from django.views import View
from .forms import CustomerRegistrationForm 
from django.contrib import messages

class ProductView(View):
 def get(self,request):
  top_wear=Product.objects.filter(category='TW')
  bottom_wear=Product.objects.filter(category='BW')
  mobiles=Product.objects.filter(category='M')
  laptops=Product.objects.filter(category='L')
  return render(request,'app/home.html',{'top_wear':top_wear,'bottom_wear':bottom_wear,'mobiles':mobiles,'laptops':laptops})
 
class ProductDetailView(View):
 def get(self,request,pk):
  product=Product.objects.get(pk=pk)
  return render(request,'app/productdetail.html',{'product':product})

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')
def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request,data=None):
 if data==None:
  mobiles=Product.objects.filter(category='M')
 elif data=='mi' or data=='samsung':
  mobiles=Product.objects.filter(category='M').filter(brand=data)

 elif data=='Below':
    mobiles=Product.objects.filter(category='M').filter(discounted_price__lt=10000)

 elif data=='Above':
    mobiles=Product.objects.filter(category='M').filter(discounted_price__gt=10000)
 
 return render(request, 'app/mobile.html',{'mobiles':mobiles})


# def customerregistration(request):
#  return render(request, 'app/customerregistration.html')

class CustomerRegistrationView(View):
 def get(self,request):
  form=CustomerRegistrationForm()
  return render(request,'app/customerregistration.html',{'form':form})
 
 def post(self,request):
  form=CustomerRegistrationForm(request.POST)
  if form.is_valid():
   messages.success(request,'Congratulatiions !! Registered Successfully')
   form.save()
  return render(request,'app/customerregistration.html',{'form':form})

def checkout(request):
 return render(request, 'app/checkout.html')
