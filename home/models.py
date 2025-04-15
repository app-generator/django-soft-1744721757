# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Morador(models.Model):

    #__Morador_FIELDS__
    nome = models.CharField(max_length=255, null=True, blank=True)
    cpf = models.CharField(max_length=255, null=True, blank=True)
    teltefone = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    status_moradia = models.CharField(max_length=255, null=True, blank=True)
    descricao_moradia = models.CharField(max_length=255, null=True, blank=True)
    celular = models.CharField(max_length=255, null=True, blank=True)

    #__Morador_FIELDS__END

    class Meta:
        verbose_name        = _("Morador")
        verbose_name_plural = _("Morador")


class Residencia(models.Model):

    #__Residencia_FIELDS__
    apto = models.CharField(max_length=255, null=True, blank=True)

    #__Residencia_FIELDS__END

    class Meta:
        verbose_name        = _("Residencia")
        verbose_name_plural = _("Residencia")


class Morador_Residencia(models.Model):

    #__Morador_Residencia_FIELDS__
    morador_id = models.ForeignKey(morador, on_delete=models.CASCADE)
    residencia_id = models.ForeignKey(residencia, on_delete=models.CASCADE)

    #__Morador_Residencia_FIELDS__END

    class Meta:
        verbose_name        = _("Morador_Residencia")
        verbose_name_plural = _("Morador_Residencia")



#__MODELS__END
