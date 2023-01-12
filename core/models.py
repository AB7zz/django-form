from django.db import models
import uuid

# Create your models here.

class Database(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    schcol = models.CharField(max_length=100)
    uni = models.CharField(max_length=100)
    seds = models.CharField(max_length=100)
    proof = models.ImageField(upload_to = 'proof_images')
    # input8 = models.CharField(max_length=100)
    # input9 = models.CharField(max_length=100)
