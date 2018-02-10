from rest_framework import serializers
from models import Bat, Bch, Bnb, Btc, Btg, Cyca, Dash, Dcr, Dgb, Doge, Eos, Etc, Eth, Fun, Gno, Gnt, Icx, Knc, Ltc, Omg, Pivx, Ppt, Rep, Salt, Snt, SpatialRefSys, Trx, Veri, Vtc, Wtc, Xem, Xmr, Xvg, Zec, Zrx


class BatSerializer(serializers.ModelSerializer):
	class Meta:
		model = Bat
		fields = ("__all__")

class BchSerializer(serializers.ModelSerializer):
	class Meta:
		model = Bch
		fields = ("__all__")

class BnbSerializer(serializers.ModelSerializer):
	class Meta:
		model = Bnb
		fields = ("__all__")

class BtcSerializer(serializers.ModelSerializer):
	class Meta:
		model = Btc
		fields = ("__all__")

class BtgSerializer(serializers.ModelSerializer):
	class Meta:
		model = Btg
		fields = ("__all__")

class CycaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cyca
		fields = ("__all__")

class DashSerializer(serializers.ModelSerializer):
	class Meta:
		model = Dash
		fields = ("__all__")

class DcrSerializer(serializers.ModelSerializer):
	class Meta:
		model = Dcr
		fields = ("__all__")

class DgbSerializer(serializers.ModelSerializer):
	class Meta:
		model = Dgb
		fields = ("__all__")

class DogeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Doge
		fields = ("__all__")

class EosSerializer(serializers.ModelSerializer):
	class Meta:
		model = Eos
		fields = ("__all__")

class EtcSerializer(serializers.ModelSerializer):
	class Meta:
		model = Etc
		fields = ("__all__")

class EthSerializer(serializers.ModelSerializer):
	class Meta:
		model = Eth
		fields = ("__all__")

class FunSerializer(serializers.ModelSerializer):
	class Meta:
		model = Fun
		fields = ("__all__")

class GnoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Gno
		fields = ("__all__")

class GntSerializer(serializers.ModelSerializer):
	class Meta:
		model = Gnt
		fields = ("__all__")

class IcxSerializer(serializers.ModelSerializer):
	class Meta:
		model = Icx
		fields = ("__all__")

class KncSerializer(serializers.ModelSerializer):
	class Meta:
		model = Knc
		fields = ("__all__")

class LtcSerializer(serializers.ModelSerializer):
	class Meta:
		model = Ltc
		fields = ("__all__")

class OmgSerializer(serializers.ModelSerializer):
	class Meta:
		model = Omg
		fields = ("__all__")

class PivxSerializer(serializers.ModelSerializer):
	class Meta:
		model = Pivx
		fields = ("__all__")

class PptSerializer(serializers.ModelSerializer):
	class Meta:
		model = Ppt
		fields = ("__all__")

class RepSerializer(serializers.ModelSerializer):
	class Meta:
		model = Rep
		fields = ("__all__")

class SaltSerializer(serializers.ModelSerializer):
	class Meta:
		model = Salt
		fields = ("__all__")

class SntSerializer(serializers.ModelSerializer):
	class Meta:
		model = Snt
		fields = ("__all__")

class SpatialRefSysSerializer(serializers.ModelSerializer):
	class Meta:
		model = SpatialRefSys
		fields = ("__all__")

class TrxSerializer(serializers.ModelSerializer):
	class Meta:
		model = Trx
		fields = ("__all__")

class VeriSerializer(serializers.ModelSerializer):
	class Meta:
		model = Veri
		fields = ("__all__")

class VtcSerializer(serializers.ModelSerializer):
	class Meta:
		model = Vtc
		fields = ("__all__")

class WtcSerializer(serializers.ModelSerializer):
	class Meta:
		model = Wtc
		fields = ("__all__")

class XemSerializer(serializers.ModelSerializer):
	class Meta:
		model = Xem
		fields = ("__all__")

class XmrSerializer(serializers.ModelSerializer):
	class Meta:
		model = Xmr
		fields = ("__all__")

class XvgSerializer(serializers.ModelSerializer):
	class Meta:
		model = Xvg
		fields = ("__all__")

class ZecSerializer(serializers.ModelSerializer):
	class Meta:
		model = Zec
		fields = ("__all__")

class ZrxSerializer(serializers.ModelSerializer):
	class Meta:
		model = Zrx
		fields = ("__all__")

