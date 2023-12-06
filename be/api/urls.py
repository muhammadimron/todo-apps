from rest_framework.routers import SimpleRouter
from api.viewsets import RegisterViewset, PersonViewset, PersonAllViewset, ProjectViewset

router = SimpleRouter()
router.register(r'register', RegisterViewset, basename="register")
router.register(r'person', PersonViewset, basename="person")
router.register(r'personAll', PersonAllViewset, basename="personAll")
router.register(r'project', ProjectViewset, basename="project")
urlpatterns = router.urls
