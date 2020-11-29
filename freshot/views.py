from rest_framework import viewsets
from freshot.models import Atividade
from freshot.serializer import AtividadeSerializer
from freshot.models import Aula
from freshot.serializer import AulaSerializer
from freshot.models import Curso
from freshot.serializer import CursoSerializer
from freshot.models import Materia
from freshot.serializer import MateriaSerializer
from freshot.models import Usuario
from freshot.serializer import UsuarioSerializer
from freshot.models import AuxUsuarioAula
from freshot.serializer import AuxUsuarioAulaSerializer


class AuxUsuarioAulasViewSet(viewsets.ModelViewSet):
    queryset = AuxUsuarioAula.objects.all()
    serializer_class = AuxUsuarioAulaSerializer


class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class MateriasViewSet(viewsets.ModelViewSet):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer


class CursosViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class AulasViewSet(viewsets.ModelViewSet):
    queryset = Aula.objects.all()
    serializer_class = AulaSerializer


class AtividadesViewSet(viewsets.ModelViewSet):
    queryset = Atividade.objects.all()
    serializer_class = AtividadeSerializer