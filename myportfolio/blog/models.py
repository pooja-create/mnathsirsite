from django.db import models

# Create your models here.
class blog(models.Model):
    title=models.CharField(max_length=100)
    pubdate=models.DateTimeField()
    image=models.ImageField(upload_to='images/')
    body=models.TextField()
    def summary(self):
        return(self.body[:60])
    def pubdate1(self):
        return(self.pubdate.strftime("%d %B, %Y"))
    def __str__(self):
        return(self.title)