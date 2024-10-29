from django.contrib import admin
from django.urls import path, include
from .views import home, cadastro, login
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    #path('caminho url', função da view, name='apelido para a model')
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('cadastro/', cadastro, name='cadastro'),
    path('login/', login, name = 'login'),
    path('veiculo/', include('veiculo.urls'), name='veiculo')
    # name = 'nome' é sensivel a Maiúsculo e minusculo!
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
