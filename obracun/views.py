from django.shortcuts import render, redirect
from .forms import CountryForm, CountryEntityForm, MunicipalityForm
from .models import Country, CountryEntity, Contract, Canton, Municipality
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, JsonResponse
import json
from django.core import serializers
from plate.utils import render_to_pdf
from django.views.generic import View
from django.contrib import messages
import datetime
from django.core.paginator import Paginator

from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def base(request):
	return render(request, 'base.html')

def test(request):
	return render(request, 'test.html')


# =====//--COUNTRY--\\=====


class CountryAdd(CreateView):
	model = Country
	fields = ['country_name']
	template_name = 'add_form.html'
	form_class = CountryForm

class CountryList(ListView):

	model = Country
	# paginate_by = 50
	context_object_name = 'countries'
	queryset = Country.objects.all()
	template_name = 'list_country.html'  

class CountryDetail(DetailView):
	model = Country
	template_name = 'country_details.html'
	context_object_name = 'country'
	slug_field = 'id'

class CountryEdit(UpdateView):
	model = Country
	fields = ['country_name']
	template_name = 'add_form.html'

class CountryDelete(DeleteView):
	model = Country
	success_url = reverse_lazy('list_country')
	template_name = 'delete.html'


# =====//--COUNTRY-ENTITIY--\\=====


class CountryEntityAdd(CreateView):
	model = CountryEntity
	fields = ['entity_name']
	template_name = 'add_form.html'

class CountryEntityList(ListView):

	model = CountryEntity
	context_object_name = 'entities'
	queryset = CountryEntity.objects.all()
	template_name = 'list_countryentity.html'  

class CountryEntityDetail(DetailView):
	model = CountryEntity
	template_name = 'countryentity_detail.html'
	context_object_name = 'entities'
	slug_field = 'id'

class CountryEntityEdit(UpdateView):
	model = CountryEntity
	fields = ['entity_name']
	template_name = 'add_form.html'

class CountryEntityDelete(DeleteView):
	model = CountryEntity
	success_url = reverse_lazy('list_countryentity')
	template_name = 'delete.html'

# =====//--CANTON--\\=====


class CantonAdd(CreateView):
	model = Canton
	fields = ['canton_name']
	template_name = 'add_form.html'

class CantonList(ListView):

	model = Canton
	context_object_name = 'cantons'
	queryset = Canton.objects.all()
	template_name = 'list_canton.html'  

class CantonDetail(DetailView):
	model = Canton
	template_name = 'canton_detail.html'
	context_object_name = 'cantons'
	slug_field = 'id'

class CantonEdit(UpdateView):
	model = Canton
	fields = ['canton_name']
	template_name = 'add_form.html'

class CantonDelete(DeleteView):
	model = Canton
	success_url = reverse_lazy('list_countryentity')
	template_name = 'delete.html'


# =====//--CANTON--\\=====


class MunicipalityAdd(CreateView):
	model = Municipality
	# nije dozvoljeno koristenje fields i forms_class, jer je u koviru form_class vec izdefinisan fields
	# fields = ['municipality_name', 'municipality_code', 'country_entity', 'country', 'canton']
	template_name = 'add_form.html'
	form_class = MunicipalityForm

class MunicipalityList(ListView):

	model = Municipality
	context_object_name = 'municipalities'
	queryset = Municipality.objects.all()
	template_name = 'list_municipality.html'  

class MunicipalityDetail(DetailView):
	model = Municipality
	template_name = 'canton_detail.html'
	context_object_name = 'cantons'
	slug_field = 'id'

class MunicipalityEdit(UpdateView):
	model = Municipality
	fields = ['municipality_name', 'municipality_code', 'country_entity', 'country', 'canton']
	template_name = 'add_form.html'

class MunicipalityDelete(DeleteView):
	model = Municipality
	success_url = reverse_lazy('list_municipality')
	template_name = 'delete.html'


# =====//--PDF reports--\\==== 

def testreport(request):
	countries = Country.objects.all()
	count_countries = countries.count()
	context = {
		'countries': countries,
		'count_countries': count_countries,
		}
	pdf = render_to_pdf('reports/test.html', context)
	return HttpResponse(pdf, content_type='application/pdf')