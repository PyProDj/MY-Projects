from django.urls import path, include
from . import views

urlpatterns = [
    
    # base ulr

	path('', views.base, name='base'),
    path('test', views.test, name='test'),
    
    # country urls

    # path('country', views.country, name='country'),
    path('add_country', views.CountryAdd.as_view(), name='add_country'),
    path('list_country', views.CountryList.as_view(), name='list_country'),
    path('detail_country/<int:pk>/', views.CountryDetail.as_view(), name='detail_country'),
    path('edit_country/<int:pk>/', views.CountryEdit.as_view(), name='edit_country'),
    path('delete_country/<int:pk>/', views.CountryDelete.as_view(), name='delete_country'),

    # countryentity urls

    path('add_countryentity', views.CountryEntityAdd.as_view(), name='add_countryentity'),
    path('list_countryentity', views.CountryEntityList.as_view(), name='list_countryentity'),
    path('detail_countryentity/<int:pk>/', views.CountryEntityDetail.as_view(), name='detail_countryentity'),
    path('edit_countryentity/<int:pk>/', views.CountryEntityEdit.as_view(), name='edit_countryentity'),
    path('delete_countryentity/<int:pk>/', views.CountryEntityDelete.as_view(), name='delete_countryentity'),

    # canton urls

    path('add_canton', views.CantonAdd.as_view(), name='add_canton'),
    path('list_canton', views.CantonList.as_view(), name='list_canton'),
    path('detail_canton/<int:pk>/', views.CantonDetail.as_view(), name='detail_canton'),
    path('edit_canton/<int:pk>/', views.CantonEdit.as_view(), name='edit_canton'),
    path('delete_canton/<int:pk>/', views.CantonDelete.as_view(), name='delete_canton'),

    # municipality urls

    path('add_municipality', views.MunicipalityAdd.as_view(), name='add_municipality'),
    path('list_municipality', views.MunicipalityList.as_view(), name='list_municipality'),
    path('detail_municipality/<int:pk>/', views.MunicipalityDetail.as_view(), name='detail_municipality'),
    path('edit_municipality/<int:pk>/', views.MunicipalityEdit.as_view(), name='edit_municipality'),
    path('delete_municipality/<int:pk>/', views.MunicipalityDelete.as_view(), name='delete_municipality'),


    # employee urls

    path('add_employee', views.EmployeeAdd.as_view(), name='add_employee'),
    path('list_employee', views.EmployeeList.as_view(), name='list_employee'),
    path('detail_employee/<int:pk>/', views.EmployeeDetail.as_view(), name='detail_employee'),
    path('edit_employee/<int:pk>/', views.EmployeeEdit.as_view(), name='edit_employee'),
    path('delete_employee/<int:pk>/', views.EmployeeDelete.as_view(), name='delete_employee'),

    # country type urls

    path('add_contract_type', views.ContractTypeAdd.as_view(), name='add_contract_type'),
    path('list_contract_type', views.ContractTypeList.as_view(), name='list_contract_type'),
    path('detail_contract_type/<int:pk>/', views.ContractTypeDetail.as_view(), name='detail_contract_type'),
    path('edit_contract_type/<int:pk>/', views.ContractTypeEdit.as_view(), name='edit_contract_type'),
    path('delete_contract_type/<int:pk>/', views.ContractTypeDelete.as_view(), name='delete_contract_type'),

    # country type urls

    path('add_contract_duration', views.ContractDurationAdd.as_view(), name='add_contract_duration'),
    path('list_contract_duration', views.ContractDurationList.as_view(), name='list_contract_duration'),
    path('edit_contract_duration/<int:pk>/', views.ContractDurationEdit.as_view(), name='edit_contract_duration'),
    path('delete_contract_duration/<int:pk>/', views.ContractDurationDelete.as_view(), name='delete_contract_duration'),

    # country urls

    path('add_contract', views.ContractAdd.as_view(), name='add_contract'),
    path('list_contract', views.ContractList.as_view(), name='list_contract'),

    # country annex urls

    path('add_contractannex', views.ContractAnnexAdd.as_view(), name='add_contractannex'),
    # path('list_contract', views.ContractList.as_view(), name='list_contract'),

    # report urls

    path('testreport', views.testreport, name='testreport'),       
]
