from django import forms
from .models import Country, CountryEntity, Municipality, country_entity_list, country_list, canton_list

class CountryForm(forms.ModelForm):

	country_name = forms.CharField(max_length=100, label= "Ime države", widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta:
		model = Country
		fields = ['country_name']

class CountryEntityForm(forms.ModelForm):

	entity_name = forms.CharField(max_length=100, label= "Ime države", widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta:
		model = CountryEntity
		fields = ['entity_name']

class MunicipalityForm(forms.ModelForm):

	municipality_name = forms.CharField(max_length=100)
	municipality_code = forms.CharField(max_length=3)
	country_entity = forms.IntegerField()
	country_entity = forms.ChoiceField(choices=country_entity_list())
	country = forms.ChoiceField(choices=country_list())
	canton = forms.ChoiceField(choices=canton_list(), required=False)

	class Meta:
		model = Municipality
		fields = '__all__'