from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from openpyxl import Workbook
from reportlab.pdfgen import canvas
import io
import logging
from .models import BusinessDetails
from .forms import BusinessDetailsForm

logger = logging.getLogger(__name__)

def business_details_view(request):
    """ View to handle the display and creation of business details """
    if request.method == "POST":
        form = BusinessDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info('BusinessDetails saved successfully')
            messages.success(request, "Business details saved successfully!")
            return redirect('business_details')
        else:
            messages.error(request, "Please correct the errors below.")
            logger.error(f'Form errors: {form.errors}')
    else:
        form = BusinessDetailsForm()

    business_details = BusinessDetails.objects.filter(is_deleted=False)
    return render(request, 'myapp/business_details.html', {'form': form, 'business_details': business_details})

def delete_business_detail(request, pk):
    """ View to soft delete a business detail """
    business_detail = get_object_or_404(BusinessDetails, pk=pk)
    if not business_detail.is_deleted:
        business_detail.is_deleted = True
        business_detail.save()
        messages.success(request, "Business detail removed successfully!")
        logger.info(f'BusinessDetails with ID {pk} marked as deleted')
    else:
        messages.warning(request, "This item is already deleted.")
    return redirect('business_details')

def retrieve_deleted_business_details(request):
    """ View to list all deleted business details """
    deleted_business_details = BusinessDetails.objects.filter(is_deleted=True)
    return render(request, 'myapp/retrieve_deleted.html', {'deleted_business_details': deleted_business_details})

def restore_business_detail(request, pk):
    """ View to restore a soft deleted business detail """
    business_detail = get_object_or_404(BusinessDetails, pk=pk)
    if business_detail.is_deleted:
        business_detail.is_deleted = False
        business_detail.save()
        messages.success(request, "Business detail restored successfully!")
        logger.info(f'BusinessDetails with ID {pk} restored')
    else:
        messages.warning(request, "This item is not marked as deleted.")
    return redirect('retrieve_deleted')

def download_excel(request):
    """ View to export business details to an Excel file """
    wb = Workbook()
    ws = wb.active
    ws.title = "Business Details"

    # Define headers
    headers = [
        'SL', 'Batch Type', 'Order No', 'Received On', 'Borrower Name 1',
        'Borrower Name 2', 'Address', 'State', 'Country', 'Loan Amount',
        'Product', 'Status', 'Processor Name', 'Typing', 'Completed On', 'Order', 'Acer'
    ]
    ws.append(headers)

    # Retrieve and append business details data
    try:
        business_details = BusinessDetails.objects.filter(is_deleted=False)
        for business in business_details:
            ws.append([
                business.sl, business.batch_type, business.order_no, business.received_on,
                business.borrower_name_1, business.borrower_name_2, business.address,
                business.state, business.country, business.loan_amount, business.product,
                business.status, business.processor_name, business.typing, business.completed_on,
                business.order, business.acer
            ])
    except Exception as e:
        logger.error(f"Error while exporting to Excel: {e}")
        messages.error(request, "There was an error exporting the data to Excel.")
        return redirect('business_details')

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=business_details.xlsx'
    wb.save(response)

    return response

def generate_report(request):
    """ View to generate a PDF report of business details """
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)

    # Customize the report content here
    p.drawString(100, 750, "Business Details Report")
    p.drawString(100, 730, "This is a sample report.")

    # Example content addition
    # Add more details to the PDF as needed
    p.drawString(100, 700, "Additional report content can be added here.")

    p.showPage()
    p.save()

    buffer.seek(0)
    return HttpResponse(buffer, content_type='application/pdf')


def retrieve_deleted(request):
    """ View to list all deleted business details """
    deleted_business_details = BusinessDetails.objects.filter(is_deleted=True)
    return render(request, 'myapp/retrieve_deleted.html', {'deleted_business_details': deleted_business_details})