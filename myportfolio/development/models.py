from django.db import models

# Create your models here.
class categorytable(models.Model):
       category=models.CharField(max_length=100) 
       def __str__(self):
             return(self.category)
class development(models.Model):
    title=models.CharField(max_length=100)
    projectimage=models.ImageField(upload_to='images/')
    description=models.TextField()
    technology=models.CharField(max_length=500)
    category=models.ForeignKey(categorytable,on_delete=models.CASCADE)
    def des(self):
        return(self.description[:26])
    def __str__(self):
        return(self.title)