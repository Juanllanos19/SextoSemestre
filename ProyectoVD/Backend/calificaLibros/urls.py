from django.urls import path
#from .views import index
from rest_framework import routers
from .views import LibrosViewSet
from .views import AutoresViewSet
from .views import GenerosViewSet
from .views import UsuariosViewSet
from .views import CalificacionesViewSet
#urlpatterns = [
#    path('',index,name="index")
#]

router = routers.DefaultRouter()
router.register('libros',LibrosViewSet)
router.register('autores',AutoresViewSet)
router.register('generos',GenerosViewSet)
router.register('usuarios',UsuariosViewSet)
router.register('calificaciones',CalificacionesViewSet)

urlpatterns = router.urls