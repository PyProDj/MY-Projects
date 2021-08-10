from django.shortcuts import render, redirect
from .forms import CountryForm, CountryEntityForm, MunicipalityForm, EmployeeForm, ContractTypeForm, ContractDurationForm, ContractForm, ContractAnnexForm
from .models import Country, CountryEntity, Contract, Canton, Municipality, Employee, Contract_type, Contract_duration, Contract,Contract_annex
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, JsonResponse
import json
from django.core import serializers
from plate.utils import render_to_pdf
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
import datetime

from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic import DetailView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def base(request):
	return render(request, 'base.html')

def test(request):
	return render(request, 'test.html')


# =====//--COUNTRY--\\=====


class CountryAdd(CreateView):
	model = Country
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
	form_class = CountryEntityForm
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


# =====//--Municipality--\\=====


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
	template_name = 'municipality_detail.html'
	context_object_name = 'municipality'
	slug_field = 'id'

class MunicipalityEdit(UpdateView):
	model = Municipality
	fields = ['municipality_name', 'municipality_code', 'country_entity', 'country', 'canton']
	template_name = 'add_form.html'

class MunicipalityDelete(DeleteView):
	model = Municipality
	success_url = reverse_lazy('list_municipality')
	template_name = 'delete.html'


# =====//--Employee--\\=====


class EmployeeAdd(CreateView):
	model = Employee
	# fields = ['municipality_name', 'municipality_code', 'country_entity', 'country', 'canton']
	template_name = 'add_form.html'
	form_class = EmployeeForm

class EmployeeList(ListView):

	model = Employee
	context_object_name = 'employees'
	queryset = Employee.objects.all()
	template_name = 'list_employee.html'  

class EmployeeDetail(DetailView):
	model = Employee
	template_name = 'employee_detail.html'
	context_object_name = 'employee'
	slug_field = 'id'

class EmployeeEdit(UpdateView):
	model = Employee
	fields = ['jmbg', 'first_name', 'last_name', 'parent_name', 'municipality', 'address', 'prof_qualification', 'educ_institution', 'prof_title', 'year_of_services', 'email']
	template_name = 'add_form.html'

class EmployeeDelete(DeleteView):
	model = Employee
	success_url = reverse_lazy('list_employee')
	template_name = 'delete.html'


# =====//--Coontract type--\\=====


class ContractTypeAdd(CreateView):
	model = Contract_type
	# fields = ['municipality_name', 'municipality_code', 'country_entity', 'country', 'canton']
	template_name = 'add_form.html'
	form_class = ContractTypeForm

class ContractTypeList(ListView):

	model = Contract_type
	context_object_name = 'contract_type'
	queryset = Contract_type.objects.all()
	template_name = 'list_contract_type.html'  

class ContractTypeDetail(DetailView):
	model = Contract_type
	template_name = 'contract_type_detail.html'
	context_object_name = 'contract_type'
	slug_field = 'id'

class ContractTypeEdit(UpdateView):
	model = Contract_type
	fields = ['contract_name', 'abbreviation', 'contribution_percent', 'taxe_percent', 'salary_account', 'contribution_account', 'taxe_account', 'solidarity_account', 'transport_account', 'food_account', 'cost_bruto_salary_account', 'cost_transport_account', 'cost_food_account']
	template_name = 'add_form.html'

class ContractTypeDelete(DeleteView):
	model = Contract_type
	success_url = reverse_lazy('list_contract_type')
	template_name = 'delete.html'

# =====//--Contract duration--\\=====


class ContractDurationAdd(CreateView):
	model = Contract_duration
	template_name = 'add_form.html'
	form_class = ContractDurationForm

class ContractDurationList(ListView):

	model = Contract_duration
	context_object_name = 'contract_duration'
	queryset = Contract_duration.objects.all()
	template_name = 'list_contract_duration.html'  

class ContractDurationEdit(UpdateView):
	model = Contract_duration
	fields = ['duration']
	template_name = 'add_form.html'

class ContractDurationDelete(DeleteView):
	model = Contract_duration
	success_url = reverse_lazy('list_contract_duration')
	template_name = 'delete.html'

# =====//--Contract--\\=====


class ContractAdd(SuccessMessageMixin, CreateView):
	model = Contract
	# fields = ['municipality_name', 'municipality_code', 'country_entity', 'country', 'canton']
	template_name = 'add_form.html'
	form_class = ContractForm
	success_message = 'Ugovor je uspješno dodat'
	error_meesage = "Ugovor nije dodat! Pokušajte ponovo!"

class ContractList(ListView):

	model = Contract
	context_object_name = 'contracts'
	queryset = Contract.objects.all()
	template_name = 'list_contract.html'  


# =====//--Contract anex--\\=====



class ContractAnnexAdd(SuccessMessageMixin, CreateView):
	model = Contract_annex
	# fields = ['municipality_name', 'municipality_code', 'country_entity', 'country', 'canton']
	template_name = 'add_form.html'
	form_class = ContractAnnexForm
	success_message = 'Ugovor je uspješno dodat'
	error_meesage = "Ugovor nije dodat! Pokušajte ponovo!"

	def form_valid(self, form):
		form.instance.contractid = request.POST.get('id')
		return super(ContractAnnexAdd, self).form_valid(form)

# def ContractAnnexAdd(request, contractid):
# 	contract = Contract.objects.all(id=contractid)
# 	form = ContractAnnexForm(instance=contract)
	



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