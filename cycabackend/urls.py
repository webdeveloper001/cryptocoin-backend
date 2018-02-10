"""cycabackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from cyca import views

router = routers.DefaultRouter()


router.register(r'bat', views.BatViewSet)
router.register(r'bch', views.BchViewSet)
router.register(r'bnb', views.BnbViewSet)
router.register(r'btc', views.BtcViewSet)
router.register(r'btg', views.BtgViewSet)
router.register(r'cyca', views.CycaViewSet)
router.register(r'dash', views.DashViewSet)
router.register(r'dcr', views.DcrViewSet)
router.register(r'dgb', views.DgbViewSet)
router.register(r'doge', views.DogeViewSet)
router.register(r'eos', views.EosViewSet)
router.register(r'etc', views.EtcViewSet)
router.register(r'eth', views.EthViewSet)
router.register(r'fun', views.FunViewSet)
router.register(r'gno', views.GnoViewSet)
router.register(r'gnt', views.GntViewSet)
router.register(r'icx', views.IcxViewSet)
router.register(r'knc', views.KncViewSet)
router.register(r'ltc', views.LtcViewSet)
router.register(r'omg', views.OmgViewSet)
router.register(r'pivx', views.PivxViewSet)
router.register(r'ppt', views.PptViewSet)
router.register(r'rep', views.RepViewSet)
router.register(r'salt', views.SaltViewSet)
router.register(r'snt', views.SntViewSet)
router.register(r'spatialRefSys', views.SpatialRefSysViewSet)
router.register(r'trx', views.TrxViewSet)
router.register(r'veri', views.VeriViewSet)
router.register(r'vtc', views.VtcViewSet)
router.register(r'wtc', views.WtcViewSet)
router.register(r'xem', views.XemViewSet)
router.register(r'xmr', views.XmrViewSet)
router.register(r'xvg', views.XvgViewSet)
router.register(r'zec', views.ZecViewSet)
router.register(r'zrx', views.ZrxViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^corr/(?P<from_currency>\w{0,5})/(?P<to_currency>\w{0,50})/$', views.correlation)
]
