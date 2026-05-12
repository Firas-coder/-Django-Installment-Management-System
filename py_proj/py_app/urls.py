from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.add_customer, name='add_customer'),
    path('search/', views.search_customer, name='search_customer'),
    path('edit/<int:customer_id>/', views.edit_customer, name='edit_customer'),
    path('receipt/<int:customer_id>/', views.print_customer_receipt, name='print_receipt'),
]
