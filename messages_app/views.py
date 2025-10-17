from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Message
from django.contrib.auth.models import User

@login_required
def inbox(request):
    msgs = Message.objects.filter(receiver=request.user).order_by("-sent_at")
    return render(request, "messages_app/inbox.html", {"msgs": msgs})

@login_required
def detail(request, pk):
    m = get_object_or_404(Message, pk=pk, receiver=request.user)
    if not m.read:
        m.read = True; m.save()
    return render(request, "messages_app/detail.html", {"m": m})

@login_required
def new(request):
    if request.method == "POST":
        to = get_object_or_404(User, username=request.POST.get("to"))
        Message.objects.create(
            sender=request.user, receiver=to,
            subject=request.POST.get("subject",""), body=request.POST.get("body","")
        )
        return redirect("messages_app:inbox")
    users = User.objects.exclude(id=request.user.id)
    return render(request, "messages_app/new.html", {"users": users})

