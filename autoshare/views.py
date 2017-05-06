# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

#My Imports
from forms import TravelForm, RegistrationForm
from autoshare.models import TravelTable
from datetime import date, time, datetime, timedelta
from urllib2 import urlopen
# Create your views here.

@csrf_exempt
def TravelView(request):
   if request.method == 'GET':
      form = TravelForm()
      #variables = RequestContext(request, {'form':form})
      return render_to_response('Travel.html', {'form' : form} ) 
      
   if request.method == 'POST':
      form = TravelForm(request.POST)
      if form.is_valid():
         Leaving_Time = form.cleaned_data['Leaving_Time']
         Leaving_Date = form.cleaned_data['Leaving_Date']
         Offset = form.cleaned_data['Offset']
         From = form.cleaned_data['From']
         To = form.cleaned_data['To']
         Entry, created = TravelTable.objects.get_or_create(
            Train = form.cleaned_data['Train'],
            From = From,
            To = To,
            Leaving_Time = Leaving_Time,
            Leaving_Date = Leaving_Date,
            Offset = Offset)
         Entry.Upper_Time = datetime(year = Leaving_Date.year,
                                  month = Leaving_Date.month,
                                  day = Leaving_Date.day,
                                  hour = Leaving_Time.hour,
                                  minute = Leaving_Time.minute,
                                  second = Leaving_Time.second)
         Entry.Lower_Time = Entry.Upper_Time + timedelta(hours = -Offset.hour,
                                                minutes = -Offset.minute)
         Entry.save()
         queryset = TravelTable.objects.filter(Lower_Time__lte = Entry.Upper_Time,
                                         From = From, To = To)
         return render_to_response('results.html', {'query':queryset, 'user': request.user})
      else:
         return HttpResponseRedirect('/home')

@csrf_exempt
def RegistrationView(request):
   if request.method == 'POST':
      form = RegistrationForm(request.POST)
      if form.is_valid() and form.clean_password() and  form.clean_username():
         Entry = User.objects.create_user(
               username = form.cleaned_data['Username'],
               password = form.cleaned_data['Password1'],
               email = form.cleaned_data['Email'],
               last_name = form.cleaned_data['Last_Name'],
               first_name = form.cleaned_data['First_Name']
            )
         Entry.save()
         return HttpResponseRedirect('/home')
      else:
         return HttpResponseRedirect('/register')
   else:
      form = RegistrationForm()
      return render_to_response('register.html', {'form':form})

def logout(request):
   logout(request)
   return HttpResponseRedirect('/')

@csrf_exempt
def ShowResults(Upper_Time, From, To):
   queryset = TravelTable.objects.filter(Lower_Time__gte = Upper_Time,
                                         From = From, To = To)
   print 'ashwani\nkumar\ngautam'
   return render_to_response('results.html')
