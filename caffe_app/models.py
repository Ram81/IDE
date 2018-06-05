from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import User


class Network(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)
    network = JSONField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, blank=True, null=True)

    def __unicode__(self):
        return self.name


class SharedWith(models.Model):
    ACCESS_PRIVILEGE = (
        ('E', 'Can Edit'),
        ('V', 'Can View'),
        ('C', 'Can Comment')
    )
    network = models.ForeignKey(Network)
    user = models.ForeignKey(User)
    access_privilege = models.CharField(max_length=1, choices=ACCESS_PRIVILEGE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return ''


class ModelExport(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=20, primary_key=True)
    network = JSONField()
    createdOn = models.DateField(auto_now_add=True)
    updatedOn = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.id
