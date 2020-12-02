# Importing general functions
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

# Importing internal functions
from freshot.views import AtividadesViewSet
from freshot.views import AulasViewSet
from freshot.views import CursosViewSet
from freshot.views import MateriasViewSet
from freshot.views import UsuariosViewSet
from freshot.views import AuxUsuarioAulasViewSet

# Defining internal variables
router = routers.DefaultRouter()

# Relating views and paths
router.register(r'atividades', AtividadesViewSet)
router.register(r'aulas', AulasViewSet)
router.register(r'cursos', CursosViewSet)
router.register(r'materias', MateriasViewSet)
router.register(r'usuarios', UsuariosViewSet)
router.register(r'auxusuarioaulas', AuxUsuarioAulasViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
