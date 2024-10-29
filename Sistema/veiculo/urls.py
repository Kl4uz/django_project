from django.urls import path
from .views import ListarVeiculos, CriarVeiculos, SerializadorVeiculo, APIListarVeiculos
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', ListarVeiculos.as_view(), name='veiculo'),
    path('criar/', CriarVeiculos, name='criar-veiculo'),
    path('api/', APIListarVeiculos.as_view(), name='api-listar-veiculo')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

