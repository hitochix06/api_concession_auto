from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers
from api.views import ConcessionViewSet, VehiculeViewSet

router = routers.DefaultRouter()
router.register(r'concessions', ConcessionViewSet)

concessions_router = routers.NestedDefaultRouter(router, r'concessions', lookup='concession')
concessions_router.register(r'vehicules', VehiculeViewSet, basename='concession-vehicules')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include(concessions_router.urls)),
] 