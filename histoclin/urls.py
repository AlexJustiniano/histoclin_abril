"""histoclin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login
from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import TemplateView

from cineantro import views

from cineantro.views import (
    MyAppBuscar,
    MyAppCreate,
    MyAppDelete,
    MyAppUpdate,
    MyAppDetail,
    MyAppList,
    MyAppTemplateView,
    
    )


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^inicio/$', login, {'template_name':'inicio.html'}, name='login'),
    #url(r'^inicio/$', MyAppTemplateView.as_view()),
    url(r'^create/$', MyAppCreate.as_view(), name='f_paciente'),
    url(r'^detail/(?P<pk>\d+)/$', MyAppDetail.as_view(), name='detail'),
    url(r'^detail/(?P<pk>\d+)/update$', MyAppUpdate.as_view(), name='update'),
    url(r'^detail/(?P<pk>\d+)/delete$', MyAppDelete.as_view(), name='delete'),
    url(r'^list/$', MyAppList.as_view(), name='list'),
    url(r'^buscar/$', MyAppBuscar.as_view(), name='buscar'),
    #url(r'^paciente/', views.paciente, name='form_paciente'),
    url(r'^institucion/', views.institucion, name='form_institucion'),
    url(r'^examen/$', views.CrearExamen, name='crear_examen'),
    #url(r'^$', views.inicio, name='inicio')
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
