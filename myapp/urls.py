from django.urls import path
from .views import (
    business_details_view, download_excel, generate_report, 
    delete_business_detail, restore_business_detail, retrieve_deleted
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', business_details_view, name='business_details'),
    path('download-excel/', download_excel, name='download_excel'),
    path('generate-report/', generate_report, name='generate_report'),
    path('delete-business-detail/<int:pk>/', delete_business_detail, name='delete_business_detail'),
    path('restore-business-detail/<int:pk>/', restore_business_detail, name='restore_business_detail'),
    path('retrieve-deleted/', retrieve_deleted, name='retrieve_deleted'),  # Add this line
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
