from django.db import models

# Create your models here.
class Trainer(models.Model):

    name = models.CharField(max_length=128, blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
