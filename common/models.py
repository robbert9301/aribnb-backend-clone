from django.db import models

# Create your models here.
# reuse model, bluepoint of model

class CommonModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta : #not put in database
        abstract = True