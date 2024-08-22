from django.contrib import admin
from .models import Profile, BusinessDetails

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'phone_number', 'birth_date', 'sl', 'batch_type', 
        'order_no', 'received_on', 'borrower_name_1', 'borrower_name_2', 
        'loan_amount', 'status', 'completed_on'
    )
    search_fields = (
        'user__username', 'phone_number', 'borrower_name_1', 
        'borrower_name_2', 'address'
    )
    list_filter = (
        'status', 'product', 'assigned_on'
    )
    ordering = ('user',)

    fieldsets = (
        (None, {
            'fields': ('user', 'profile_image', 'bio', 'phone_number', 'birth_date')
        }),
        ('Loan Details', {
            'fields': (
                'sl', 'batch_type', 'order_no', 'received_on', 'borrower_name_1', 
                'borrower_name_2', 'address', 'state', 'country', 'loan_amount', 
                'organization_date', 'product', 'assigned_on', 'status', 
                'processor_name', 'typing', 'completed_on', 'order', 'acer'
            )
        }),
    )

@admin.register(BusinessDetails)
class BusinessDetailsAdmin(admin.ModelAdmin):
    list_display = (
        'sl', 'batch_type', 'order_no', 'received_on', 'borrower_name_1', 
        'borrower_name_2', 'loan_amount', 'status', 'completed_on'
    )
    search_fields = (
        'order_no', 'borrower_name_1', 'borrower_name_2', 'address'
    )
    list_filter = (
        'status', 'product', 'assigned_on'
    )
    ordering = ('received_on',)
