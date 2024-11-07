from django.shortcuts import render
from .models import Room, CarouselImage


# Create your views here.
def index(request):
    rooms = Room.objects.all()[:3]
    carousel_images = CarouselImage.objects.all()
    context = {
        "rooms":rooms,
        "carousel_images":carousel_images,
    }
    return render(request, "pages/index.html", context)

def rooms(request):
    return 
    