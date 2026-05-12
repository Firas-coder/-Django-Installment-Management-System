from django.contrib import messages

from django.shortcuts import redirect, render
from .forms import CustomerForm
from .models import Customer
# Create your views here.
def add_customer(request):
    formCustomer = CustomerForm()
    if request.method == 'POST':
        formCustomer = CustomerForm(request.POST)
        if formCustomer.is_valid():
            formCustomer.save() 
            return redirect('search_customer') 
    return render(request, 'pages/add_customer.html', {'form': formCustomer})

def search_customer(request):
    customers = Customer.objects.all()  # قيمة افتراضية
    
    if request.method == 'GET':
        q = request.GET.get('q')  # نص + تنظيف المسافات
        if q:
            customers = Customer.objects.filter(name__icontains=q)
        else:
            messages.error(request, 'Invalid search query')
    
    return render(request, 'pages/search_customer.html', {'customers': customers})

def edit_customer(request,customer_id):
    customer = Customer.objects.get(id=customer_id)
    formCustomer = CustomerForm(instance=customer)
    if request.method == 'POST':
        formCustomer = CustomerForm(request.POST, instance=customer)
        if formCustomer.is_valid():
            formCustomer.save()
            return redirect('search_customer') 
    return render(request, 'pages/edit_customer.html', {'form': formCustomer})
from django.shortcuts import get_object_or_404, render

def print_customer_receipt(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    return render(request, 'pages/receipt_print.html', {'customer': customer})