from django.db import models

from django.utils import timezone




class Article(models.Model):

    titre = models.CharField(max_length=200)

    contenu = models.TextField()

    date_publication = models.DateTimeField(default=timezone.now)

    auteur = models.CharField(max_length=100)


    def __str__(self):

        return self.titre
    

class Commentaire(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,related_name='commentaires')

    auteur = models.CharField(max_length=100) 

    text = models.TextField()

    date_creation = models.DateTimeField(default=timezone.now)

    def __str__(self):

        return f'Commentaire par {self.auteur} sur {self.article.titre}'   

