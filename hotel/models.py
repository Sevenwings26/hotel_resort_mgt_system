from django.db import models

# Create your models here.
# <!-- rooms: image, room-type, price, -->

class Room(models.Model):
    ROOM_TYPE_CHOICES = [
        ('1', 'Family'),
        ('2', 'Presidential'),
        ('3', 'Single'),
    ]

    image = models.CharField(max_length=300)
    room_type = models.CharField(max_length=20, choices=ROOM_TYPE_CHOICES, default='1',) # Optional: set a default choice if desired
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        # Display a meaningful representation of the model instance
        return f"{self.get_room_type_display()} Room"


class CarouselImage(models.Model):
    title = models.CharField(max_length=150, default='Carousel-image')
    image = models.ImageField(upload_to='carousel/')
    
    def __str__(self):
        return self.title
    

