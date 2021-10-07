from django.db import models


class Curso(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    thumb = models.ImageField(upload_to="thumb_cursos")

    def __str__(self) -> str:
        return self.nome


class Aula(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    aula = models.FileField(upload_to="aulas")
    curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.nome
