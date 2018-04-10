from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=140)
    auteur = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title
