from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ChatRoom,ChatMessage
# Create your views here.
@login_required
def index(request):
    chatrooms = ChatRoom.objects.all()
    return render(request,'chatapp/index.html',{'chatrooms':chatrooms})
@login_required
def chatroom(request,slug):
    chatroom = ChatRoom.objects.get(slug=slug)
    messages = ChatMessage.objects.filter(room=chatroom)[0:300]
    return render(request,'chatapp/room.html',{'chatroom':chatroom,'messages':messages})