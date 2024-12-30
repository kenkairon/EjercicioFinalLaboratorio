from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Laboratorio
from django.db.models import F
import re


class ListarLaboratorio(ListView):
    model = Laboratorio
    template_name = 'laboratorio/lista_laboratorio.html'
    context_object_name = 'laboratorios'

    def ordenar_por_nombre(self, queryset):
        # Función para extraer números y manejar espacios correctamente
        def clave_orden(nombre):
            return [int(texto) if texto.isdigit() else texto.lower().strip() for texto in re.split(r'(\d+)', nombre)]

        # Ordenar usando la clave personalizada
        return sorted(queryset, key=lambda obj: clave_orden(obj.nombre))

    def get_queryset(self):
        queryset = super().get_queryset()
        return self.ordenar_por_nombre(queryset)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtener el contador de visitas desde las cookies del usuario
        visitas = int(self.request.COOKIES.get('visitas', 0)) + 1
        context['contador_visitas'] = visitas  # Agregar al contexto
        return context

    def render_to_response(self, context, **response_kwargs):
        # Sobrescribir para configurar la cookie
        response = super().render_to_response(context, **response_kwargs)
        response.set_cookie('visitas', context['contador_visitas'], max_age=60 * 60 * 24 * 30)  # 30 días
        return response

class DetalleLaboratorio(DetailView):
    model = Laboratorio
    template_name = 'laboratorio/laboratorio.html'
    context_object_name = 'laboratorio'

class CrearLaboratorio(CreateView):
    model = Laboratorio
    fields = ['nombre', 'ciudad', 'pais']
    success_url = reverse_lazy('laboratorios')
    template_name = 'laboratorio/formulario_laboratorio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Ingresar Laboratorio"
        context['boton_texto'] = "Crear"
        return context

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['nombre'].widget.attrs.update({'placeholder': 'Ingrese el nombre del laboratorio'})
        form.fields['ciudad'].widget.attrs.update({'placeholder': 'Ingrese la ciudad del laboratorio'})
        form.fields['pais'].widget.attrs.update({'placeholder': 'Ingrese el país del laboratorio'})
        return form

class EditarLaboratorio(UpdateView):
    model = Laboratorio
    fields = ['nombre', 'ciudad', 'pais']
    success_url = reverse_lazy('laboratorios')
    template_name = 'laboratorio/formulario_laboratorio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Actualizar Laboratorio"
        context['boton_texto'] = "Actualizar"
        return context

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['nombre'].widget.attrs.update({'placeholder': 'Actualice el nombre del laboratorio'})
        form.fields['ciudad'].widget.attrs.update({'placeholder': 'Actualice la ciudad del laboratorio'})
        form.fields['pais'].widget.attrs.update({'placeholder': 'Actualice el país del laboratorio'})
        return form

class EliminarLaboratorio(DeleteView):
    model = Laboratorio
    template_name = 'laboratorio/eliminar_laboratorio.html'
    context_object_name = 'laboratorio'
    success_url = reverse_lazy('laboratorios')

    

