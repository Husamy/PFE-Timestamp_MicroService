from django.db import models


# Create your models here.
class user_timestamp(models.Model):
    owner = models.EmailField()
    user_id = models.IntegerField()
    action = models.CharField(max_length=10)
    created_date = models.DateField()
    created_time = models.TimeField()

    def __str__(self) -> str:
        return self.email
    
class document_timestamp(models.Model):
    action = models.CharField(max_length=30)
    document_id = models.IntegerField()
    owner = models.EmailField(max_length=30)
    user_id = models.IntegerField()
    created_date = models.DateField()
    created_time = models.TimeField()

    def __str__(self) -> str:
        return self.document_id
    

class organisation_timestamp(models.Model):
    action = models.CharField(max_length=20)
    organisation = models.CharField(max_length=30)
    owner = models.EmailField(max_length=30)
    user_id = models.IntegerField()
    created_date = models.DateField()
    created_time = models.TimeField()

    def __str__(self) -> str:
        return self.organisation_id
    