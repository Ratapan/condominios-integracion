from django.db import models

# Create your models here.
class Residente(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    

class Casa(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.IntegerField()
    type_name = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    

class Existencia(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.IntegerField()
    type_name = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    date_init = models.DateTimeField()
    date_end = models.DateTimeField()

    
  