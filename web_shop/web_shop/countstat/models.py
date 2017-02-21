from django.db import models

class Statistic(models.Model):
    #category = models.CharField(verbose_name='Category', max_length=50)
    #product  = models.CharField(verbose_name='Product', max_length=50)

    class Meta:
        managed = False
