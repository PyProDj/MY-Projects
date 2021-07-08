from django.contrib import admin
from .models import Country, CountryEntity, Canton, Municipality, Employee, Contract_type, Contract_duration, Contract, Contract_annex, Payroll

admin.site.register(Country)
admin.site.register(CountryEntity)
admin.site.register(Canton)
admin.site.register(Municipality)
admin.site.register(Employee)
admin.site.register(Contract_type)
admin.site.register(Contract_duration)
admin.site.register(Contract)
admin.site.register(Contract_annex)
admin.site.register(Payroll)