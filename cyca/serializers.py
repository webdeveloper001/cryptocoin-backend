from rest_framework import serializers
from models import Bat, Bch, Bnb, Btc, Btg, Cyca, Dash, Dcr, Dgb, Doge, Eos, Etc, Eth, Fun, Gno, Gnt, Icx, Knc, Ltc, Omg, Pivx, Ppt, Rep, Salt, Snt, SpatialRefSys, Trx, Veri, Vtc, Wtc, Xem, Xmr, Xvg, Zec, Zrx


class BatSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Bat
		fields = ()

class BchSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Bch
		fields = ()

class BnbSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Bnb
		fields = ()

class BtcSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Btc
		fields = ()

class BtgSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Btg
		fields = ()

class CycaSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Cyca
		fields = ()

class DashSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Dash
		fields = ()

class DcrSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Dcr
		fields = ()

class DgbSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Dgb
		fields = ()

class DogeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Doge
		fields = ()

class EosSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Eos
		fields = ()

class EtcSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Etc
		fields = ()

class EthSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Eth
		fields = ()

class FunSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Fun
		fields = ()

class GnoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Gno
		fields = ()

class GntSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Gnt
		fields = ()

class IcxSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Icx
		fields = ()

class KncSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Knc
		fields = ()

class LtcSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Ltc
		fields = ()

class OmgSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Omg
		fields = ()

class PivxSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Pivx
		fields = ()

class PptSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Ppt
		fields = ()

class RepSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Rep
		fields = ()

class SaltSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Salt
		fields = ()

class SntSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Snt
		fields = ()

class SpatialRefSysSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = SpatialRefSys
		fields = ()

class TrxSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Trx
		fields = ()

class VeriSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Veri
		fields = ()

class VtcSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Vtc
		fields = ()

class WtcSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Wtc
		fields = ()

class XemSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Xem
		fields = ()

class XmrSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Xmr
		fields = ()

class XvgSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Xvg
		fields = ()

class ZecSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Zec
		fields = ()

class ZrxSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Zrx
		fields = ()

