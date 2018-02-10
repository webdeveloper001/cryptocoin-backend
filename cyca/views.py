# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from django.http import HttpResponse
from django.apps import apps
import pandas as pd
import pprint
import json

from serializers import BatSerializer, BchSerializer, BnbSerializer, BtcSerializer, BtgSerializer, CycaSerializer, DashSerializer, DcrSerializer, DgbSerializer, DogeSerializer, EosSerializer, EtcSerializer, EthSerializer, FunSerializer, GnoSerializer, GntSerializer, IcxSerializer, KncSerializer, LtcSerializer, OmgSerializer, PivxSerializer, PptSerializer, RepSerializer, SaltSerializer, SntSerializer, SpatialRefSysSerializer, TrxSerializer, VeriSerializer, VtcSerializer, WtcSerializer, XemSerializer, XmrSerializer, XvgSerializer, ZecSerializer, ZrxSerializer
from models import Bat, Bch, Bnb, Btc, Btg, Cyca, Dash, Dcr, Dgb, Doge, Eos, Etc, Eth, Fun, Gno, Gnt, Icx, Knc, Ltc, Omg, Pivx, Ppt, Rep, Salt, Snt, SpatialRefSys, Trx, Veri, Vtc, Wtc, Xem, Xmr, Xvg, Zec, Zrx


class BatViewSet(viewsets.ModelViewSet):
	queryset = Bat.objects.all()
	serializer_class = BatSerializer

class BchViewSet(viewsets.ModelViewSet):
	queryset = Bch.objects.all()
	serializer_class = BchSerializer

class BnbViewSet(viewsets.ModelViewSet):
	queryset = Bnb.objects.all()
	serializer_class = BnbSerializer

class BtcViewSet(viewsets.ModelViewSet):
	queryset = Btc.objects.all()
	serializer_class = BtcSerializer

class BtgViewSet(viewsets.ModelViewSet):
	queryset = Btg.objects.all()
	serializer_class = BtgSerializer

class CycaViewSet(viewsets.ModelViewSet):
	queryset = Cyca.objects.all()
	serializer_class = CycaSerializer

class DashViewSet(viewsets.ModelViewSet):
	queryset = Dash.objects.all()
	serializer_class = DashSerializer

class DcrViewSet(viewsets.ModelViewSet):
	queryset = Dcr.objects.all()
	serializer_class = DcrSerializer

class DgbViewSet(viewsets.ModelViewSet):
	queryset = Dgb.objects.all()
	serializer_class = DgbSerializer

class DogeViewSet(viewsets.ModelViewSet):
	queryset = Doge.objects.all()
	serializer_class = DogeSerializer

class EosViewSet(viewsets.ModelViewSet):
	queryset = Eos.objects.all()
	serializer_class = EosSerializer

class EtcViewSet(viewsets.ModelViewSet):
	queryset = Etc.objects.all()
	serializer_class = EtcSerializer

class EthViewSet(viewsets.ModelViewSet):
	queryset = Eth.objects.all()
	serializer_class = EthSerializer

class FunViewSet(viewsets.ModelViewSet):
	queryset = Fun.objects.all()
	serializer_class = FunSerializer

class GnoViewSet(viewsets.ModelViewSet):
	queryset = Gno.objects.all()
	serializer_class = GnoSerializer

class GntViewSet(viewsets.ModelViewSet):
	queryset = Gnt.objects.all()
	serializer_class = GntSerializer

class IcxViewSet(viewsets.ModelViewSet):
	queryset = Icx.objects.all()
	serializer_class = IcxSerializer

class KncViewSet(viewsets.ModelViewSet):
	queryset = Knc.objects.all()
	serializer_class = KncSerializer

class LtcViewSet(viewsets.ModelViewSet):
	queryset = Ltc.objects.all()
	serializer_class = LtcSerializer

class OmgViewSet(viewsets.ModelViewSet):
	queryset = Omg.objects.all()
	serializer_class = OmgSerializer

class PivxViewSet(viewsets.ModelViewSet):
	queryset = Pivx.objects.all()
	serializer_class = PivxSerializer

class PptViewSet(viewsets.ModelViewSet):
	queryset = Ppt.objects.all()
	serializer_class = PptSerializer

class RepViewSet(viewsets.ModelViewSet):
	queryset = Rep.objects.all()
	serializer_class = RepSerializer

class SaltViewSet(viewsets.ModelViewSet):
	queryset = Salt.objects.all()
	serializer_class = SaltSerializer

class SntViewSet(viewsets.ModelViewSet):
	queryset = Snt.objects.all()
	serializer_class = SntSerializer

class SpatialRefSysViewSet(viewsets.ModelViewSet):
	queryset = SpatialRefSys.objects.all()
	serializer_class = SpatialRefSysSerializer

class TrxViewSet(viewsets.ModelViewSet):
	queryset = Trx.objects.all()
	serializer_class = TrxSerializer

class VeriViewSet(viewsets.ModelViewSet):
	queryset = Veri.objects.all()
	serializer_class = VeriSerializer

class VtcViewSet(viewsets.ModelViewSet):
	queryset = Vtc.objects.all()
	serializer_class = VtcSerializer

class WtcViewSet(viewsets.ModelViewSet):
	queryset = Wtc.objects.all()
	serializer_class = WtcSerializer

class XemViewSet(viewsets.ModelViewSet):
	queryset = Xem.objects.all()
	serializer_class = XemSerializer

class XmrViewSet(viewsets.ModelViewSet):
	queryset = Xmr.objects.all()
	serializer_class = XmrSerializer

class XvgViewSet(viewsets.ModelViewSet):
	queryset = Xvg.objects.all()
	serializer_class = XvgSerializer

class ZecViewSet(viewsets.ModelViewSet):
	queryset = Zec.objects.all()
	serializer_class = ZecSerializer

class ZrxViewSet(viewsets.ModelViewSet):
	queryset = Zrx.objects.all()
	serializer_class = ZrxSerializer


def correlation(request, from_currency, to_currency):
	one = apps.get_model(app_label='cyca', model_name=from_currency.title())
	other = apps.get_model(app_label='cyca', model_name=to_currency.title())
	exec("one_serializer = "+ from_currency.title() + "Serializer(one.objects.all(), many=True)")
	exec("other_serializer = "+to_currency.title() + "Serializer(other.objects.all(), many=True)")
	one_data = one_serializer.data
	other_data = other_serializer.data
	one_df = pd.DataFrame(one_data)
	other_df = pd.DataFrame(other_data)
	data = one_df.loc[:, 'txvolume':].rolling(3).corr(other_df.loc[:,'txvolume':]).to_json()
	return HttpResponse(data)

