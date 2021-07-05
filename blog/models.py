from django.conf import settings
from django.db import models
from django.utils import timezone



class production_pvrmt(models.Model):
    dt_utc = models.DateTimeField(primary_key=True)
    Charge = models.FloatField(db_column='Charge')  # Field name made lowercase.
    Decharge = models.FloatField(db_column='Decharge')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'production_pvrmt'