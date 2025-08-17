from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import Customer
from django.views.decorators.csrf import csrf_exempt
import json

def register_customer(request):
    if request.method == 'POST':
        try:
            # Handle both JSON and form data
            if request.content_type == 'application/json':
                data = json.loads(request.body)
            else:
                data = request.POST
            
            # Extract form data
            full_name = data.get('full_name')
            phone_number = data.get('phone_number')
            email = data.get('email')
            password = data.get('password')
            delivery_address = data.get('delivery_address')
            
            # Validation
            if not all([full_name, phone_number, email, password, delivery_address]):
                if request.content_type == 'application/json':
                    return JsonResponse({'error': 'All fields are required'}, status=400)
                messages.error(request, 'All fields are required')
                return render(request, 'register_customer.html')
            
            # Check if email already exists
            if Customer.objects.filter(email=email).exists():
                if request.content_type == 'application/json':
                    return JsonResponse({'error': 'Email already registered'}, status=400)
                messages.error(request, 'Email already registered')
                return render(request, 'register_customer.html')
            
            # Check if phone already exists
            if Customer.objects.filter(phone_number=phone_number).exists():
                if request.content_type == 'application/json':
                    return JsonResponse({'error': 'Phone number already registered'}, status=400)
                messages.error(request, 'Phone number already registered')
                return render(request, 'register_customer.html')
            
            # Create new customer
            customer = Customer.objects.create(
                full_name=full_name,
                phone_number=phone_number,
                email=email,
                password=password,
                delivery_address=delivery_address
            )
            
            if request.content_type == 'application/json':
                return JsonResponse({
                    'success': True,
                    'message': 'Registration successful',
                    'customer_id': customer.customer_id
                })
            
            messages.success(request, 'Registration successful! Please login.')
            return redirect('login')
        except Exception as e:
            if request.content_type == 'application/json':
                return JsonResponse({'error': str(e)}, status=500)
            messages.error(request, 'Registration failed. Please try again.')
            return render(request, 'register_customer.html')
    return render(request, 'register_customer.html')

@csrf_exempt
def register_customer_api(request):
    return register_customer(request)

def home(request):
    return render(request, 'index.html')

def checkout(request):
    return render(request, 'checkout.html')
    
def login(request):
    return render(request, 'login.html')
    
def customer_dashboard(request):
    return render(request, 'customer_dashboard.html')

def shop_dashboard(request):
    return render(request, 'shop_dashboard.html')

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def register_shop(request):
    return render(request, 'register_shop.html')

def help(request):
    return render(request, 'help.html')
