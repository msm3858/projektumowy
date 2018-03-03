from django.db import models
from django.shortcuts import reverse
from django.db import models
############################################################################################################################
## BAZY DANYCH ##
############################################################################################################################
class BazyDanych(models.Model):
    ORACLE = 'Or'
    MYSQL = 'My'
    POSTGRESQL = 'Po'
    MSSQL = 'Ms'
    DB_CHOICES = (
        (ORACLE, 'Oracle'),
        (MYSQL, 'MySQL'),
        (POSTGRESQL, 'PostgreSQL'),
        (MSSQL, 'MS SQL'),
    )
    PLATNA = 'Pl'
    DARMOWA = 'Da'
    LICENCJA_CHOICES = (
        (PLATNA, 'Płatna'),
        (DARMOWA, 'Darmowa'),
    )
    nazwa = models.CharField(
        max_length=2,
        choices = DB_CHOICES,
        default=MYSQL,
    )
    wersja = models.CharField(max_length=40)
    licencja = models.CharField(
        max_length=2,
        choices = LICENCJA_CHOICES,
        default = DARMOWA
    )
    def __str__(self):
        return self.nazwa + " " + self.wersja
    def get_absolute_url(self):
        return reverse('umowy:bazy_detail',kwargs={'pk':self.pk})

############################################################################################################################
## ADMINISTRATORZY ##
############################################################################################################################

class Administratorzy(models.Model):
    imie = models.CharField(max_length=100)
    nazwisko = models.CharField(max_length=100)
    def __str__(self):
        return self.imie + " " + self.nazwisko
    def get_absolute_url(self):
        return reverse('umowy:administratorzy_detail',kwargs={'pk':self.pk})
############################################################################################################################
## SERWERY ##
############################################################################################################################
class Serwery(models.Model):
    LINUX = 'L'
    WINDOWS = 'W'
    SYSTEM_CHOICES = (
        (LINUX, 'Linux'),
        (WINDOWS, 'Windows'),
    )
    FIZYCZNY = 'F'
    WIRTUALNY = 'W'
    WIFI_CHOICES = (
        (FIZYCZNY,'Fizyczny'),
        (WIRTUALNY,'Wirtualny'),

    )
    hostname = models.CharField(max_length=100, unique=True)
    nazwa = models.CharField(max_length=100)
    system_operacyjny = models.CharField(
        max_length=1,
        choices = SYSTEM_CHOICES,
        default = WINDOWS,
    )
    fizyczny_wirtualny = models.CharField(
        max_length=1,
        choices = WIFI_CHOICES,
        default = FIZYCZNY,
    )
    wersja = models.CharField(max_length=40)
    adres = models.CharField(max_length=15)
    def __str__(self):
        return self.nazwa + " " + self.wersja
    def get_absolute_url(self):
        return reverse('umowy:serwery_detail',kwargs={'pk':self.pk})


############################################################################################################################
## SYSTEMY ##
############################################################################################################################
class Systemy(models.Model):
    INSTYTUT = 'IB'
    SPOLKA = 'SP'
    FIRMA_CHOICES = (
        (INSTYTUT, 'NASK PIB'),
        (SPOLKA, 'NASK SA'),
    )
    firma = models.CharField(
        max_length=2,
        choices = FIRMA_CHOICES,
        default = INSTYTUT,
    )
    nazwa = models.CharField(max_length=100)
    opis_systemu = models.TextField(max_length=400)
    baza_danych = models.ForeignKey(BazyDanych,blank=True, null=True,on_delete=models.SET_NULL)
    oprogramowanie = models.CharField(max_length=100,blank=True)
    data_wsparcia = models.DateField('data końca wsparcia')
    administrator_systemu_glowny = models.ForeignKey(Administratorzy,blank=True, null=True,on_delete=models.SET_NULL, related_name='admin_system_glowny')
    administrator_systemu_zastepczy = models.ForeignKey(Administratorzy,blank=True, null=True,on_delete=models.SET_NULL, related_name='admin_system_zastepca')
    administrator_bazy_glowny = models.ForeignKey(Administratorzy,blank=True, null=True,on_delete=models.SET_NULL, related_name='admin_baza_glowny')
    administrator_bazy_zastepczy = models.ForeignKey(Administratorzy,blank=True, null=True,on_delete=models.SET_NULL, related_name='admin_baza_zastepca')
    def get_absolute_url(self):
        return reverse('umowy:systemy_detail',kwargs={'pk':self.pk})
    def __str__(self):
        return self.nazwa

############################################################################################################################
## UMOWY UTRZYMANIOWE ##
############################################################################################################################

class UmowyUtrzymaniowe(models.Model):
    opis = models.CharField(max_length=100)
    dataUmowy = models.DateField('Data podpisania')
    dataKoncaUmowy = models.DateField('Data końca obowiązywania')
    wsparcie_techniczne = models.TextField(max_length=400)
    system = models.ForeignKey(Systemy, on_delete=models.CASCADE)
    plik_umowy = models.FileField()
    def get_absolute_url(self):
        return reverse('umowy:umowy_detail',kwargs={'pk':self.pk})
    def __str__(self):
        return self.opis

############################################################################################################################
## SERWERY SYSTEMÓW ##
############################################################################################################################
class SerwerySystemow(models.Model):
    serwer = models.ForeignKey(Serwery,blank=True, null=True,on_delete=models.SET_NULL)
    system = models.ForeignKey(Systemy,blank=True, null=True,on_delete=models.SET_NULL)
    def get_absolute_url(self):
        return reverse('umowy:serwerysystemow_detail',kwargs={'pk':self.pk})