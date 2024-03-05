from django.db import models

# Create your models here.
from django.db.models import CASCADE


class ClientRegister_Model(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    gender= models.CharField(max_length=30)
    address= models.CharField(max_length=30)


class detect_attack(models.Model):


    RID= models.CharField(max_length=300)
    source_nodeip= models.CharField(max_length=300)
    destination_nodeip= models.CharField(max_length=300)
    start_time= models.CharField(max_length=300)
    source_port= models.CharField(max_length=300)
    destination_port= models.CharField(max_length=300)
    flags= models.CharField(max_length=300)
    site= models.CharField(max_length=300)
    asn= models.CharField(max_length=300)
    num_packets= models.CharField(max_length=300)
    num_bytes= models.CharField(max_length=300)
    flow_trajectories_ip= models.CharField(max_length=300)
    proto= models.CharField(max_length=300)
    prediction= models.CharField(max_length=300)


class detection_accuracy(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)

class detection_ratio(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)



