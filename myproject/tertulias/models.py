from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Tertulia(models.Model):
    tertulia_name = models.CharField(max_length=100)
    tertulia_banner = models.ImageField(default='fallback.png', blank=True)
    tertulia_description = models.TextField(max_length=450, blank=True)
    tertulia_address = models.CharField(max_length=250, blank=True, null=True)
    tertulia_horario = models.CharField(max_length=100)
    tertulia_fecha_de_inicio = models.DateField(auto_now_add=False, auto_now=False, null=True)
    tertulia_sesiones = models.PositiveSmallIntegerField()
    tertulia_encargado_picture = models.ImageField(default='alonso.jpg', blank=True)
    tertulia_encargado = models.CharField(max_length=100)
    tertulia_lugares = models.PositiveIntegerField(blank=True, null=True)
    slug = models.IntegerField(default=0)

    def __str__(self):
        return self.tertulia_name

@receiver(post_save, sender=Tertulia)
def slug_generator(sender, instance, created, **kwargs):
    if created and not instance.slug:
        instance.slug = instance.id
        instance.save()