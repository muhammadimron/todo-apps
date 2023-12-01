from rest_framework.routers import SimpleRouter
from api.viewsets import RegisterViewset, PersonViewset

router = SimpleRouter()
router.register(r'register', RegisterViewset, basename="register")
router.register(r'person', PersonViewset, basename="person")
urlpatterns = router.urls
