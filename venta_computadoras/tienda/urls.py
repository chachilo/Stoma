# tienda/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import  lista_computadoras, detalle_computadora, pagina_principal, iniciar_sesion


urlpatterns = [
    path('', iniciar_sesion, name='iniciar_sesion'),
    path('computadoras/', lista_computadoras, name='lista_computadoras'),
    path('computadoras/<int:computadora_id>/', detalle_computadora, name='detalle_computadora'),
    path('pagina_principal/', pagina_principal, name='pagina_principal'),  # Añade esta línea
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
