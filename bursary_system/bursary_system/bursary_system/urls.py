from django.contrib import admin
from django.urls import path, include
from applications.views import home
urlpatterns = [
    path('', home, name='home'), 
    path('admin/', admin.site.urls),
    path('applications/', include('applications.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    
    
]

