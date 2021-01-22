
from django.shortcuts import render, redirect
from customer.models import Customer
from customer.forms import CustomerForm
# from authenticate import Authentication
# Create your views here.


# @Authentication.is_admin_user
def index(request):
    customers = Customer.objects.all()
    return render(request, "customer/index.html", {'customers': customers})


# @Authentication.is_admin_user
def create(request):
    print(request.POST)
    if request.method == "POST":
        form = CustomerForm(request.POST)
        form.save()
        return redirect("/customer")
    else:
        form = CustomerForm()
    return render(request, "customer/create.html", {'form': form})


# @Authentication.is_admin_user_having_id
def update(request, id):
    customer = Customer.objects.get(id=id)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        form.save()
        return redirect("/customer")
    else:
        form = CustomerForm(instance=customer)
    return render(request, "customer/edit.html", {'form': form})


# @Authentication.is_admin_user_having_id
def delete(request, id):
    customer = Customer.objects.get(id=id)
    customer.delete()
    return redirect("/customer")
