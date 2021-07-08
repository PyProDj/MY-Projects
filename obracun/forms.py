from django import forms
from .models import Country, CountryEntity

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