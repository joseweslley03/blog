from django.db import models
from author.models import Author

class Publication (models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE, max_length=200)
    date_publication = models.DateField()
    pub_text = models.CharField(max_length=100)
    title = models.CharField(max_length=100)


    class Meta:
        db_table = 'publications'
