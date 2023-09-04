from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import RegistroForm
from .models import Empleado

class CustomLoginView(LoginView):
    template_name = 'login.html'

@method_decorator(login_required, name='dispatch')
class RegistroEmpleadoView(View):
    template_name = 'registro_empleado.html'

    def get(self, request):
        form = RegistroForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = RegistroForm(request.POST)
        if form.is_valid():
            empleado = form.save()
            return redirect('mostrar_boleta', empleado_id=empleado.pk)
        return render(request, self.template_name, {'form': form})

@login_required
def mostrar_boleta(request, empleado_id):
    empleado = Empleado.objects.get(id=empleado_id)
    return render(request, 'mostrar_boleta.html', {'empleado': empleado})