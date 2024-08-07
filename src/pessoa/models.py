from django.db import models

# Create your models here.
class Pessoa(models.Model):
    pessoa_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    name_father = models.CharField(max_length=60)
    name_mother = models.CharField(max_length=60)
    date_born = models.DateField()
    salary = models.DecimalField(max_digits=10,decimal_places=2)
    cpf = models.CharField(max_length=14,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)