from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_image = models.ImageField(default='default-avatar.png', upload_to='users/', null=True, blank=True)
    
    # Additional fields
    sl = models.CharField(max_length=100, blank=True)
    batch_type = models.CharField(max_length=100, blank=True)
    order_no = models.CharField(max_length=100, blank=True)
    received_on = models.DateField(null=True, blank=True)
    borrower_name_1 = models.CharField(max_length=255, blank=True)
    borrower_name_2 = models.CharField(max_length=255, blank=True)
    address = models.TextField(max_length=500, blank=True)
    state = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    organization_date = models.DateField(null=True, blank=True)
    product = models.CharField(max_length=100, blank=True)
    assigned_on = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=100, blank=True)
    processor_name = models.CharField(max_length=100, blank=True)
    typing = models.CharField(max_length=100, blank=True)
    completed_on = models.DateField(null=True, blank=True)
    order = models.CharField(max_length=100, blank=True)
    acer = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

class BusinessDetails(models.Model):
    received_on = models.DateField()
    organization_date = models.DateField()
    assigned_on = models.DateField()
    completed_on = models.DateField()
    sl = models.CharField(max_length=100, blank=True)
    batch_type = models.CharField(max_length=100, blank=True)
    order_no = models.CharField(max_length=100, blank=True)
    borrower_name_1 = models.CharField(max_length=255, blank=True)
    borrower_name_2 = models.CharField(max_length=255, blank=True)
    address = models.TextField(max_length=500, blank=True)
    state = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    product = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=100, blank=True)
    processor_name = models.CharField(max_length=100, blank=True)
    typing = models.CharField(max_length=100, blank=True)
    completed_on = models.DateField(null=True, blank=True)
    order = models.CharField(max_length=100, blank=True)
    acer = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.order_no} - {self.borrower_name_1}"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
