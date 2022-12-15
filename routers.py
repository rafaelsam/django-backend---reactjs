from rest_framework import routers
from crud.viewsets import ProductViewSet
router = routers.SimpleRouter()
router.register(r'crud', ProductViewSet, basename='crud')

