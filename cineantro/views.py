from django.shortcuts import render, redirect

from django.core.urlresolvers import reverse, reverse_lazy
from django.forms import formset_factory

from .forms import PacienteModForm, InstitucionModForm, ExamenModForm, ExamenFormset
from .models import Paciente, Examen

from django.forms.models import modelformset_factory, inlineformset_factory
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# Create your views here.


#---- VISTAS PARA PACIENTES

class MyAppCreate(CreateView):
	#model = Paciente
	#fields = ["nombre", "apellidos"]
	form_class = PacienteModForm
	template_name = "form_paciente.html"

	def get_success_url(self):
		return reverse("list")

class MyAppUpdate(UpdateView):
	model = Paciente
	form_class = PacienteModForm
	template_name = "update_paciente.html"

	def get_success_url(self):
		return reverse("list")	

class MyAppDelete(DeleteView):
	model = Paciente

	def get_success_url(self):
		return reverse("list")	

class MyAppTemplateView(TemplateView):
	template_name = "inicio.html"

	def get_success_url(self):
		return reverse_lazy("f_paciente")

class MyAppDetail(DetailView):
	model = Paciente

class MyAppList(ListView):
	model = Paciente

	def get_queryset(self, *args, **kwargs):
		qs = super(MyAppList, self).get_queryset(*args, **kwargs)
		return qs

class MyAppBuscar(TemplateView):
	model = Paciente
	template_name = "buscar.html"

	
	def post(self, request, *args, **kwargs):
		buscar = request.POST['q']
		pacientes = Paciente.objects.filter(apellidos__contains=buscar)
	
		return render(request,'buscar.html',{"pacientes": pacientes})

#----FIN DE VISTAS PARA PACIENTES

###################################

#----VISTAS PARA EXAMENES (CRUD)


def CrearExamen(request):
	#ExamenFormset = formset_factory(ExamenModForm)
	formset = ExamenFormset(queryset=Examen.objects.all())
	if request.method == 'POST':
		formset = ExamenFormset(request.POST, queryset=Examen.objects.all())
		if (formset.is_valid()):
			message = "Thanks"
			examenes = formset.save(commit=False)

			#for obj in formset.deleted_objects:
			#	obj.delete()

			for examen in examenes:
				examen.save()
			pass
		else:
			message = "Error"
		return render(request, 'form_examen.html', {'message': message})
	else:
		return render(request, 'form_examen.html', {'formset': ExamenFormset})
 	   



#----FIN DE VISTAS PARA EXAMENES

def paciente(request):
	form = PacienteModForm(request.POST or None)
	context = {
		"el_form": form,
	}

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		#return redirect(instance)
	
	return render(request, "form_paciente.html", context)

def institucion(request):
	form = InstitucionModForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()

	context = {
		"el_form": form,
	}
	return render(request, "form_institucion.html", context)