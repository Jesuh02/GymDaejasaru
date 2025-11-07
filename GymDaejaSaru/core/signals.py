from django.db.models.signals import pre_save
from django.dispatch import receiver
from datetime import date, timedelta
from .models import ClienteMembresia


@receiver(pre_save, sender=ClienteMembresia)
def set_membresia_fechas(sender, instance, **kwargs):
    """
    Señal que se activa antes de guardar una membresía.
    Establece automáticamente:
    - Fecha inicio: hoy
    - Fecha fin: hoy + 30 días
    """
    # Solo si es una nueva membresía (no tiene pk)
    if not instance.pk:  # Nueva membresía
        # Establecer fecha inicio como hoy (si no está establecida)
        if not instance.clime_fecha_inicio:
            instance.clime_fecha_inicio = date.today()
        
        # Establecer fecha fin como fecha inicio + 30 días (si no está establecida)
        if not instance.clime_fecha_fin:
            fecha_base = instance.clime_fecha_inicio if instance.clime_fecha_inicio else date.today()
            instance.clime_fecha_fin = fecha_base + timedelta(days=30)

