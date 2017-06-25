from django.forms import ModelForm, TextInput, Textarea, NumberInput

from manager.models import Building


class BuildingForm(ModelForm):
	class Meta:
		model = Building

		fields = ['name', 'address', 'rif', 'apartament_number']

		widgets = {
			'name': TextInput(attrs={'class': 'form-control'}),
			'address': Textarea(attrs={'class': 'form-control'}),
			'rif': TextInput(attrs={'class': 'form-control'}),
			'apartament_number': NumberInput(attrs={'class': 'form-control'}),
		}
