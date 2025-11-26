from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

ROLE_CHOICES = (
    ('Seller', 'Seller'),
    ('Buyer', 'Buyer')
)

MARK_CHOICES = (
    ('toyota', 'Toyota'),
    ('lexus', 'Lexus'),
    ('honda', 'Honda'),
    ('volvo', 'Volvo'),
    ('chevrolet', 'Chevrolet'),
    ('ford', 'Ford'),
    ('mazda', 'Mazda'),
    ('mercedes-benz', 'Mercedes-Benz'),
    ('volkswagen', 'Volkswagen'),
    ('hyundai', 'Hyundai'),
    ('nissan', 'Nissan'),
    ('audi', 'Audi'),
    ('mitsubishi', 'Mitsubishi'),
    ('bmw', 'Bmw')
)

TIME_STATUS = (
    ('Active', 'Active'),
    ('Finished', 'Finished')
)

class User(AbstractUser):
    role = models.CharField(choices=ROLE_CHOICES, default='Buyer')
    data_registered = models.DateField(auto_now_add=True)
    token = models.CharField(max_length=16)

    def __str__(self):
        return self.username

class Car(models.Model):
    image = models.ImageField(upload_to='car_images/')
    brand = models.CharField(choices=MARK_CHOICES, default=None)
    model = models.CharField(max_length=64, blank=True, null=True)
    year = models.DateField(blank=True, null=True)
    transmission = models.CharField(max_length=64, blank=True, null=True)
    fuel_type = models.CharField(max_length=64, blank=True, null=True)
    mileage = models.CharField(max_length=64)
    description = models.TextField(blank=True, null=True)
    price = models.PositiveSmallIntegerField()
    seller = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.brand} - {self.model} - {self.price}'

class Auction(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    start_price = models.PositiveSmallIntegerField()
    start_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=TIME_STATUS, default=None)

    def __str__(self):
        return f'{self.car} - {self.status}'

class Bid(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.amount

class Feedback(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sellers')
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='buyers')
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(11)])
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.rating}/10'