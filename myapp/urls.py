# myapp/urls.py
from django.urls import path
from .views import business_details_view
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', business_details_view, name='business_details'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
