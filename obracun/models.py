from django.db import models
from django.urls import reverse
from django.utils import timezone


class Country(models.Model):

	country_name = models.CharField(max_length=100)

	def __str__(self):
		return self.country_name

	def get_absolute_url(self):
		return reverse('list_country')

class CountryEntity(models.Model):

	entity_name = models.CharField(max_length=100)

	def __str__(self):
		return self.entity_name

	def get_absolute_url(self):
		return reverse('list_countryentity')

class Canton(models.Model):

	canton_name = models.CharField(max_length=100)

	def __str__(self):
		return self.canton_name

	def get_absolute_url(self):
		return reverse('list_canton')

class Municipality(models.Model):

	municipality_name = models.CharField(max_length=100)
	municipality_code = models.CharField(max_length=3)

	country_entity = models.ForeignKey(CountryEntity, on_delete=models.SET_NULL, null=True)
	country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
	canton = models.ForeignKey(Canton, on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return self.municipality_name

	def get_absolute_url(self):
		return reverse('list_municipality')

class Employee(models.Model):

	jmbg = models.CharField(max_length=13, unique=True, error_messages={'unique':"Matični broj već postoji u bazi."})
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	parent_name = models.CharField(max_length=50)	
	municipality = models.ForeignKey(Municipality, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=100)
	prof_qualification = models.CharField(max_length=100)
	educ_institution = models.CharField(max_length=100)
	prof_title = models.CharField(max_length=100)
	year_of_services = models.DecimalField(max_digits=6, decimal_places=0)
	email = models.EmailField(null=True)

	def __str__(self):
		return '{} ({}) {} [{}]'.format(self.first_name, self.parent_name, self.last_name, self.jmbg)

	def get_absolute_url(self):
		return reverse('list_employee')


class Contract_type(models.Model):

	contract_name = models.CharField(max_length=100)
	abbreviation = models.CharField(max_length=3, unique=True)
	contribution_percent = models.DecimalField(max_digits=6, decimal_places=2)
	taxe_percent = models.DecimalField(max_digits=6, decimal_places=2)
	salary_account = models.CharField(max_length=10)
	contribution_account = models.CharField(max_length=10)
	taxe_account = models.CharField(max_length=10)
	solidarity_account = models.CharField(max_length=10)
	transport_account = models.CharField(max_length=10)
	food_account = models.CharField(max_length=10)
	cost_bruto_salary_account = models.CharField(max_length=10)
	cost_transport_account = models.CharField(max_length=10)
	cost_food_account = models.CharField(max_length=10)

	def __str__(self):
		return self.contract_name

	def get_absolute_url(self):
		return reverse('list_contract_type')

class Contract_duration(models.Model):

	duration = models.CharField(max_length=20)

	def __str__(self):
		return self.duration

	def get_absolute_url(self):
		return reverse('list_contract_duration')

class Contract(models.Model):

	contract_type = models.ForeignKey(Contract_type, on_delete=models.SET_NULL, null=True)
	employee = models.OneToOneField(Employee, on_delete=models.CASCADE, null=True)
	contract_duration = models.ForeignKey(Contract_duration, on_delete=models.SET_NULL, null=True)
	contract_number = models.CharField(max_length=15, unique=True)
	contract_date = models.DateField()
	start_work_date = models.DateField()
	end_work_date = models.DateField(null=True, blank=True)
	# work_time = models.DateTimeField()
	salary = models.DecimalField(max_digits=10, decimal_places=2)
	active_status = models.BooleanField(default=True)
	DisplayField = ['contract_type', 'employee', 'period']

	# @property
	def period(self):
		if contract_date != None:
			period = start_work_date - end_work_date
		return period

	def __str__(self):
		return "Ugovor broj: " + self.contract_number + " Radnik: " + str(self.employee)

	def get_absolute_url(self):
		return reverse('base')

class Contract_annex(models.Model):

	contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
	annex_date = models.DateField(default=timezone.now)
	annex_number = models.CharField(max_length=15)
	contract_duration = models.ForeignKey(Contract_duration, on_delete=models.SET_NULL, null=True)
	end_work_date = models.DateField(null=True, blank=True)
	salary = models.DecimalField(max_digits=10, decimal_places=2, null=True)

	def get_absolute_url(self):
		return reverse('base')

# Obracun plata / plan je sa se u samoj bazi nalazi podatak o ugovorenoj plati
#porezima i doprinosima sumarno, a onda da se u izvjestajima prikazuje zasebno

class Payroll(models.Model):

	contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
	year = models.DecimalField(max_digits=4, decimal_places=0)
	payroll_date = models.DateField()
	payroll_of_date = models.DateField()
	payroll_to_date = models.DateField()
	worked_days = models.DecimalField(max_digits=6, decimal_places=2)
	salary = models.DecimalField(max_digits=6, decimal_places=2)
	net_salary = models.DecimalField(max_digits=6, decimal_places=2)
	gross_salary = models.DecimalField(max_digits=6, decimal_places=2)
	contributions = models.DecimalField(max_digits=6, decimal_places=2)
	taxe = models.DecimalField(max_digits=6, decimal_places=2)
	contributions_health = models.DecimalField(max_digits=6, decimal_places=2)
	contributions_unemployment = models.DecimalField(max_digits=6, decimal_places=2)
	contributions_child = models.DecimalField(max_digits=6, decimal_places=2)
