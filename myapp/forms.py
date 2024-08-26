from django import forms
from .models import BusinessDetails

class BusinessDetailsForm(forms.ModelForm):
    class Meta:
        model = BusinessDetails
        fields = [
            'received_on', 'organization_date', 'assigned_on', 'completed_on',
             'batch_type', 'order_no', 'borrower_name_1', 'borrower_name_2',
            'address', 'state', 'country', 'loan_amount', 'product', 'status',
            'processor_name', 'typing', 'completed_on', 'order', 'acer'
        ]
        widgets = {
            'received_on': forms.DateInput(attrs={'class': 'form-control datepicker', 'type': 'date'}),
            'organization_date': forms.DateInput(attrs={'class': 'form-control datepicker', 'type': 'date'}),
            'assigned_on': forms.DateInput(attrs={'class': 'form-control datepicker', 'type': 'date'}),
            'completed_on': forms.DateInput(attrs={'class': 'form-control datepicker', 'type': 'date'}),
            #'sl': forms.TextInput(attrs={'class': 'form-control'}),
            'batch_type': forms.TextInput(attrs={'class': 'form-control'}),
            'order_no': forms.TextInput(attrs={'class': 'form-control'}),
            'borrower_name_1': forms.TextInput(attrs={'class': 'form-control'}),
            'borrower_name_2': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'loan_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'product': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'processor_name': forms.TextInput(attrs={'class': 'form-control'}),
            'typing': forms.TextInput(attrs={'class': 'form-control'}),
            'order': forms.TextInput(attrs={'class': 'form-control'}),
            'acer': forms.TextInput(attrs={'class': 'form-control'}),
        }
