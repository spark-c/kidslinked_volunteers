from django.db import models

class Applicant(models.Model):
    firstname = models.Charfield(max_length=200)
    lastname = models.Charfield(max_length=200)
    email = models.EmailField(blank=True) # allow users w no email
    phone = models.Charfield(max_length=200)
    org_affiliation = models.Charfield(max_length=200)
    station_preference = models.JSONField() # e.g. {"games": False, "ticket_sales": True, ... } bc no array model field in SQLite