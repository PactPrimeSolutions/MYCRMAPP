# myapp/models.py
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class BusinessDetails(models.Model):
    received_on = models.DateField()
    organization_date = models.DateField()
    assigned_on = models.DateField()
    completed_on = models.DateField()
    sl = models.IntegerField(blank=True, null=True)
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
    is_deleted = models.BooleanField(default=False)  # Field to mark deletion

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
    # Other fields as needed

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
