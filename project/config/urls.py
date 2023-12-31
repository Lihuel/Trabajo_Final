from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(("home.urls", "home"))),
    path("equipos/", include(("equipos.urls", "equipos"))),
    path("jugador/", include(("jugador.urls", "jugador"))),
    path("noticias/", include(("noticias.urls", "noticias"))),
]
