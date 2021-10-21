from rest_framework import routers

from application.views import CurrencyViewSet

router = routers.DefaultRouter()
router.register('api/v1/quotes', CurrencyViewSet, 'currency')

urlpatterns = router.urls
