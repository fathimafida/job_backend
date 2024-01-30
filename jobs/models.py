from django.db import models


class Alumni(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)


class Internship(models.Model):
    company = models.CharField(max_length=255)
    duration = models.CharField(max_length=50)
    role = models.CharField(max_length=255)


class Placement(models.Model):
    company = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    package = models.DecimalField(max_digits=10, decimal_places=2)


class JobsModule(models.Model):
    module_name = models.CharField(max_length=255)
    alumni = models.ManyToManyField(Alumni)
    internship_details = models.ManyToManyField(Internship)
    placements = models.ManyToManyField(Placement)
    additional_info = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.module_name
