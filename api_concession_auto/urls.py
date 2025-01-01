from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register(r'concessions', views.ConcessionViewSet)
router.register(r'vehicules', views.VehiculeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('concessions/<int:concession_pk>/vehicules/', 
         views.ConcessionVehiculesViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='concession-vehicules-list'),
    path('concessions/<int:concession_pk>/vehicules/<int:pk>/',
         views.ConcessionVehiculesViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='concession-vehicules-detail'),
] 