from django.db import models

# Create your models here.
class todoModel(models.Model):
    id = models.IntegerField(primary_key=True)
    todo_title = models.CharField(max_length=50,primary_key=False)