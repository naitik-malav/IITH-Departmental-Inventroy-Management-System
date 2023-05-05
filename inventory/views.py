from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
from .models import InventoryModel
from .forms import InventoryForm
# Create your views here.


def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            request.session.set_expiry(86400)
            login(request, user)
            return HttpResponseRedirect(reverse('index'))

        else:
            return render(request, 'inventory/signin_page.html', {
                'not_authenticated': True
            })
    elif request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'inventory/signin_page.html')


def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('sign-in'))


def sign_up(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        existing_user = False
        invalid_request = False
        new_user = False
        if User.objects.filter(username=username):
            existing_user = True
            return render(request, 'inventory/signup_page.html', {
                'existing_user': existing_user
            })

        elif username == '' or password == '':
            invalid_request = True
            return render(request, 'inventory/signup_page.html', {
                'invalid_request': invalid_request
            })

        else:
            new_user = True
            User.objects.create_user(
                username=username,
                password=password
            )
            return render(request, 'inventory/signup_page.html', {
                'new_user': new_user
            })
    else:
        return render(request, 'inventory/signup_page.html')


@login_required
def index(request):
    model = InventoryModel.objects.all()
    return render(request, 'inventory/index.html', {
        'model': model
    })

@login_required
def search(request):
        query = request.GET.get('q')
        results = InventoryModel.objects.filter(Q(Name__contains=query) | Q(InvoiceNo__contains=query) | Q(PurchasingDate__contains=query))
        context = {'results': results}
        return render(request, 'inventory/search.html', context)

@login_required
def add_item(request):
    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            Name = form.cleaned_data['Name']
            Quantity = form.cleaned_data['Quantity']
            Description = form.cleaned_data['Description']
            InvoiceNo = form.cleaned_data['InvoiceNo']
            Warranty = form.cleaned_data['Warranty']
            Price = form.cleaned_data['Price']
            Department = form.cleaned_data['Department']
            PurchasingDate = form.cleaned_data['PurchasingDate']

            if InventoryModel.objects.filter(Name=Name):
                return render(request, 'inventory/add_item.html', {
                    'form': InventoryForm,
                    'sku_present': True
                })
            else:
                model = InventoryModel(Name=Name, Quantity=Quantity, Description=Description, InvoiceNo=InvoiceNo, Warranty=Warranty, Price=Price, Department=Department, PurchasingDate=PurchasingDate)
                model.save()
                return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'inventory/add_item.html', {
            'form': InventoryForm
        })
