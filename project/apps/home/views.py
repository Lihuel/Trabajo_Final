from django.shortcuts import render
from datetime import datetime
from django.contrib.auth import authenticate, login
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.forms import AuthenticationForm
from . import forms


def index(request):
    return render(request, "home/index.html")

def laliga(request):
    now = datetime.now()
    Fecha = now.strftime("%d de  %B del %Y ")
    # fecha = f"{now}".split()[0] 
    # year,month,day = fecha.split("-") 
    # months = {1:"Enero", 2: "Febrero", 3:"Marzo", 4:"Abril", 5:"Mayo", 6:"Junio", 7:"Julio", 8:"Agosto"}
    # Fecha = f"{day} de {months[int(month)]} del {year}"
    return render(request, "home/laliga.html", {"Fecha": Fecha})


def nosotros(request):
    return render(request, "home/nosotros.html")


# def login_request(request):
#     if request.method == "POST":
#         form = forms.CustomAuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             usuario = form.cleaned_data.get("username")
#             contraseña = form.cleaned_data.get("password")
#             user = authenticate(username=usuario, password=contraseña)
#             if user is not None:
#                 login(request, user)
#                 return render(request, "home/index.html", {"mensaje": f"Usted a sido logeado como {usuario}"})
#     else:
#         form = AuthenticationForm()
#     return render(request, "home/login.html", {"form": form})
@staff_member_required
def register(request):
    if request.method == "POST":
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "home/index.html", {"Usuario": username})
    else:
        form = forms.CustomUserCreationForm()
    return render(request, "home/register.html", {"form": form})

# def noticias(request):
#     return render(request, "noticias/index.html")