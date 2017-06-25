from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from manager.forms import BuildingForm
from manager.models import Building


class BuildingListView(ListView):
	model = Building

	context_object_name = 'building_list'

	template_name = 'manager/building/building_list.html'


class BuildingAddView(CreateView):
	model = Building

	template_name = 'manager/building/building_form.html'

	form_class = BuildingForm

	def get_success_url(self):
		return reverse_lazy('manager.building.list')

	def get_context_data(self, **kwargs):
		data = super(BuildingAddView, self).get_context_data(**kwargs)

		data['title_form'] = 'Agregar Edificio'

		return data


class BuildingEditView(UpdateView):
	model = Building

	template_name = 'manager/building/building_form.html'

	form_class = BuildingForm

	def get_success_url(self):
		return reverse_lazy('manager.building.list')

	def get_context_data(self, **kwargs):
		data = super(BuildingEditView, self).get_context_data(**kwargs)

		data['title_form'] = self.object

		return data
