# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

#My Imports
from datetime import time, date, datetime

# Create your models here.



class TravelTable(models.Model):
   Train = models.IntegerField()
   From = models.CharField(max_length = 10)
   To = models.CharField(max_length = 10)
   Leaving_Date = models.DateField(default = date.today())
   Leaving_Time = models.TimeField()
   Offset = models.TimeField(default = '0:10')
   Lower_Time = models.DateTimeField(default = datetime.now())
   Upper_Time = models.DateTimeField(default = datetime.now())

   def __str__(self):
      print "%d %s %s"  % (
         self.Train,
         self.From,
         self.To
         ) 
