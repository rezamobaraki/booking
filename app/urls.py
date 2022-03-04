"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from core.api.booking_view import VehicleDetail

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/', include('core.urls', namespace='core')),
                  path('blog/', include('blog.urls', namespace='blog')),
                  path('ckeditor/', include('ckeditor_uploader.urls')),
                  path('accounts/', include('accounts.urls', namespace='accounts')),
                  path('oauth/', include('social_django.urls', namespace='social')),
                  path('club/', include('club.urls', namespace='club')),
                  path('api/rental/<str:vehicle_id>/detail/<str:search_key>/<str:pick>/<str:drop>/',
                       VehicleDetail.as_view(),
                       name='vehicles-detail'),
                  path('', TemplateView.as_view(template_name='core/search_car.html'), name='search'),
                  # path('search/cars/', TemplateView.as_view(template_name='core/cars.html'))

              ] + [
                  path('__debug__/', include('debug_toolbar.urls')),
              ]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
