# myapp/models.py
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class BusinessDetails(models.Model):
    STATUS_CHOICES = [
        ('choose', 'Choose status'),
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
        ('Clarification', 'Clarification'),
    ]

    received_on = models.DateField(null=True, blank=True)
    #Origination_date = models.DateField(null=True, blank=True)
    assigned_on = models.DateField(null=True, blank=True)
    completed_on = models.DateField(null=True, blank=True)
    sl = models.IntegerField(blank=True, null=True,unique=True)
    batch_type = models.CharField(max_length=100, blank=True)
    order_no = models.CharField(max_length=100, blank=True)
    borrower_name_1 = models.CharField(max_length=255, blank=True)
    borrower_name_2 = models.CharField(max_length=255, blank=True)
    address = models.TextField(max_length=500, blank=True)
    state = models.CharField(max_length=100, blank=True)
    county = models.CharField(max_length=100, blank=True)
    Origination_date = models.DateField(null=True, blank=True)
    loan_amount = models.DecimalField(max_digits=90, decimal_places=2, null=True, blank=True)
    product = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=100, blank=True)
    processor_name = models.CharField(max_length=100, blank=True)
    typing = models.CharField(max_length=100, blank=True)
    order = models.CharField(max_length=100, blank=True)
    Qcer = models.CharField(max_length=100, blank=True)
    is_deleted = models.BooleanField(default=False)  # Field to mark deletion

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='choose',
    )
    

    def __str__(self):
        return f"{self.order_no} - {self.borrower_name_1}"
    
    class Meta:
        verbose_name = _("Business Detail")
        verbose_name_plural = _("Business Details")
        ordering = ['received_on']



    def save(self, *args, **kwargs):
        if not self.pk:  # If new instance
            last_instance = BusinessDetails.objects.exclude(is_deleted=True).order_by('-sl').first()
            if last_instance:
                self.sl = last_instance.sl + 1
            else:
                self.sl = 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.sl} - {self.batch_type}"

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_image = models.ImageField(default='default-avatar.png', upload_to='users/', null=True, blank=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Event(models.Model):
    title = models.CharField(max_length=200)
    start = models.DateTimeField()
    end = models.DateTimeField(null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    deleted = models.BooleanField(default=False) # Soft delete field
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = _("Client")
        verbose_name_plural = _("Clients")
        ordering = ['first_name']



# models.py

class State(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class County(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}, {self.state.name}"
