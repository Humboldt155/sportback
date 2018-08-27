from django.db import models

# from django.contrib.auth import get_user_model
# User = get_user_model()


class Sport(models.Model):
    ru_name = models.CharField(max_length=64, unique=True, blank=False, null=False)
    ru_description = models.CharField(max_length=128, blank=True, null=True)
    en_name = models.CharField(max_length=64, unique=True, blank=False, null=False)
    en_description = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        ordering = ('ru_name',)

    def __str__(self):
        return self.ru_name


class SportGroup(models.Model):
    ru_name = models.CharField(max_length=64, unique=True, blank=False, null=False)
    ru_description = models.CharField(max_length=128, blank=True, null=True)
    en_name = models.CharField(max_length=64, unique=True, blank=False, null=False)
    en_description = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        ordering = ('ru_name',)

    def __str__(self):
        return self.ru_name


class SportSubGroup(models.Model):
    ru_name = models.CharField(max_length=64, unique=True, blank=False, null=False)
    ru_description = models.CharField(max_length=128, blank=True, null=True)
    en_name = models.CharField(max_length=64, unique=True, blank=False, null=False)
    en_description = models.CharField(max_length=128, blank=True, null=True)
    sport_group = models.ForeignKey(SportGroup, on_delete=models.CASCADE)
    sports = models.ManyToManyField(Sport, related_name='sport_sub_groups')

    class Meta:
        ordering = ('ru_name',)

    def __str__(self):
        return self.ru_name


class SportType(models.Model):
    ru_name = models.CharField(max_length=64)
    ru_description = models.CharField(max_length=128, blank=True, null=True)
    en_name = models.CharField(max_length=64)
    en_description = models.CharField(max_length=128, blank=True, null=True)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)

    class Meta:
        ordering = ('ru_name',)

    def __str__(self):
        return self.ru_name

