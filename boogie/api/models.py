from django.db import models
# this is the schema 
class Note(models.Model):
    body =models.TextField()
    updated =models.DateTimeField(auto_now=True)
    created =models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.body[0:50]
    class Meta:
        ordering =['-updated']
        
class Users(models.Model):
    userName =models.CharField( max_length=50)    
    email =models.EmailField(max_length=254)    
    password =models.CharField(max_length=50)
    
    def __str__(self):
        return self.userName
    
    
    
    
# Create your models here.
