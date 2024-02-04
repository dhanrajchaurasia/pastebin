from django.shortcuts import render, redirect
from .models import Paste
import secrets, string
from datetime import timedelta
def genkey(length=5):
    key_characters = string.ascii_letters + string.digits
    unique_key = ''.join(secrets.choice(key_characters) for _ in range(length))
    return unique_key

def home(request, key = ""):
    if key != "":
        paste = Paste.objects.filter(key=key)
        if paste.exists():
            mypaste = paste.first()
            mypaste.created_at = mypaste.created_at + timedelta(hours=5, minutes=30)
            return render(request, 'paste.html', {'paste': mypaste})
        return redirect("/")
    if request.method == "POST":
        title = request.POST.get('title', "Pastebin") if request.POST.get('title', "Pastebin").strip() else "Pastebin"
        author = request.POST.get('author', "Anonymous") if request.POST.get('author', "Anonymous").strip() else "Anonymous"
        description = request.POST.get('description', "") if request.POST.get('description', "").strip() else ""
        text = request.POST.get('text', "Nothing") if request.POST.get('text', "Nothing").strip() else "Nothing"
        key = genkey()
        paste = Paste.objects.create(title=title, author=author, description=description, text=text, key=key)
        return redirect("/" + key)
    return render(request, 'home.html')