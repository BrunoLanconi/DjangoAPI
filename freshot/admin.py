# Importing general functions
from django.contrib import admin

# Importing internal functions
from freshot.models import Atividade
from freshot.models import Aula
from freshot.models import Curso
from freshot.models import Materia
from freshot.models import Usuario
from freshot.models import AuxUsuarioAula


class Atividades(admin.ModelAdmin):
    list_display = ('id_atividade', 'data_cadastro', 'id_aula', 'matricula_usuario', 'data_final', 'titulo_atividade', 'descricao_atividade', 'fontes_atividade')
    list_display_links = ('id_atividade', 'data_cadastro', 'id_aula', 'matricula_usuario', 'data_final', 'titulo_atividade', 'descricao_atividade', 'fontes_atividade')


class Aulas(admin.ModelAdmin):
    list_display = ('id_aula', 'id_curso', 'id_materia', 'semestre')
    list_display_links = ('id_aula', 'id_curso', 'id_materia', 'semestre')


class Cursos(admin.ModelAdmin):
    list_display = ('id_curso', 'nome_curso')
    list_display_links = ('id_curso', 'nome_curso')


class Materias(admin.ModelAdmin):
    list_display = ('id_materia', 'nome_materia')
    list_display_links = ('id_materia', 'nome_materia')


class Usuarios(admin.ModelAdmin):
    list_display = ('matricula_usuario', 'id_curso', 'nome_usuario', 'senha_usuario', 'email_usuario', 'matricula_responsavel')
    list_display_links = ('matricula_usuario', 'id_curso', 'nome_usuario', 'senha_usuario', 'email_usuario', 'matricula_responsavel')


class AuxUsuarioAulas(admin.ModelAdmin):
    list_display = ('id_vinculacao', 'matricula_usuario', 'id_aula')
    list_display_links = ('id_vinculacao', 'matricula_usuario', 'id_aula')


admin.site.register(Atividade, Atividades)
admin.site.register(Aula, Aulas)
admin.site.register(Curso, Cursos)
admin.site.register(Materia, Materias)
admin.site.register(Usuario, Usuarios)
admin.site.register(AuxUsuarioAula, AuxUsuarioAulas)

