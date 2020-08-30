from django.db import models

# Create your models here.
class agent(models.Model):
    name = models.CharField(max_length=200,blank= True)
    agent_img = models.ImageField(upload_to='media/agent_img/%Y/%m/%d/',blank= True)
    number = models.CharField(max_length=200,blank= True)
    email = models.EmailField(max_length=200,blank= True)
    tweetsm = models.CharField(max_length=200,blank= True)
    fbooksm = models.CharField(max_length=200,blank= True)
    linksm = models.CharField(max_length=200,blank= True)
    def __str__(self):
        return self.name