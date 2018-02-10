# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Bat(models.Model):
    date = models.DateField(blank=True, primary_key=True, unique=True)
    txvolume = models.FloatField(blank=True, null=True)
    txcount = models.FloatField(blank=True, null=True)
    marketcap = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    exchangevolume = models.FloatField(blank=True, null=True)
    generatedcoins = models.FloatField(blank=True, null=True)
    fees = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bat'


class Bch(models.Model):
    date = models.DateField(blank=True, primary_key=True, unique=True)
    txvolume = models.FloatField(blank=True, null=True)
    txcount = models.FloatField(blank=True, null=True)
    marketcap = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    exchangevolume = models.FloatField(blank=True, null=True)
    generatedcoins = models.FloatField(blank=True, null=True)
    fees = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bch'


class Bnb(models.Model):
    date = models.DateField(blank=True, primary_key=True, unique=True)
    txvolume = models.FloatField(blank=True, null=True)
    txcount = models.FloatField(blank=True, null=True)
    marketcap = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    exchangevolume = models.FloatField(blank=True, null=True)
    generatedcoins = models.FloatField(blank=True, null=True)
    fees = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bnb'


class Btc(models.Model):
    date = models.DateField(blank=True, primary_key=True, unique=True)
    txvolume = models.FloatField(blank=True, null=True)
    txcount = models.FloatField(blank=True, null=True)
    marketcap = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    exchangevolume = models.FloatField(blank=True, null=True)
    generatedcoins = models.FloatField(blank=True, null=True)
    fees = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'btc'


class Btg(models.Model):
    date = models.DateField(blank=True, primary_key=True, unique=True)
    txvolume = models.FloatField(blank=True, null=True)
    txcount = models.FloatField(blank=True, null=True)
    marketcap = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    exchangevolume = models.FloatField(blank=True, null=True)
    generatedcoins = models.FloatField(blank=True, null=True)
    fees = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'btg'


class Cyca(models.Model):
    date = models.DateField(blank=True, primary_key=True, unique=True)
    txvolume = models.FloatField(blank=True, null=True)
    txcount = models.FloatField(blank=True, null=True)
    marketcap = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    exchangevolume = models.FloatField(blank=True, null=True)
    generatedcoins = models.FloatField(blank=True, null=True)
    fees = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cyca'


class Dash(models.Model):
    date = models.DateField(blank=True, primary_key=True, unique=True)
    txvolume = models.FloatField(blank=True, null=True)
    txcount = models.FloatField(blank=True, null=True)
    marketcap = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    exchangevolume = models.FloatField(blank=True, null=True)
    generatedcoins = models.FloatField(blank=True, null=True)
    fees = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dash'


class Dcr(models.Model):
    date = models.DateField(blank=True, primary_key=True, unique=True)
    txvolume = models.FloatField(blank=True, null=True)
    txcount = models.FloatField(blank=True, null=True)
    marketcap = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    exchangevolume = models.FloatField(blank=True, null=True)
    generatedcoins = models.FloatField(blank=True, null=True)
    fees = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dcr'


class Dgb(models.Model):
    date = models.DateField(blank=True, primary_key=True, unique=True)
    txvolume = models.FloatField(blank=True, null=True)
    txcount = models.FloatField(blank=True, null=True)
    marketcap = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    exchangevolume = models.FloatField(blank=True, null=True)
    generatedcoins = models.FloatField(blank=True, null=True)
    fees = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dgb'


class Doge(models.Model):
    date = models.DateField(blank=True, primary_key=True, unique=True)
    txvolume = models.FloatField(blank=True, null=True)
    txcount = models.FloatField(blank=True, null=True)
    marketcap = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    exchangevolume = models.FloatField(blank=True, null=True)
    generatedcoins = models.FloatField(blank=True, null=True)
    fees = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doge'


class Eos(models.Model):
    date = models.DateField(blank=True, primary_key=True, unique=True)
    txvolume = models.FloatField(blank=True, null=True)
    txcount = models.FloatField(blank=True, null=True)
    marketcap = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    exchangevolume = models.FloatField(blank=True, null=True)
    generatedcoins = models.FloatField(blank=True, null=True)
    fees = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eos'


class Etc(models.Model):
    date = models.DateField(blank=True, primary_key=True, unique=True)
    txvolume = models.FloatField(blank=True, null=True)
    txcount = models.FloatField(blank=True, null=True)
    marketcap = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    exchangevolume = models.FloatField(blank=True, null=True)
    generatedcoins = models.FloatField(blank=True, null=True)
    fees = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'etc'


class Eth(models.Model):
    date = models.DateField(blank=True, primary_key=True, unique=True)
    txvolume = models.FloatField(blank=True, null=True)
    txcount = models.FloatField(blank=True, null=True)
    marketcap = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    exchangevolume = models.FloatField(blank=True, null=True)
    generatedcoins = models.FloatField(blank=True, null=True)
    fees = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eth'


class Fun(models.Model):
    date = models.DateField(blank=True, primary_key=True, unique=True)
    txvolume = models.FloatField(blank=True, null=True)
    txcount = models.FloatField(blank=True, null=True)
    marketcap = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    exchangevolume = models.FloatField(blank=True, null=True)
    generatedcoins = models.FloatField(blank=True, null=True)
    fees = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fun'


class Gno(models.Model):
    date = models.DateField(blank=True, primary_key=True, unique=True)
    txvolume = models.FloatField(blank=True, null=True)
    txcount = models.FloatField(blank=True, null=True)
    marketcap = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    exchangevolume = models.FloatField(blank=True, null=True)
    generatedcoins = models.FloatField(blank=True, null=True)
    fees = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gno'


class Gnt(models.Model):
    date = models.DateField(blank=True, primary_key=True, unique=True)
    txvolume = models.FloatField(blank=True, null=True)
    txcount = models.FloatField(blank=True, null=True)
    marketcap = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    exchangevolume = models.FloatField(blank=True, null=True)
    generatedcoins = models.FloatField(blank=True, null=True)
    fees = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gnt'


class Icx(models.Model):
    date = models.DateField(blank=True, primary_key=True, unique=True)
    txvolume = models.FloatField(blank=True, null=True)
    txcount = models.FloatField(blank=True, null=True)
    marketcap = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    exchangevolume = models.FloatField(blank=True, null=True)
    generatedcoins = models.FloatField(blank=True, null=True)
    fees = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icx'


class Knc(models.Model):
    date = models.DateField(blank=True, primary_key=True, unique=True)
    txvolume = models.FloatField(blank=True, null=True)
    txcount = models.FloatField(blank=True, null=True)
    marketcap = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    exchangevolume = models.FloatField(blank=True, null=True)
    generatedcoins = models.FloatField(blank=True, null=True)
    fees = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'knc'


class Ltc(models.Model):
    date = models.DateField(blank=True, primary_key=True, unique=True)
    txvolume = models.FloatField(blank=True, null=True)
    txcount = models.FloatField(blank=True, null=True)
    marketcap = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    exchangevolume = models.FloatField(blank=True, null=True)
    generatedcoins = models.FloatField(blank=True, null=True)
    fees = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ltc'


class Omg(models.Model):
    date = models.DateField(blank=True, primary_key=True, unique=True)
    txvolume = models.FloatField(blank=True, null=True)
    txcount = models.FloatField(blank=True, null=True)
    marketcap = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    exchangevolume = models.FloatField(blank=True, null=True)
    generatedcoins = models.FloatField(blank=True, null=True)
    fees = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'omg'


class Pivx(models.Model):
    date = models.DateField(blank=True, primary_key=True, unique=True)
    txvolume = models.FloatField(blank=True, null=True)
    txcount = models.FloatField(blank=True, null=True)
    marketcap = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    exchangevolume = models.FloatField(blank=True, null=True)
    generatedcoins = models.FloatField(blank=True, null=True)
    fees = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pivx'


class Ppt(models.Model):
    date = models.DateField(blank=True, primary_key=True, unique=True)
    txvolume = models.FloatField(blank=True, null=True)
    txcount = models.FloatField(blank=True, null=True)
    marketcap = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    exchangevolume = models.FloatField(blank=True, null=True)
    generatedcoins = models.FloatField(blank=True, null=True)
    fees = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ppt'


class Rep(models.Model):
    date = models.DateField(blank=True, primary_key=True, unique=True)
    txvolume = models.FloatField(blank=True, null=True)
    txcount = models.FloatField(blank=True, null=True)
    marketcap = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    exchangevolume = models.FloatField(blank=True, null=True)
    generatedcoins = models.FloatField(blank=True, null=True)
    fees = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rep'


class Salt(models.Model):
    date = models.DateField(blank=True, primary_key=True, unique=True)
    txvolume = models.FloatField(blank=True, null=True)
    txcount = models.FloatField(blank=True, null=True)
    marketcap = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    exchangevolume = models.FloatField(blank=True, null=True)
    generatedcoins = models.FloatField(blank=True, null=True)
    fees = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'salt'


class Snt(models.Model):
    date = models.DateField(blank=True, primary_key=True, unique=True)
    txvolume = models.FloatField(blank=True, null=True)
    txcount = models.FloatField(blank=True, null=True)
    marketcap = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    exchangevolume = models.FloatField(blank=True, null=True)
    generatedcoins = models.FloatField(blank=True, null=True)
    fees = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'snt'


class SpatialRefSys(models.Model):
    srid = models.IntegerField(primary_key=True)
    auth_name = models.CharField(max_length=256, blank=True, null=True)
    auth_srid = models.IntegerField(blank=True, null=True)
    srtext = models.CharField(max_length=2048, blank=True, null=True)
    proj4text = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spatial_ref_sys'


class Trx(models.Model):
    date = models.DateField(blank=True, primary_key=True, unique=True)
    txvolume = models.FloatField(blank=True, null=True)
    txcount = models.FloatField(blank=True, null=True)
    marketcap = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    exchangevolume = models.FloatField(blank=True, null=True)
    generatedcoins = models.FloatField(blank=True, null=True)
    fees = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trx'


class Veri(models.Model):
    date = models.DateField(blank=True, primary_key=True, unique=True)
    txvolume = models.FloatField(blank=True, null=True)
    txcount = models.FloatField(blank=True, null=True)
    marketcap = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    exchangevolume = models.FloatField(blank=True, null=True)
    generatedcoins = models.FloatField(blank=True, null=True)
    fees = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'veri'


class Vtc(models.Model):
    date = models.DateField(blank=True, primary_key=True, unique=True)
    txvolume = models.FloatField(blank=True, null=True)
    txcount = models.FloatField(blank=True, null=True)
    marketcap = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    exchangevolume = models.FloatField(blank=True, null=True)
    generatedcoins = models.FloatField(blank=True, null=True)
    fees = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vtc'


class Wtc(models.Model):
    date = models.DateField(blank=True, primary_key=True, unique=True)
    txvolume = models.FloatField(blank=True, null=True)
    txcount = models.FloatField(blank=True, null=True)
    marketcap = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    exchangevolume = models.FloatField(blank=True, null=True)
    generatedcoins = models.FloatField(blank=True, null=True)
    fees = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wtc'


class Xem(models.Model):
    date = models.DateField(blank=True, primary_key=True, unique=True)
    txvolume = models.FloatField(blank=True, null=True)
    txcount = models.FloatField(blank=True, null=True)
    marketcap = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    exchangevolume = models.FloatField(blank=True, null=True)
    generatedcoins = models.FloatField(blank=True, null=True)
    fees = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xem'


class Xmr(models.Model):
    date = models.DateField(blank=True, primary_key=True, unique=True)
    txvolume = models.FloatField(blank=True, null=True)
    txcount = models.FloatField(blank=True, null=True)
    marketcap = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    exchangevolume = models.FloatField(blank=True, null=True)
    generatedcoins = models.FloatField(blank=True, null=True)
    fees = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xmr'


class Xvg(models.Model):
    date = models.DateField(blank=True, primary_key=True, unique=True)
    txvolume = models.FloatField(blank=True, null=True)
    txcount = models.FloatField(blank=True, null=True)
    marketcap = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    exchangevolume = models.FloatField(blank=True, null=True)
    generatedcoins = models.FloatField(blank=True, null=True)
    fees = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xvg'


class Zec(models.Model):
    date = models.DateField(blank=True, primary_key=True, unique=True)
    txvolume = models.FloatField(blank=True, null=True)
    txcount = models.FloatField(blank=True, null=True)
    marketcap = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    exchangevolume = models.FloatField(blank=True, null=True)
    generatedcoins = models.FloatField(blank=True, null=True)
    fees = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zec'


class Zrx(models.Model):
    date = models.DateField(blank=True, primary_key=True, unique=True)
    txvolume = models.FloatField(blank=True, null=True)
    txcount = models.FloatField(blank=True, null=True)
    marketcap = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    exchangevolume = models.FloatField(blank=True, null=True)
    generatedcoins = models.FloatField(blank=True, null=True)
    fees = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zrx'
