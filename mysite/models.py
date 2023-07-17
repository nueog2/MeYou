from django.db import models

# Create your models here.
from django.db import models

class MainContent(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return f'{self.price}₩'

    pub_date = models.DateTimeField('date published')