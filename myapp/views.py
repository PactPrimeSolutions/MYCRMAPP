from django.shortcuts import render, redirect
from django.contrib import messages
from .models import BusinessDetails
from .forms import BusinessDetailsForm
import logging

logger = logging.getLogger(__name__)

def business_details_view(request):
    if request.method == "POST":
        form = BusinessDetailsForm(request.POST)
        if form.is_valid():
            instance = form.save()
            logger.info(f'BusinessDetails saved: {instance}')
            messages.success(request, "Business details saved successfully!")
            return redirect('business_details')
        else:
            messages.error(request, "Please correct the errors below.")
            logger.error(f'Form errors: {form.errors}')
    else:
        form = BusinessDetailsForm()

    business_details = BusinessDetails.objects.all()
    return render(request, 'myapp/business_details.html', {'form': form, 'business_details': business_details})
