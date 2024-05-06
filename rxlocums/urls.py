"""
URL configuration for rxlocums project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from rxApp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('download/<path:file_path>/', views.download_file, name='download_file'),
    path('', views.home, name='home'),
    path('hospitals/', views.hospitals, name='hospitals'),
    path('physicians/', views.physicians, name='physicians'),
    path('nurses/', views.nurses, name='nurses'),
    #path('telemedicine/', views.telemedicine, name='telemedicine'),
   # path('visa/', views.visa, name='visa'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('login_page/', views.login_page, name='login_page'),
    path('logout_page/', views.logout_page, name='logout_page'),
    path('admin_page/', views.admin_page, name='admin_page'),
    path('admin_physician/', views.admin_physician, name='admin_physician'),
    path('admin_nurse/', views.admin_nurse, name='admin_nurse'),
   # path('admin_telemedicine/', views.admin_telemedicine, name='admin_telemedicine'),
   # path('admin_visa/', views.admin_visa, name='admin_visa'),
    path('admin_contact/', views.admin_contact, name='admin_contact'),
    path('admin_hospital_detail/<int:id>/', views.admin_hospital_detail, name='admin_hospital_detail'),
    path('admin_physician_detail/<int:id>/', views.admin_physician_detail, name='admin_physician_detail'),
    # path('admin_telemedicine_detail/<int:id>/', views.admin_telemedicine_detail, name='admin_telemedicine_detail'),
   # path('admin_visa_detail/<int:id>/', views.admin_visa_detail, name='admin_visa_detail'),
   path('admin_nurse_detail/<int:id>/', views.admin_nurse_detail, name='admin_nurse_detail'),
    path('admin_contact_detail/<int:id>/', views.admin_contact_detail, name='admin_contact_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
