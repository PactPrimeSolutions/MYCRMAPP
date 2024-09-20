from django.urls import path
from .views import (
    base_view, download_excel, generate_report, 
    delete_business_detail, restore_business_detail, retrieve_deleted
)
from django.conf import settings
from django.conf.urls.static import static
from .views import calendar_view
from .views import events_view
from .views import event_list
from . import views
from .views import  add_client_view, delete_client_view, deleted_clients_view, restore_client_view
from .views import client_list_view, client_create_view, client_edit_view, client_delete_view, client_detail_view

from .views import download_excel

urlpatterns = [
    path('', base_view, name='base'),
    path('download-excel/', download_excel, name='download_excel'),
    path('generate-report/', generate_report, name='generate_report'),
    path('delete-business-detail/<int:pk>/', delete_business_detail, name='delete_business_detail'),
    path('restore-business-detail/<int:pk>/', restore_business_detail, name='restore_business_detail'),
    path('retrieve-deleted/', retrieve_deleted, name='retrieve_deleted_business'),
    path('calendar/', calendar_view, name='calendar'),
    path('events/', event_list, name='event_list'),  # Add this line
    path('calendar/add/', views.add_event, name='add_event'),
    path('calendar/delete/<int:event_id>/', views.delete_event, name='delete_event'),
    path('calendar/restore/<int:event_id>/', views.restore_event, name='restore_event'),


    path('clients/', client_list_view, name='client_list'),
    path('clients/new/', client_create_view, name='client_create'),
    path('clients/edit/<int:pk>/', client_edit_view, name='client_edit'),
    path('clients/delete/<int:pk>/', client_delete_view, name='client_delete'),
    path('clients/detail/<int:pk>/', client_detail_view, name='client_detail'),
    path('add/', add_client_view, name='add_client'),
    path('delete/<int:pk>/', delete_client_view, name='delete_client'),
    path('deleted/', deleted_clients_view, name='deleted_clients'),
    path('restore/<int:pk>/', restore_client_view, name='restore_client'),
    path('deleted-clients/', deleted_clients_view, name='deleted_clients'),
     path('load-counties/', views.load_counties, name='load_counties'),

     path('get_counties/<int:state_id>/', views.get_counties, name='get_counties'),




    path('download-excel/', download_excel, name='download_excel'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('events/', events_view, name='events'),
]