from django.shortcuts import redirect, render
from django.contrib import messages
from food_order_app.serializers import HotelSerializer
from django.utils import timezone
from datetime import timedelta

def home(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        current_time = timezone.now()
        end_time = current_time + timedelta(days=365)  # One year from now

        data = {
            'hotel_name': request.POST.get('hotel_name'),
            'hotel_reg_num': request.POST.get('hotel_reg_num'),
            'hotel_gst_num': request.POST.get('hotel_gst_num'),
            'address': request.POST.get('address'),
            'mobile_num': request.POST.get('mobile_num'),
            'email': request.POST.get('email'),
            'password': request.POST.get('password'),
            'number_of_table': request.POST.get('number_of_table'),
            'owner_name': request.POST.get('owner_name'),
            'subscription_plan': request.POST.get('subscription_plan'),
            'subscription_status': request.POST.get('subscription_status', False),
            'subscription_start_date': current_time,
            'subscription_end_date': end_time,
            'subscription_payment_mode': 'Gpay',
            'created_at': current_time,
            'updated_at': None,
            'deleted_at': None,
        }
        serializer = HotelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            messages.success(request, 'Hotel registered successfully.')
            return redirect('login')
        else:
            messages.error(request, 'Error registering hotel. Please check the details.')
            return render(request, 'signup.html', {'errors': serializer.errors})

    return render(request, 'signup.html')


def login(request):
    return render(request, 'login.html')

def admin_dashboard(request):
    return render(request, 'admindashboard.html')
