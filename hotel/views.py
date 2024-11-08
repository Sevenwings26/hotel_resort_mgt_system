from django.shortcuts import render
from .models import Room, CarouselImage
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Room, Booking
from .forms import BookingForm


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
    rooms = Room.objects.all()
    context = {
        "rooms":rooms,
    }
    return render(request, "pages/rooms.html", context)
    

def room_detail(request, slug):
    room = get_object_or_404(Room, slug=slug)
    return render(request, 'room_detail.html', {'room': room})


def book_room(request, slug):
    room = get_object_or_404(Room, slug=slug)
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.room = room
            booking.save()
            return redirect(reverse('room_list'))
    else:
        form = BookingForm()
    return render(request, 'book_room.html', {'room': room, 'form': form})
