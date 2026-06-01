from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import MarcaViewSet, VehiculoViewSet
from .triangle_views import calcular_area_triangulo
from .sale_views import promedio_ventas

router = DefaultRouter()
router.register(r"marcas", MarcaViewSet, basename="marcas")
router.register(r"vehiculos", VehiculoViewSet, basename="vehiculos")

urlpatterns = []
urlpatterns += router.urls
urlpatterns.append(
    path(
        'triangle/area/',
        calcular_area_triangulo,
        name='triangle-area'
    ),
    path(
        'products/promedio-ventas/',
        promedio_ventas,
        name='promedio-ventas'
    ),
)