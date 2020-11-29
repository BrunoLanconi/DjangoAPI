from rest_framework import serializers
from freshot.models import Atividade
from freshot.models import Aula
from freshot.models import Curso
from freshot.models import Materia
from freshot.models import Usuario
from freshot.models import AuxUsuarioAula


class AtividadeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Atividade
        fields = ['id_atividade', 'data_cadastro', 'id_aula', 'matricula_usuario', 'data_final', 'titulo_atividade', 'descricao_atividade', 'fontes_atividade']


class AulaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Aula
        fields = ['id_aula', 'semestre']


class CursoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Curso
        fields = ['id_curso', 'nome_curso']


class MateriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Materia
        fields = ['id_aula', 'id_curso', 'id_materia', 'semestre']


class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = ['matricula_usuario', 'id_curso', 'nome_usuario', 'senha_usuario', 'email_usuario',
                  'matricula_responsavel']


class AuxUsuarioAulaSerializer(serializers.ModelSerializer):

    class Meta:
        model = AuxUsuarioAula
        fields = ['id_vinculacao', 'matricula_usuario', 'id_aula']
