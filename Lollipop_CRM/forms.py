from django.forms import ModelForm

from Lollipop_CRM.models import Customer, Sender, Package


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class SenderForm(ModelForm):
    class Meta:
        model = Sender
        fields = '__all__'


class PackageForm(ModelForm):
    class Meta:
        model = Package
        fields = '__all__'
