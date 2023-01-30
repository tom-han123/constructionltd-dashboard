from django.db import models
from django.utils import timezone

#acc

class acc_register(models.Model):
    acc_id = models.AutoField(db_column="User ID", primary_key=True)
    phone = models.CharField(db_column="Phone", max_length=50)
    password = models.CharField(db_column="Password", max_length=50)

    def __str__(self):
        return self.phone
