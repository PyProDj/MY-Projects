from django.test import TestCase


# prikazi koje sma koristio ali mi trenutno samo smetaju
# ovjdje sam ih izmjestio da mi je views.py cistiji sa kodom 
# def country(request):
# 	return render(request, 'country.html')

# # def add_country(request):
# # 	form = CountryForm(request.POST)
# # 	if form.is_valid():
# # 		form.save()
# # 		form = CountryForm()
# # 		return redirect('list_country')
# # 	context = {
# # 		'form': form
# # 	}
# # 	return render(request, 'add_country.html', context)

# def list_country (request):

# 	countries_list = []
 
# 	for country in Country.objects.all().order_by('country_name'):
# 		countries_list.append({'country_name': country.country_name})

# 	paginator = Paginator(countries_list, 25)
# 	page_number = request.GET.get('page')
# 	countries = paginator.get_page(page_number)
	
# 	context = {
# 		'countries': countries,
# 	}

# 	# data = json.dumps(context)
	
# 	return render(request, 'list_country.html', context)


# def edit_country(request, pk):
# 	template_name = 'cepy/add_country_form.html'
# 	countries = Country.objects.get(id=pk)
# 	form = CountryForm(instance=countries)
# 	if request.method == 'POST':
# 		form = CountryForm(request.POST, instance=countries)
# 		if form.is_valid():
# 			form.save()
# 			messages.success(request, "Odlicno")
# 			return redirect('/country')
# 		else:
# 			messages.error(request, "Ovo je greska sve joj jebem")
# 	context = {
# 		"form": form
# 	}
# 	return render(request, "add_country.html", context)

# def delete_country (request, pk):
	
# 	countries = Country.objects.get(id=pk)
		
# 	if request.method == 'POST':
# 		countries.delete()
# 		return redirect('/list_country')

# 	context = {
# 		'countries': countries
# 		}
# 	return render(request, "list_country.html", context)

