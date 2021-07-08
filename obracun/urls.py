from django.urls import path, include
from . import views

urlpatterns = [
    
    # base ulr

	path('', views.base, name='base'),
    
    # country urls

    path('country', views.country, name='country'),
    path('add_country', views.add_country, name='add_country'),
    path('list_country', views.list_country, name='list_country'),
    path('edit_country/<int:pk>/', views.edit_country, name='edit_country'),
    path('delete_country/<int:pk>/', views.delete_country, name='delete_country'),

    # report urls

    path('testreport', views.testreport, name='testreport'),       
]
