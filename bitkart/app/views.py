from django.shortcuts import render,redirect
from .models import Customer,Product,Cart,OrderPlaced
from django.views import View
from .forms import CustomerRegistrationForm ,CustomerProfileForm
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
 user=request.user
 product_id=request.GET.get('prod_id')
 product=Product.objects.get(id=product_id)
 Cart(user=user,product=product).save()
 return redirect('/cart')

def show_cart(request):
 user=request.user
 if user.is_authenticated:
  carts=Cart.objects.filter(user=user)
  total_amt=0.0
  delivery_charge=50
  for cart in carts:
   product=cart.product
   total_amt+=(cart.quantity*product.discounted_price)
  total=total_amt+delivery_charge
  message=""
  if(total==delivery_charge):
   total=0
   message="Your cart is empty"
  return render(request, 'app/addtocart.html',{'carts':carts,'total_amt':total_amt,'delivery_charge':delivery_charge,'total':total,'message':message})
 

def buy_now(request):
 return render(request, 'app/buynow.html')


def address(request):
 new_add=Customer.objects.filter(user=request.user)
 return render(request, 'app/address.html',{'new_add':new_add,'active':'btn-primary'})

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
   messages.success(request,'Congratulations !! Registered Successfully')
   form.save()
  return render(request,'app/customerregistration.html',{'form':form})

def checkout(request):
 return render(request, 'app/checkout.html')


class ProfileView(View):
 def get(self,request):
  form=CustomerProfileForm()
  return render(request,'app/profile.html',{'form':form,'active':'btn-primary'})
 
 def post(self,request):
  form=CustomerProfileForm(request.POST)
  if form.is_valid():
   messages.success(request,'Congratulations !! Address added Successfully')
   form.save()
  return render(request,'app/profile.html',{'form':form,'active':'btn-primary'})