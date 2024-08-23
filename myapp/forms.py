from django import forms
from .models import BusinessDetails

class BusinessDetailsForm(forms.ModelForm):
    class Meta:
        model = BusinessDetails
        fields = [
            'received_on', 'organization_date', 'assigned_on', 'completed_on', 
            'sl', 'batch_type', 'order_no', 'borrower_name_1', 'borrower_name_2', 
            'address', 'state', 'country', 'loan_amount', 'product', 'status', 
            'processor_name', 'typing', 'order', 'acer'
        ]
        widgets = {
            'received_on': forms.DateInput(attrs={'class': 'form-control datepicker', 'type': 'date'}),
            'organization_date': forms.DateInput(attrs={'class': 'form-control datepicker', 'type': 'date'}),
            'assigned_on': forms.DateInput(attrs={'class': 'form-control datepicker', 'type': 'date'}),
            'completed_on': forms.DateInput(attrs={'class': 'form-control datepicker', 'type': 'date'}),
        }
