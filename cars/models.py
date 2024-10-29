from django.db import models

# Create your models here.
class brand(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name
class Car(models.Model):
    id=models.AutoField(primary_key=True)
    model=models.CharField(max_length=200)
    brand=models.ForeignKey(brand,on_delete=models.PROTECT,related_name='brands')
    factory_year=models.IntegerField(blank=True,null=True)
    model_year=models.IntegerField(blank=True,null=True)
    plate=models.CharField(max_length=10,blank=True,null=True)
    value=models.FloatField(blank=True,null=True)
    photo=models.ImageField(upload_to='cars/',blank=True,null=True)
    def __str__(self):
        return self.model