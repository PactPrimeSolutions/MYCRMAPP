from django import forms
from .models import BusinessDetails, Client, State, County
from django.core.exceptions import ValidationError

# Custom widget for currency input
class CurrencyInput(forms.NumberInput):
    def __init__(self, *args, **kwargs):
        kwargs['attrs'] = {'class': 'form-control currency-input', 'placeholder': '$0.00', 'step': '0.01'}
        super().__init__(*args, **kwargs)

# Form for BusinessDetails model
class BusinessDetailsForm(forms.ModelForm):
    state = forms.ModelChoiceField(queryset=State.objects.all(), widget=forms.Select(attrs={'id': 'state-dropdown', 'class': 'form-control'}))
    county = forms.ModelChoiceField(queryset=County.objects.none(), widget=forms.Select(attrs={'id': 'county-dropdown', 'class': 'form-control'}))

    class Meta:
        model = BusinessDetails
        fields = [
            'received_on', 'assigned_on', 'completed_on',
            'batch_type', 'order_no', 'borrower_name_1', 'borrower_name_2',
            'address', 'state', 'county', 'Origination_date', 'loan_amount', 'product', 'status',
            'processor_name', 'typing', 'completed_on', 'order', 'Qcer'
        ]
        widgets = {
            'received_on': forms.DateInput(attrs={'class': 'form-control datepicker', 'type': 'date'}),
            'assigned_on': forms.DateInput(attrs={'class': 'form-control datepicker', 'type': 'date'}),
            'completed_on': forms.DateInput(attrs={'class': 'form-control datepicker', 'type': 'date'}),
            'Origination_date': forms.DateInput(attrs={'class': 'form-control datepicker', 'type': 'date'}),
            'loan_amount': CurrencyInput(),
            'batch_type': forms.TextInput(attrs={'class': 'form-control'}),
            'order_no': forms.TextInput(attrs={'class': 'form-control'}),
            'borrower_name_1': forms.TextInput(attrs={'class': 'form-control'}),
            'borrower_name_2': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'product': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'processor_name': forms.TextInput(attrs={'class': 'form-control'}),
            'typing': forms.TextInput(attrs={'class': 'form-control'}),
            'order': forms.TextInput(attrs={'class': 'form-control'}),
            'Qcer': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'state' in self.data:
            try:
                state_id = int(self.data.get('state'))
                self.fields['county'].queryset = County.objects.filter(state_id=state_id).order_by('name')
            except (ValueError, TypeError):
                self.fields['county'].queryset = County.objects.none()
        elif self.instance.pk:
            self.fields['county'].queryset = self.instance.state.county_set.order_by('name')

    def clean(self):
        cleaned_data = super().clean()
        received_on = cleaned_data.get("received_on")
        Origination_date = cleaned_data.get("Origination_date")
        assigned_on = cleaned_data.get("assigned_on")
        completed_on = cleaned_data.get("completed_on")

        #if Origination_date and received_on and Origination_date <= received_on:
            #raise ValidationError("Origination Date must be after Received On Date.")
        
        #if assigned_on and Origination_date and assigned_on <= Origination_date:
            #raise ValidationError("Assigned On Date must be after Origination Date.")
        
        if completed_on and assigned_on and completed_on <= assigned_on:
            raise ValidationError("Completed On Date must be after Assigned On Date.")
        
        return cleaned_data

# Form for Client model
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            'first_name', 'last_name', 'email', 'phone', 'address'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
