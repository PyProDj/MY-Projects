from django.shortcuts import render, redirect
from .forms import CountryForm, CountryEntityForm
from .models import Country, CountryEntity
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, JsonResponse
import json
from django.core import serializers
from plate.utils import render_to_pdf
from django.views.generic import View
from django.contrib import messages


def base(request):
	return render(request, 'base.html')

# =====//--COUNTRY--\\=====

def country(request):
	return render(request, 'country.html')

def add_country(request):
	form = CountryForm(request.POST)
	if form.is_valid():
		form.save()
		form = CountryForm()
		return redirect('list_country')
	context = {
		'form': form
	}
	return render(request, 'add_country.html', context)

def list_country (request):

	countries_list = []
 
	for country in Country.objects.all().order_by('country_name'):
		countries_list.append({'country_name': country.country_name})

	data = json.dumps(countries_list)
	return HttpResponse(data)


def edit_country(request, pk):
	template_name = 'cepy/add_country_form.html'
	countries = Country.objects.get(id=pk)
	form = CountryForm(instance=countries)
	if request.method == 'POST':
		form = CountryForm(request.POST, instance=countries)
		if form.is_valid():
			form.save()
			messages.success(request, "Odlicno")
			return redirect('/country')
		else:
			messages.error(request, "Ovo je greska sve joj jebem")
	context = {
		"form": form
	}
	return render(request, "add_country.html", context)

def delete_country (request, pk):
	countries = Country.objects.get(id=pk)
		
	if request.method == 'POST':
		countries.delete()
		return redirect('/list_country')

	context = {
		'countries': countries
		}
	return render(request, "delete.html", context)



def add_countryentity(request):
	form = CountryForm(request.POST)
	if form.is_valid():
		form.save()
		form = CountryForm()
		return redirect('list_country')
	context = {
		'form': form
	}
	return render(request, 'add_country.html', context)

def list_countryentity (request):
	countries_list = CountryEntity.objects.all()
	page = request.GET.get('page', 1)

	paginator = Paginator(countries_list, 10)
	try:
		countries = paginator.page(page)
	except PageNotAnInteger:
		countries = paginator.page(1)
	except EmptyPage:
		countries = paginator.page(paginator.num_pages)

	index = countries.number - 1  
	max_index = len(paginator.page_range)
	start_index = index - 3 if index >= 3 else 0
	end_index = index + 3 if index <= max_index - 3 else max_index
	page_range = list(paginator.page_range)[start_index:end_index]


	context = {
		'countries': countries,
		'page_range': page_range
	}
	return render (request, 'list_country.html', context)

def edit_countryentity(request, pk):
	template_name = 'cepy/add_country_form.html'
	country = Country.objects.get(id=pk)
	form = CountryForm(instance=country)
	if request.method == 'POST':
		form = CountryForm(request.POST, instance=country)
		if form.is_valid():
			form.save()
			messages.success(request, "Odlicno")
			return redirect('/list_country')
		else:
			messages.error(request, "Ovo je greska sve joj jebem")
	context = {
		"form": form
	}
	return render(request, "add_country.html", context)

def delete_countryentity (request, pk):
	countries = Country.objects.get(id=pk)
		
	if request.method == 'POST':
		countries.delete()
		return redirect('/list_country')

	context = {
		'countries': countries
		}
	return render(request, "delete.html", context)

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