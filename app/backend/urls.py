from django.urls import path
from backend.views import *
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', home, name='home'),
    path('add_teacher/', add_teacher, name='add_teacher'),
    path('add_student/', add_student, name='add_student'),
    path('api/get_teachers/', get_teachers, name='get_teachers'),
    path('api/get_students/', get_students, name='get_students'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('verify-certificate/', verify_certificate, name='verify_certificate'),
    path('generate-certificate/', generate_certificate, name='generate_certificate'),
]
