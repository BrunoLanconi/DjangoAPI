from django.db import models


class Materia(models.Model):
    id_materia = models.IntegerField(null=True)
    nome_materia = models.DateField(max_length=30, null=True)

    def __str__(self):
        return self.id_materia


class Curso(models.Model):
    id_curso = models.IntegerField(null=True)
    nome_curso = models.DateField(max_length=30, null=True)

    def __str__(self):
        return self.id_curso


class Usuario(models.Model):
    matricula_usuario = models.IntegerField(null=True)
    id_curso = models.IntegerField(null=True)
    nome_usuario = models.DateField(max_length=30, null=True)
    senha_usuario = models.DateField(max_length=30, null=True)
    email_usuario = models.CharField(max_length=30, null=True)
    matricula_responsavel = models.IntegerField(null=True)

    def __str__(self):
        return self.matricula_usuario


class Aula(models.Model):
    id_aula = models.IntegerField(null=True)
    id_curso = models.IntegerField(null=True)
    id_materia = models.IntegerField(null=True)
    semestre = models.IntegerField(null=True)

    def __str__(self):
        return self.id_aula


class Atividade(models.Model):
    id_atividade = models.IntegerField(null=True)
    id_aula = models.IntegerField(null=True)
    matricula_usuario = models.IntegerField(null=True)
    data_cadastro = models.DateField(max_length=30, null=True)
    data_final = models.DateField(max_length=30, null=True)
    titulo_atividade = models.CharField(max_length=30, null=True)
    descricao_atividade = models.CharField(max_length=30, null=True)
    fontes_atividade = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.id_atividade


class AuxUsuarioAula(models.Model):
    id_vinculacao = models.IntegerField(null=True)
    matricula_usuario = models.IntegerField(null=True)
    id_aula = models.IntegerField(null=True)

    def __str__(self):
        return self.id_vinculacao