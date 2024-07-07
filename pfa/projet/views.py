from django.shortcuts import render, redirect

from projet.models import *

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)
        user = User.objects.filter(email=email, password=password).first()
        if user:
            if user.role == 'client':
                return redirect('client/'+ str(user.id) )
            elif user.role == 'driver':
                return redirect('driver/'+ str(user.id) )
        else:
            return redirect('/login', {'error': 'Invalid email or password'})
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')
        fullName = request.POST.get('fullName')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        car = request.POST.get('car')
        matricule = request.POST.get('matricule')
        print(email, password, role, fullName, phone, address, 0, car, matricule)
        user = User(email=email, password=password, role=role, fullName=fullName, phone=phone, address=address, credit=0, car=car, matricule=matricule)
        user.save()
        return redirect('login')
    return render(request, 'signup.html')

def client(request, id):
    user = User.objects.filter(id=id).first()
    rides = Ride.objects.filter(client=user)
    if request.method == 'POST':
        start = request.POST.get('start')
        end = request.POST.get('end')
        distance = float(request.POST.get('distance'))  # Convert distance to float
        price = distance * 0.5
        client = user
        status = 'pending'
        ride = Ride(start=start, end=end, distance=distance, price=price, client=client, status=status)
        ride.save()
    return render(request, 'client.html', {'user': user, 'rides': rides})

def clientHistory(request, id):
    user = User.objects.filter(id=id).first()
    rides = Ride.objects.filter(client=user).filter(status='reserved')
    return render(request, 'clientHistory.html', {'user': user, 'rides': rides})

def clientRidesPending(request, id):
    user = User.objects.filter(id=id).first()
    rides = Ride.objects.filter(client=user).filter(status='pending')
    return render(request, 'clientRidesPending.html', {'user': user, 'rides': rides})

def driver(request, id):
    rides = Ride.objects.filter(status='pending')
    user = User.objects.filter(id=id).first()
    rideHistory = Ride.objects.filter(driver=user)
    return render(request, 'driver.html', {'user':user,'rides': rides})

def accept(request, id):
    ride = Ride.objects.filter(id=id).first()
    ride.status = 'accepted'
    ride.save()
    return redirect('driver')

def reserve(request, id1, id2):
    user = User.objects.filter(id=id1).first()
    ride = Ride.objects.filter(id=id2).first()
    print(user.email, ride.status)
    if request.method == 'POST':
        ride.driver = user
        ride.status = 'reserved'
        notification = Notification(user=ride.client, message='Your ride has been accepted by '+ride.driver.fullName)
        notification.save()
        ride.save()
        return redirect('/login/driver/'+str(user.id))
    return render(request, 'reserve.html', {'user': user, 'ride': ride})