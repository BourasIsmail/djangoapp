from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    fullName = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    credit = models.FloatField()
    car = models.CharField(max_length=50)
    matricule = models.CharField(max_length=50)

class Ride(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client')
    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='driver', null=True)
    start = models.CharField(max_length=50)
    end = models.CharField(max_length=50)
    distance = models.FloatField()
    price = models.FloatField()
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

class Review(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE)
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='clientReview')
    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='driverReview')
    rating = models.FloatField()
    comment = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Notification(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



