from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Message, Room
# Create your views here.

def home(request):
    return render(request, 'home.html')


def room(request, room):
    username = request.GET.get('username')
    roomDetails = Room.objects.get(name=room)

    # allMessages = Message.objects.all()

    return render(request, 'room.html', {
            'username': username, 
            'room_details': roomDetails,
            'room': room,
            # 'allMessages': allMessages
    })


def checkview(request):
    room = request.POST['room-name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect("/" + room+"/?username=" + username)
    else:
        newRoom = Room.objects.create(name=room)
        newRoom.save()
        return redirect("/" + room+"/?username=" + username)


def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    newMessage = Message.objects.create(
        value=message,
        user=username,
        room=room_id
    )
    
    newMessage.save()

    return HttpResponse('Message sent Successfully!!!')



