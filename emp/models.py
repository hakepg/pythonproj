from django.db import models

class employee(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()

    class Meta:
        db_table= "empinfo"

# Create your models here.
