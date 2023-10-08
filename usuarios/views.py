from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.http import Http404
from .models import InformacionAdicionalUsuario, MultimediaUsuario
from django.contrib.auth.models import User

def home(request):
    return render(request, "home.html")

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Crear la instancia de InformacionAdicionalUsuario asociada al usuario
            InformacionAdicionalUsuario.objects.create(user=user)

            # Crear la instancia de MultimediaUsuario asociada al usuario
            multimedia_usuario = MultimediaUsuario(user=user)
            multimedia_usuario.save()

            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("homepage")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="register.html", context={"form":form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("homepage")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect("homepage")    

def show_user_info(request, username):
    try:
        usuario = User.objects.get(username=username)
        info_adicional = InformacionAdicionalUsuario.objects.get(user=usuario)
        multimedia = MultimediaUsuario.objects.get(user=usuario)
    except User.DoesNotExist:
        raise Http404("Usuario no encontrado")

    context = {
        'usuario': usuario,
        'puntuacion': info_adicional.puntuacion,
        'imagen': multimedia.imagenPerfil
    }

    return render(request, "show_user_info.html", context)
