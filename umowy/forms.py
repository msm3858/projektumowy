from .models import Systemy,UmowyUtrzymaniowe
from django import forms

from django.contrib.auth.models import User


class SystemForm(forms.ModelForm):
    class Meta:
        model = Systemy
        fields = ['nazwa','opis_systemu','firma','baza_danych','oprogramowanie','data_wsparcia','administrator_systemu_glowny','administrator_systemu_zastepczy','administrator_bazy_glowny','administrator_bazy_zastepczy']
        widgets = {
            'data_wsparcia': forms.SelectDateWidget(),
            'opis_systemu': forms.Textarea(attrs={'cols':60,'rows':5}),

        }
        labels = {
            'nazwa':'Nazwa systemu',
            'opis_systemu': 'Opis systemu',
            'baza_danych': 'Baza danych na jakiej oparty jest system',
            'oprogramowanie': 'Oprogramowanie do systemu',
            'administrator_systemu_glowny': 'Administrator główny systemu',
            'administrator_systemu_zastepczy': 'Administrator zastępczy systemu',
            'administrator_bazy_glowny':'Administrator główny bazy danych',
            'administrator_bazy_zastepczy':'Administrator zastępczy bazy danych',

        }
        #error_messages = {
        #    NON_FIELD_ERRORS: {
        #
        #    }
        #}

class UmowaForm(forms.ModelForm):
    class Meta:
        model = UmowyUtrzymaniowe
        fields = ['opis','dataUmowy','dataKoncaUmowy','wsparcie_techniczne','system','plik_umowy']
        widgets = {
            'dataUmowy': forms.SelectDateWidget(),
            'dataKoncaUmowy': forms.SelectDateWidget()
        }
    




    #class Meta:
    #    model = Systemy
    #   fields = ['nazwa','opis_systemu','baza_danych','oprogramowanie','data_wsparcia']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']
        widgets = {
            'password': forms.PasswordInput(),
        }