from django.urls import path
from .views import apply_bursary, application_success, signup
 
from . import views
from .models import Allocation


urlpatterns = [
    
    path('apply/', apply_bursary, name='apply_bursary'),
    path('success/', application_success, name='application_success'),
    path('signup/', signup, name='signup'),
  path('check_allocation/<str:student_type>/', views.check_allocation, name='check_allocation'),

    
    
]
