from django.db import models
import uuid

# Create your models here.

class Database(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    input1 = models.CharField(max_length=100)
    input2 = models.CharField(max_length=100)
    input3 = models.CharField(max_length=100)
    input4 = models.CharField(max_length=100)
    input5 = models.CharField(max_length=100)
    input6 = models.CharField(max_length=100)
    input7 = models.CharField(max_length=100)
    # input8 = models.CharField(max_length=100)
    # input9 = models.CharField(max_length=100)
