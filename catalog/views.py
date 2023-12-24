from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Catalog


def catalog_table(request):
    prods = Catalog.objects.all()
    return render(request, "home.html", {'prods': prods})


def add_column(request):
    prods = Catalog.objects.all()
    return render(request, "add_column.html", {'prods': prods})


def insert_into_table(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        value = request.POST.get('value')
        price = request.POST.get('price')
        total = float(value) * float(price)

        if not Catalog.objects.filter(name=name).exists():
            Catalog.objects.create(name=name, value=value, price=price, total=total)
            messages.success(request, 'Product added successfully')
        else:
            messages.warning(request,
                             f'The product "{name}" already exists in the table, '
                             f'if you want to change product, please choose "change column" button')

    return redirect('home')


def pop(request):
    prods = Catalog.objects.all()
    return render(request, "pop.html", {'prods': prods})


def pop_column(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if Catalog.objects.filter(name=name).exists():
            Catalog.objects.filter(name=name).delete()
            messages.success(request, 'Product deleted successfully')
        else:
            messages.warning(request, f'The product "{name}" does not exist in the table')
        return redirect('home')


def change(request):
    prods = Catalog.objects.all()
    return render(request, "change.html", {'prods': prods})


def change_table(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        new_name = request.POST.get('new_name')
        value = request.POST.get('value')
        price = request.POST.get('price')
        if Catalog.objects.filter(name=name).exists():
            Catalog.objects.filter(name=name).update(name=new_name, value=value, price=price)
            messages.success(request, 'Product changed successfully')
        else:
            messages.warning(request, f'The product "{name}" does not exist in the table')
        return redirect('home')
