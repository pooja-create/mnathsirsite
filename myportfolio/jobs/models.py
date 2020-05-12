from django.db import models

# Create your models here.
class categorytable(models.Model):
       category=models.CharField(max_length=100) 
       def __str__(self):
             return(self.category)
      
class job(models.Model):
      title=models.CharField(max_length=100)
      summary=models.TextField(max_length=400)
      image=models.ImageField(max_length=200)
      category=models.ForeignKey(categorytable,on_delete=models.CASCADE)
      def summary1(self):
            return(self.summary[:30])
      def __str__(self):
            return(self.title)

    