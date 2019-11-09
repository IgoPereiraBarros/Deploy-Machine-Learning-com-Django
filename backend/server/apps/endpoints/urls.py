from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .views import EndPointViewSet
from .views import MLAlgorithmViewSet
from .views import MLAlgorithmStatusViewSet
from .views import MLRequestViewSet
from .views import PredictView
from .views import ABTestViewSet
from .views import StopABTestView

router = DefaultRouter(trailing_slash=False)
router.register('endpoints', EndPointViewSet, basename='endpoints')
router.register('mlalgorithms', MLAlgorithmViewSet, basename='mlalgorithms')
router.register('mlalgorithmstatuses', MLAlgorithmStatusViewSet, basename='mlalgorithmstatuses')
router.register('mlrequests', MLRequestViewSet, basename='mlrequests')
router.register('abtests', ABTestViewSet, basename='abtests')

urlpatterns = [
    url('^api/v1/', include(router.urls)),
    url('^api/v1/(?P<endpoint_name>.+)/predict$', PredictView.as_view(), name='predict'), # predict url
    url('^api/v1/stop_ab_test/(?P<ab_test_id>.+)', StopABTestView.as_view(), name='stop_ab')
]
