"""
App Models
Create your models in here
"""

import json

# Django
from django.db import models
from django.contrib.auth.decorators import login_required, permission_required
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Subquery, OuterRef
from django.db.models import F
from django.db.models.functions import Coalesce
from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class General(models.Model):
    """Meta model for app permissions"""

    class Meta:
        """Meta definitions"""

        managed = False
        default_permissions = ()
        permissions = (("basic_access",         "Can access the view payouts table app"),
                       ("use_access",           "Can access, use and therefore request reimbursements."),
                       ("fcing_access",         "Can access the fleet command module to create srp links and view them"),
                       ("reimbursement_access", "Can access the reimbursement module to accept, reject, and delete srp requests, as well as view statistics"),
                       ("admin_access",         "Can force to recalculate the view payouts table"),)

class Ship(models.Model):
    name = models.CharField(max_length=255, blank=True, unique=True)
    ship_id = models.IntegerField(default=0, unique=True)

    def __str__(self):
        return self.name

class Reimbursement(models.Model):
    index = models.IntegerField(default=0, unique=False)
    name = models.CharField(max_length=255, blank=True, unique=True)

    def __str__(self):
        return "#" + str(self.index) + " " + self.name

class Payout(models.Model):
    value = models.IntegerField(default=0, unique=False)
    ship = models.ForeignKey(Ship, on_delete=models.CASCADE, related_name="cells", default=1)
    reimbursement = models.ForeignKey(Reimbursement, on_delete=models.CASCADE, related_name="cells", default=1)

    def __str__(self):
        return "(" + self.reimbursement.name + ") " + self.ship.name + ": " + format(self.value, ",") + " ISK"

class Srp(models.Model):
    reimbursement = models.IntegerField(unique=False)
    amount = models.IntegerField(unique=False)
    comment = models.CharField(max_length=255, blank=True)

    handler_character_id = models.IntegerField(unique=False, default=0)
    handler_character_name = models.CharField(max_length=255)
    handler_corporation_id = models.IntegerField(unique=False, default=0)
    handler_corporation_name = models.CharField(max_length=255)
    handler_alliance_id = models.IntegerField(unique=False, default=0)
    handler_alliance_name = models.CharField(max_length=255)

    def __str__(self):
        status_string = ""
        if self.reimbursement == 0:
            status_string = "Paid"
        elif self.reimbursement == 1:
            status_string = "Rejected"
        
        return status_string

class Request(models.Model):
    killmail_id = models.IntegerField(unique=True)
    killmail_hash = models.CharField(max_length=255, default="")
    killmail_time = models.DateTimeField()
    killmail_amount = models.IntegerField(unique=False, default=0)
    requester = models.CharField(max_length=255, default='')
    requested_on = models.DateTimeField(auto_now_add=True)
    ship_id = models.IntegerField(unique=False, default=0)
    ship_name = models.CharField(max_length=255, default="")
    character_id = models.IntegerField(unique=False, default=0)
    character_name = models.CharField(max_length=255, default="")
    corporation_id = models.IntegerField(unique=False, default=0)
    corporation_name = models.CharField(max_length=255, default="")
    alliance_id = models.IntegerField(unique=False, default=0)
    alliance_name = models.CharField(max_length=255, default="")
    system_id = models.IntegerField(unique=False, default=0)
    system_name = models.CharField(max_length=255, default="")
    constellation_id = models.IntegerField(unique=False, default=0)
    constellation_name = models.CharField(max_length=255, default="")
    region_id = models.IntegerField(unique=False, default=0)
    region_name = models.CharField(max_length=255, default="")

    broadcast = models.TextField(default="")

    data = models.JSONField()

    review = models.ForeignKey(Srp, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.character_name) + ": " + str(self.ship_name)

class ShipData(models.Model):
    killmail_id = models.IntegerField(unique=True)
    

def recalculate_matrix():
    ship_rows = Ship.objects.all().order_by("name")
    columns = Reimbursement.objects.all().order_by("index")
    matrix = []

    for row in ship_rows:
        if Payout.objects.filter(ship=row).count() > 0:
            row_data = [row]
            for column in columns:
                cell = Payout.objects.filter(ship=row, reimbursement=column).first()
                row_data.append(cell)
            matrix.append(row_data)

    cache.set('matrix', matrix, None)

def calculate_temp_matrix(query):

    if query:
        ship_rows = Ship.objects.filter(name__icontains=query).order_by("name")
        columns = Reimbursement.objects.all().order_by("index")
        matrix = []

        for row in ship_rows:
            if Payout.objects.filter(ship=row).count() > 0:
                row_data = [row]
                for column in columns:
                    cell = Payout.objects.filter(ship=row, reimbursement=column).first()
                    row_data.append(cell)
                matrix.append(row_data)

        return matrix
    else:
        ship_rows = Ship.objects.all().order_by("name")
        columns = Reimbursement.objects.all().order_by("index")
        matrix = []

        for row in ship_rows:
            if Payout.objects.filter(ship=row).count() > 0:
                row_data = [row]
                for column in columns:
                    cell = Payout.objects.filter(ship=row, reimbursement=column).first()
                    row_data.append(cell)
                matrix.append(row_data)
        
        return matrix


## Payout Receiver

@receiver(post_save, sender=Payout)
def payout_post_save(sender, instance, **kwargs):
    recalculate_matrix()

@receiver(post_delete, sender=Payout)
def payout_post_delete(sender, instance, **kwargs):
    recalculate_matrix()

## Reimbursement Receiver

@receiver(post_save, sender=Reimbursement)
def reimbursement_post_save(sender, instance, **kwargs):
    recalculate_matrix()

@receiver(post_delete, sender=Reimbursement)
def reimbursement_post_delete(sender, instance, **kwargs):
    recalculate_matrix()

## Ship Receiver

@receiver(post_save, sender=Ship)
def ship_post_save(sender, instance, **kwargs):
    recalculate_matrix()

@receiver(post_delete, sender=Ship)
def ship_post_delete(sender, instance, **kwargs):
    recalculate_matrix()
