from django.db import models

# Create your models here.
# <!-- rooms: image, room-type, price, -->
from django.db import models
from django.utils.text import slugify
import uuid


class Room(models.Model):
    ROOM_TYPE_CHOICES = [
        ('Family', 'Family'),
        ('Presidential', 'Presidential'),
        ('Single', 'Single'),
    ]

    image = models.CharField(max_length=300)
    room_type = models.CharField(max_length=20, choices=ROOM_TYPE_CHOICES, default='Family')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # slug = models.SlugField(unique=True, blank=True)

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         unique_id = str(uuid.uuid4())[:8]  # Use a shortened UUID for readability
    #         self.slug = slugify(f"{self.room_type}-{unique_id}")
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.room_type} Room"


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="bookings")
    customer_name = models.CharField(max_length=100)
    check_in = models.DateField()
    check_out = models.DateField()
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking for {self.customer_name} in {self.room}"


class CarouselImage(models.Model):
    title = models.CharField(max_length=150, default='Carousel-image')
    image = models.ImageField(upload_to='carousel/')
    
    def __str__(self):
        return self.title
    

