# Importing general functions
from django.db import models


# Defining models
class Materia(models.Model):
    id_materia = models.IntegerField(primary_key=True)
    nome_materia = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.nome_materia


class Curso(models.Model):
    id_curso = models.IntegerField(primary_key=True)
    nome_curso = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.nome_curso

class Usuario(models.Model):
    matricula_usuario = models.IntegerField(primary_key=True)
    matricula_responsavel = models.IntegerField(null=True)
    id_curso = models.IntegerField(null=True)
    nome_usuario = models.CharField(max_length=30, null=True)
    senha_usuario = models.CharField(max_length=30, null=True)
    email_usuario = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.nome_usuario


class Aula(models.Model):
    id_aula = models.IntegerField(primary_key=True)
    id_curso = models.IntegerField(null=True)
    id_materia = models.IntegerField(null=True)
    semestre = models.IntegerField(null=True)


class Atividade(models.Model):
    id_atividade = models.IntegerField(primary_key=True)
    id_aula = models.IntegerField(null=True)
    matricula_usuario = models.IntegerField(null=True)
    data_cadastro = models.DateField(max_length=30, null=True)
    data_final = models.DateField(max_length=30, null=True)
    titulo_atividade = models.CharField(max_length=30, null=True)
    descricao_atividade = models.CharField(max_length=30, null=True)
    fontes_atividade = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.titulo_atividade


class AuxUsuarioAula(models.Model):
    id_vinculacao = models.IntegerField(primary_key=True)
    matricula_usuario = models.IntegerField(null=True)
    id_aula = models.IntegerField(null=True)

    def __str__(self):
        return self.id_vinculacao
