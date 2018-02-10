from rest_framework import serializers
from models import Bat, Bch, Bnb, Btc, Btg, Cyca, Dash, Dcr, Dgb, Doge, Eos, Etc, Eth, Fun, Gno, Gnt, Icx, Knc, Ltc, Omg, Pivx, Ppt, Rep, Salt, Snt, SpatialRefSys, Trx, Veri, Vtc, Wtc, Xem, Xmr, Xvg, Zec, Zrx


class BatSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Bat
		fields = ("__all__")

class BchSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Bch
		fields = ("__all__")

class BnbSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Bnb
		fields = ("__all__")

class BtcSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Btc
		fields = ("__all__")

class BtgSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Btg
		fields = ("__all__")

class CycaSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Cyca
		fields = ("__all__")

class DashSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Dash
		fields = ("__all__")

class DcrSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Dcr
		fields = ("__all__")

class DgbSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Dgb
		fields = ("__all__")

class DogeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Doge
		fields = ("__all__")

class EosSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Eos
		fields = ("__all__")

class EtcSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Etc
		fields = ("__all__")

class EthSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Eth
		fields = ("__all__")

class FunSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Fun
		fields = ("__all__")

class GnoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Gno
		fields = ("__all__")

class GntSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Gnt
		fields = ("__all__")

class IcxSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Icx
		fields = ("__all__")

class KncSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Knc
		fields = ("__all__")

class LtcSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Ltc
		fields = ("__all__")

class OmgSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Omg
		fields = ("__all__")

class PivxSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Pivx
		fields = ("__all__")

class PptSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Ppt
		fields = ("__all__")

class RepSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Rep
		fields = ("__all__")

class SaltSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Salt
		fields = ("__all__")

class SntSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Snt
		fields = ("__all__")

class SpatialRefSysSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = SpatialRefSys
		fields = ("__all__")

class TrxSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Trx
		fields = ("__all__")

class VeriSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Veri
		fields = ("__all__")

class VtcSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Vtc
		fields = ("__all__")

class WtcSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Wtc
		fields = ("__all__")

class XemSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Xem
		fields = ("__all__")

class XmrSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Xmr
		fields = ("__all__")

class XvgSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Xvg
		fields = ("__all__")

class ZecSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Zec
		fields = ("__all__")

class ZrxSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Zrx
		fields = ("__all__")

