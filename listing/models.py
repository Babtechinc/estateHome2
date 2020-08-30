from django.db import models
from agent.models import agent
# Create your models here.
deal = {
    ('sale','sale'),
('rent','rent'),
}
class  listi_ng(models.Model):
    street = models.CharField(max_length=200)
    agent = models.ForeignKey( agent,on_delete=models.CASCADE)
    street_img = models.ImageField(upload_to='property_img/%Y/%m/%d/', blank=True)
    deal =models.CharField(max_length=45,choices=deal,default='rent')
    type_listing = models.CharField(max_length=200)
    SqFt = models.DecimalField(max_digits=40, decimal_places=2)
    price= models.DecimalField( max_digits=40, decimal_places=2)
    bathroom = models.IntegerField()
    bedrooms = models.IntegerField()
    detail1=models.CharField(max_length=2000,default='op')
    location = models.CharField(max_length=2000,default='Epe')

    def __str__(self):
        return self.street