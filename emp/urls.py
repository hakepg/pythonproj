from rest_framework.routers import SimpleRouter
from .views import EmpViewSet


# Routers provide an easy way of automatically determining the URL conf.
router = SimpleRouter()
router.register(r'employees', EmpViewSet)
urlpatterns=router.urls
