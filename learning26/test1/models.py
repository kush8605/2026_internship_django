from django.db import models
from curses import meta

# Create your models here.

class User(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Admin'),('buyer', 'Buyer'),('seller', 'Seller'),
    )

    # AUTHENTICATION FIELDS
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    # CORE DATA
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='buyer')
    phone_number = models.CharField(max_length=15, unique=True)
    
    # SELLER & LOCATION FIELDS
    is_dealership = models.BooleanField(default=False)
    bio = models.TextField(max_length=500, blank=True)
    city = models.CharField(max_length=100, blank=True)
    address = models.TextField(blank=True)
    
    # TRUST FIELDS
    is_verified = models.BooleanField(default=False)
   
    # META CLASS (Organizes your table)

    class Meta:
        db_table = 'user_table'
        verbose_name_plural = 'Users'
        

    def __str__(self):
        return f"{self.username} - {self.role}"
    

class Car(models.Model):
    # This creates the link: One User -> Many Cars

    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    year = models.PositiveIntegerField()
    fuel_type = models.CharField(max_length=20) # e.g., Petrol, Diesel
    transmission = models.CharField(max_length=20) # e.g., Manual, Auto
    description = models.TextField()
    CAR_STATUS = (('available', 'Available'), ('reserved', 'Reserved'), ('sold', 'Sold'))
    status = models.CharField(max_length=15, choices=CAR_STATUS, default='available')

    class Meta:
        db_table = 'car_table'
        verbose_name_plural = 'Cars'

    def __str__(self):
        return f"{self.brand} {self.model}"   


class Inquiry(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='buyer_inquiries')
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    
    # NEW: Status to track the negotiation
    STATUS_CHOICES = (
        ('open', 'Open'),
        ('negotiating', 'Negotiating'),
        ('closed', 'Closed/Sold'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'inquiry_table'
        verbose_name_plural = 'Inquiry'

    def __str__(self):
        return f"Inquiry: {self.buyer.username} -> {self.car.brand} {self.car.model}"


class Message(models.Model):
    inquiry = models.ForeignKey(Inquiry, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    
    # NEW: Read receipt
    is_read = models.BooleanField(default=False)
    
    sent_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'message_table'
        ordering = ['sent_at'] # Shows the oldest message first, newest at the bottom
        verbose_name_plural = 'Messages'

    def __str__(self):
        return f"Message from {self.sender.username}"    


class CarImage(models.Model):
    # Link to the car
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='images')
    
    # Link to the photo
    image_url = models.URLField(max_length=500) 
    
    # Label for the photo (Front, Back, Interior)
    caption = models.CharField(max_length=100, blank=True)

    class Meta:
        db_table = 'car_image_table'
        verbose_name_plural = 'Car Images'

    def __str__(self):
        return f"Image for {self.car.brand}"
    

class TestDrive(models.Model):
    # The Buyer who wants to drive the car
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='test_drives')

    # The specific Car they are interested in
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    
    # APPOINTMENT DETAILS
    date = models.DateField()      # The day of the meeting
    time = models.TimeField()      # The specific time slot
    location = models.CharField(max_length=255) # Where the car is parked or meeting point
    
    # STATUS OF THE DRIVE
    # This helps the Seller manage their schedule
    STATUS_CHOICES = (
        ('pending', 'Pending Approval'),
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
    # Negotiation notes or special requests
    notes = models.TextField(blank=True, null=True) 
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'test_drive_table'
        ordering = ['-date', '-time'] # Shows upcoming drives at the top
        verbose_name_plural = 'Test Drive'

    def __str__(self):
        return f"Test Drive: {self.buyer.username} for {self.car.brand} {self.car.model}"    
    
class review(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()  # e.g., 1 to 5
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'review_table'
        verbose_name_plural = 'Reviews'
        ordering = ['-created_at']  # Newest reviews first  

    def __str__(self):
        return f"Review by {self.reviewer.username} for {self.car.brand} {self.car.model}"  
    
    