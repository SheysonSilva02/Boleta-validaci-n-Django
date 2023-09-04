from django.urls import path
from .views import CustomLoginView, RegistroEmpleadoView, mostrar_boleta

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'), 
    path('login/', CustomLoginView.as_view(), name='login'),
    path('registro/', RegistroEmpleadoView.as_view(), name='registro_empleado'),  # Usa RegistroEmpleadoView
    path('boleta/<int:empleado_id>/', mostrar_boleta, name='mostrar_boleta'),
]