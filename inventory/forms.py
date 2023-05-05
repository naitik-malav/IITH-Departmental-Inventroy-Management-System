from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column, Button

from .models import InventoryModel


class InventoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_action = ''
        self.helper.add_input(Submit('submit', 'Save', css_class='mt-2 btn btn-dark'))
        self.helper.add_input(Button('cancel', 'Cancel', onclick="location.href = '/index/'", css_class='ms-3 mt-2 btn btn-dark'))
        self.helper.layout = Layout(
            Row(
                Column('Name', css_class='mt-4'),
                Column('Quantity', css_class='mt-4'),
                Column('Description', css_class='mt-4'),
                Column('Department', css_class='mt-4'),
                Column('Price', css_class='mt-4'),
                Column('InvoiceNo', css_class='mt-4'),
                Column('PurchasingDate', css_class='mt-4'),
                Column('Warranty', css_class='mt-4'),
            )
        )

    class Meta:
        model = InventoryModel
        fields = '__all__'
        labels = {
            'Name': 'Name',
            'Quantity': 'Quantity',
            'Description': 'Description',
            'InvoiceNo': 'InvoiceNo',
            'Warranty': 'Warranty',
            'Price': 'Price',
            'Department': 'Department',
            'PurchasingDate': 'PurchasingDate',
            }
            