from django.contrib import admin
from .models import Profile, BusinessDetails

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'phone_number', 'birth_date', 'profile_image'
    )
    search_fields = (
        'user__username', 'phone_number', 'bio'
    )
    ordering = ('user',)

    fieldsets = (
        (None, {
            'fields': ('user', 'profile_image', 'bio', 'phone_number', 'birth_date')
        }),
    )
    readonly_fields = ('user',)

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
