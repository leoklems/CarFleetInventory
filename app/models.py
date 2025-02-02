from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Position(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = "Position"
        verbose_name_plural = "Positions"


    def __str__(self):
        return f"{self.name}"


class Staff(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="staff_user")
    uid = models.SlugField(max_length=15, unique=True, null=True, blank=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=7, choices=GENDER, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    position = models.ForeignKey(Position, related_name='staff_position', 
                                 on_delete=models.CASCADE, null=True, blank=True)
    active = models.BooleanField(default=True)
    present = models.BooleanField(default=False)
    last_checkin = models.DateTimeField(null=True, blank=True)
    last_checkout = models.DateTimeField(null=True, blank=True)
    date_registered = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Staff"
        verbose_name_plural = "Staff"

    def __str__(self):
        return f"{self.name}"
    
class Vehicle(models.Model):
    SERVICABILITY_CHOICES = (
        ('Serviceable', 'Serviceable'),
        ('Not Serviceable', 'Not Serviceable'),
    )

    TRACKER_CHOICES = (
        ('Active', 'Active'),
        ('Not Active', 'Not Active'),
    )
    name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)
    year_purchased = models.IntegerField(null=True, blank=True)
    year_alloted = models.IntegerField(null=True, blank=True)
    agency = models.CharField(max_length=100, null=True, blank=True)
    location_of_deployment = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    tracker_status = models.CharField(max_length=15, choices=TRACKER_CHOICES, default='Active')
    serviceability = models.CharField(max_length=20, choices=SERVICABILITY_CHOICES, default='Serviceable')
    date_recorded = models.DateTimeField(auto_now_add=True)

    def get_most_recent_service(self):
        """Fetch the most recent service record for this vehicle."""
        return self.vehicle_service_record.order_by('-service_date').first()
    
    @property
    def get_most_recent_service_date(self):
        """Fetch the most recent service date for this vehicle."""
        recent_service = self.get_most_recent_service()
        return recent_service.service_date
    
    @property
    def get_next_service_date(self):
        """Fetch the most recent service date for this vehicle."""
        recent_service = self.get_most_recent_service()
        return recent_service.next_service_date

    @property
    def is_service_due(self):
        """Check if the next service date is due based on the most recent service record."""
        recent_service = self.get_most_recent_service()
        if recent_service and recent_service.next_service_date:
            return date.today() >= recent_service.next_service_date
        return False

    def __str__(self):
        return f"{self.name}"

class ServiceRecord(models.Model):
    TYPE_CHOICES = (
        ('Basic', 'Basic'),
        ('Overhaul', 'Overhaul'),
    )
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="vehicle_service_record")
    overhaul_date = models.DateField(null=True, blank=True)
    next_overhaul_date = models.DateField(null=True, blank=True)
    service_date = models.DateField(null=True, blank=True)
    next_service_date = models.DateField(null=True, blank=True)
    type = models.CharField(max_length=15, choices=TYPE_CHOICES, default='Basic')
    cost = models.FloatField(null=True, blank=True)
    scheduled = models.BooleanField(default=True)

    
    # @property
    # def is_past_due(self):
    #     return date.today() > self.completion_date and  self.status != "COMPLETED"

    def __str__(self):
        return f"{self.vehicle} - Service - {self.id}"
