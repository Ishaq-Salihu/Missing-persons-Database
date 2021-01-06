from missingpersons.views import MissingApiView
from users.views import UserViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Missingperson', MissingApiView)
router.register('User', UserViewSet)

