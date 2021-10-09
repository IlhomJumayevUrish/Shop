from django.db import models
from django.conf import settings

class Klent(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="klent")
    phone=models.CharField("Telefon",max_length=13)
    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name="Klent"
        verbose_name_plural="Klentlar"