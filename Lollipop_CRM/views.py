from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from Lollipop_CRM.forms import CustomerForm, SenderForm, PackageForm
from Lollipop_CRM.models import Customer, Sender, Package


def auth_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['userpassword']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/crm/create/package/')
        else:
            messages.error(request, 'Invalid username/password')

    form = AuthenticationForm()
    context = {
        'form': form
    }

    return render(request, 'auth/auth-login.html', context=context)


@login_required(login_url='/crm/accounts/login/')
def add_customer(request):
    if request.method == "POST":
        form = CustomerForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer added successfully")
        else:
            messages.error(request, "Oops! an error occurred")
            print(form.errors)
    return render(request, template_name='CRM/add-customers.html')


@login_required(login_url='/crm/accounts/login/')
def auth_logout(request):
    logout(request)
    return redirect('/crm/accounts/login/')


@login_required(login_url='/crm/accounts/login/')
def view_customer(request):
    customers = Customer.objects.all()

    context = {
        'customers': customers
    }

    return render(request, template_name='CRM/view-customers.html', context=context)


@login_required(login_url='/crm/accounts/login/')
def create_package(request):
    if request.method == "POST":
        sender = Sender.objects.create(
            sender_name=request.POST.get("sender_name"),
            sender_phone_number=request.POST.get("sender_phone_number"),
            sender_company=request.POST.get("sender_company"),
            sender_address=request.POST.get("sender_address"),
            sender_zip=request.POST.get("sender_zip"),
            sender_city=request.POST.get("sender_city"),
            sender_email_address=request.POST.get("sender_email_address"))

        receiver = Customer.objects.create(
            customer_name=request.POST.get("customer_name"),
            phone_number=request.POST.get("phone_number"),
            company=request.POST.get("company"),
            address=request.POST.get("address"),
            customer_zip=request.POST.get("customer_zip"),
            city=request.POST.get("city"),
            email_address=request.POST.get("email_address"))

        package = Package.objects.create(
            package_number=request.POST.get("package_number"),
            package_weight=request.POST.get("package_weight"),
            package_length=request.POST.get("package_length"),
            package_width=request.POST.get("package_width"),
            package_height=request.POST.get("package_height"),
            package_content=request.POST.get("package_content"),
            package_value=request.POST.get("package_value"),
            package_packaging=request.POST.get("package_packaging"),
            package_ref=request.POST.get("package_ref"),
            package_note=request.POST.get("package_note"),
            package_remarks=request.POST.get("package_remarks"),
            package_billing=request.POST.get("package_billing"),
            sender=sender,
            receiver=receiver
        )

        sender.save()
        receiver.save()
        package.save()

    return render(request, template_name='packages/create-package.html')


@login_required(login_url='/crm/accounts/login/')
def view_package(request):
    all_packages = Package.objects.all()
    context = {
        'all_packages': all_packages
    }

    return render(request, template_name='packages/view-packages.html', context=context)


@login_required(login_url='/crm/accounts/login/')
def package_label(request, package_number=None):
    package_details = Package.objects.filter(package_number=package_number)
    context = {
        'package_details': package_details
    }
    return render(request, template_name="CRM/label.html", context=context)
