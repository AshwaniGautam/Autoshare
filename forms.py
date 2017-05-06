from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

class TravelForm(forms.Form):
   From = forms.ChoiceField(label='From',
                          choices = (('Campus', 'Campus'),
                                    ('CNB', 'CNB')),
                          initial = "Campus",
                          )

   To = forms.ChoiceField(label='To',
                          choices = (('CNB', 'CNB'),
                                    ('Campus', 'Campus')),
                          initial = "CNB"
                        )

   Train = forms.IntegerField(label = 'Train', required = False)
   Leaving_Date = forms.DateField(label = 'Leaving Date')
   Leaving_Time = forms.TimeField(label = 'Leaving Time')
   Offset =  forms.TimeField(label = 'Offset', initial = '1:00')

class RegistrationForm(forms.Form):
   
   First_Name = forms.CharField(label = 'First Name', required = True)
   Last_Name = forms.CharField(label = 'Last Name', required = True)
   Email = forms.EmailField(label = 'Email ID', required = True)
   Username = forms.CharField(label = 'Username', required = True)
   Password1 = forms.CharField(label = 'Password',
                               required = True,
                               widget = forms.PasswordInput())
   Password2 = forms.CharField(label = 'Confirm Password',
                               required = True,
                               widget = forms.PasswordInput())
   def clean_password(self):
      password1 = self.cleaned_data['Password1']
      password2 = self.cleaned_data['Password2']
      if password1 == password2:
         return 1
      raise forms.ValidationError('Passwords Do Not Match.')

   def clean_username(self):
      try:
         User.objects.get(username = self.cleaned_data['Username'])
      except ObjectDoesNotExist:
         return 1
      raise forms.ValidationError('Username is already Taken.')
