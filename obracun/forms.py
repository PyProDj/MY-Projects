from django import forms
from .models import Country, CountryEntity, Municipality, Employee, Contract_type, Contract_duration, Contract, Canton, Contract_annex
from django.contrib.admin.widgets import  AdminDateWidget


class CountryForm(forms.ModelForm):

	country_name = forms.CharField(max_length=100, label= "Naziv države", widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta:
		model = Country
		fields = ['country_name']

class CountryEntityForm(forms.ModelForm):

	entity_name = forms.CharField(max_length=100, label= "Naziv entiteta", widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta:
		model = CountryEntity
		fields = ['entity_name']

class MunicipalityForm(forms.ModelForm):

	municipality_name = forms.CharField(max_length=100, label=' Naziv opštine', widget=forms.TextInput(attrs={'class': 'form-control'}))
	municipality_code = forms.CharField(max_length=3, label='Šifra opštine', widget=forms.TextInput(attrs={'class': 'form-control'}))
	country_entity = forms.ModelChoiceField(label='Entitet', queryset=CountryEntity.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
	country = forms.ModelChoiceField(label='Država', queryset=Country.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
	canton = forms.ModelChoiceField(label='Kanton', queryset=Canton.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))

	class Meta:
		model = Municipality
		fields = '__all__'

class EmployeeForm(forms.ModelForm):

	jmbg = forms.CharField(max_length=13, label='JMBG', widget=forms.TextInput(attrs={'class': 'form-control'}))
	first_name = forms.CharField(max_length=50, label='Ime', widget=forms.TextInput(attrs={'class': 'form-control'}))
	last_name = forms.CharField(max_length=50, label='Prezime', widget=forms.TextInput(attrs={'class': 'form-control'}))
	parent_name = forms.CharField(max_length=50, label='Ime roditelja', widget=forms.TextInput(attrs={'class': 'form-control'}))	
	municipality = forms.ModelChoiceField(label='Opstina', queryset=Municipality.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
	address = forms.CharField(max_length=100, label='Adresa', widget=forms.TextInput(attrs={'class': 'form-control'}))
	prof_qualification = forms.CharField(max_length=100, label='Strucna sprema', widget=forms.TextInput(attrs={'class': 'form-control'}))
	educ_institution = forms.CharField(max_length=100, label='Obrazovna institucija', widget=forms.TextInput(attrs={'class': 'form-control'}))
	prof_title = forms.CharField(max_length=100, label='Zvanje', widget=forms.TextInput(attrs={'class': 'form-control'}))
	year_of_services = forms.DecimalField(max_digits=6, decimal_places=0, label='Radni staz', widget=forms.NumberInput(attrs={'class': 'form-control'}))
	email = forms.EmailField(label='Radni staz', widget=forms.EmailInput(attrs={'class': 'form-control'}))

	class Meta:
		model = Employee
		fields = '__all__'

class ContractTypeForm(forms.ModelForm):

	contract_name = forms.CharField(max_length=100, label='Naziv ugovora', widget=forms.TextInput(attrs={'class': 'form-control'}))
	abbreviation = forms.CharField(max_length=3, label='Skraćenica', widget=forms.TextInput(attrs={'class': 'form-control'}))
	contribution_percent = forms.DecimalField(max_digits=6, decimal_places=2, label='Stopa doprinosa', widget=forms.NumberInput(attrs={'class': 'form-control'}))
	taxe_percent = forms.DecimalField(max_digits=6, decimal_places=2, label='Stopa poreza', widget=forms.NumberInput(attrs={'class': 'form-control'}))
	salary_account = forms.CharField(max_length=10, label='Konto - obaveze za LD', widget=forms.TextInput(attrs={'class': 'form-control'}))
	contribution_account = forms.CharField(max_length=10, label='Konto - obaveze za doprinsoe',widget=forms.TextInput(attrs={'class': 'form-control'}))
	taxe_account = forms.CharField(max_length=10, label='Konto - obaveze za poreze', widget=forms.TextInput(attrs={'class': 'form-control'}))
	solidarity_account = forms.CharField(max_length=10, label='Konto - obaveze za solidarnost', widget=forms.TextInput(attrs={'class': 'form-control'}))
	transport_account = forms.CharField(max_length=10, label='Konto - obaveze za prevoz', widget=forms.TextInput(attrs={'class': 'form-control'}))
	food_account = forms.CharField(max_length=10, label='Konto - obaveze za topli obrok', widget=forms.TextInput(attrs={'class': 'form-control'}))
	cost_bruto_salary_account = forms.CharField(max_length=10, label='Konto - trošak bruto plata', widget=forms.TextInput(attrs={'class': 'form-control'}))
	cost_transport_account = forms.CharField(max_length=10, label='Konto - trošak prevoza', widget=forms.TextInput(attrs={'class': 'form-control'}))
	cost_food_account = forms.CharField(max_length=10, label='Konto - trošak toplog obroka', widget=forms.TextInput(attrs={'class': 'form-control'}))

	class Meta:
		model = Contract_type
		fields = '__all__'

class ContractDurationForm(forms.ModelForm):

	duration = forms.CharField(max_length=100, label= "Trajanje ugovora", widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta:
		model = Contract_duration
		fields = ['duration']

class ContractForm(forms.ModelForm):

	contract_type = forms.ModelChoiceField(label='Tip ugovora', queryset=Contract_type.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
	employee = forms.ModelChoiceField(label='Zaposleni', queryset=Employee.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
	contract_duration = forms.ModelChoiceField(label='Trajanje ugovora', queryset=Contract_duration.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
	contract_number = forms.CharField(label='Broj ugovora',max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
	contract_date = forms.DateField(label='Datum ugovora', widget=forms.DateInput(format='%d.%m.%Y', attrs={"type":"date", "data-date-format":"dd.mm.yyyy", "class":"floater_input form-control", "id":"contract_date", "name":"contract_date"}))
	start_work_date = forms.DateField(label='Datum početka radnog odnosa', widget=forms.DateInput(format='%d.%m.%Y', attrs={"type":"date", "data-date-format":"dd.mm.yyyy", "class":"floater_input form-control", "id":"contract_date", "name":"contract_date"}))
	end_work_date = forms.DateField(label='Prestanak radnog odnosa', required=False, widget=forms.DateInput(format='%d.%m.%Y', attrs={"type":"date", "data-date-format":"dd.mm.yyyy", "class":"floater_input form-control", "id":"contract_date", "name":"contract_date"}))
	salary = forms.DecimalField(label='Ugovorena plata prije oporezivanja', max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control'}))


	class Meta:
		model = Contract
		fields = ['contract_type', 'employee', 'contract_duration', 'contract_number', 'contract_date', 'start_work_date', 'end_work_date', 'salary']


class ContractAnnexForm(forms.ModelForm):

	contract = forms.ModelChoiceField(label='Tip ugovora', queryset=Contract.objects.all(), widget=forms.Select(attrs={'class': 'form-select', 'disabled': 'disabled'}))
	annex_date = forms.DateField(label='Datum aneksa', widget=forms.DateInput(format='%d.%m.%Y', attrs={"type":"date", "data-date-format":"dd.mm.yyyy", "class":"floater_input form-control", "id":"contract_date", "name":"contract_date"}))
	annex_number = forms.CharField(label='Broj aneksa',max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
	contract_duration = forms.ModelChoiceField(label='Trajanje ugovora', queryset=Contract_duration.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
	end_work_date = forms.DateField(label='Datum isteka ugovora', widget=forms.DateInput(format='%d.%m.%Y', attrs={"type":"date", "data-date-format":"dd.mm.yyyy", "class":"floater_input form-control", "id":"contract_date", "name":"contract_date"}))
	salary = forms.DecimalField(label='Ugovorena plata prije oporezivanja', max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control'}))


	class Meta:
		model = Contract_annex
		fields = ['contract', 'annex_date', 'annex_number', 'contract_duration','end_work_date', 'salary']