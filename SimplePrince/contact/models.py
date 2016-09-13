from __future__ import unicode_literals

import os
from django.db import models
from django.core.files.storage import FileSystemStorage
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.conf import settings


# Create your models here.


class Registration(models.Model):
    
    contact_name = models.CharField(_('Name'),
     max_length=40, blank=False, null=True, unique=False)
    contact_email = models.EmailField(_('Email'),
     max_length=40, blank=False, null=True, unique=False)
    