from django.db import models

class DatosMaestros(models.Model):
    dama_id = models.AutoField(primary_key=True, db_column='DAMA_ID')
    dama_nombre = models.CharField(max_length=100, db_column='DAMA_NOMBRE')
    dama_valor = models.CharField(max_length=100, db_column='DAMA_VALOR')
    dama_padre_id = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='hijos_padre', db_column='DAMA_PADRE_ID')
    dama_dependencia_id = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='hijos_dependencia', db_column='DAMA_DEPENDENCIA_ID')
    dama_estado = models.IntegerField(default=1, db_column='DAMA_ESTADO')

    class Meta:
        db_table = 'TBL_DATOS_MAESTROS'
        verbose_name = 'Dato Maestro'
        verbose_name_plural = 'Datos Maestros'

    def __str__(self):
        return f"{self.dama_nombre} ({self.dama_valor})"


class Entrenador(models.Model):
    entr_id = models.AutoField(primary_key=True, db_column='ENTR_ID')
    entr_nombre = models.CharField(max_length=100, db_column='ENTR_NOMBRE')
    entr_fecha_nacimiento = models.DateField(null=True, blank=True, db_column='ENTR_FECHA_NACIMIENTO')
    entr_telefono = models.CharField(max_length=15, null=True, blank=True, db_column='ENTR_TELEFONO')
    entr_direccion = models.CharField(max_length=150, null=True, blank=True, db_column='ENTR_DIRECCION')
    entr_numero_documento = models.CharField(max_length=20, null=True, blank=True, db_column='ENTR_NUMERO_DOCUMENTO')
    dama_tipo_documento = models.ForeignKey(DatosMaestros, on_delete=models.SET_NULL, null=True, related_name='entrenadores', db_column='DAMA_TIPO_DOCUMENTO')

    class Meta:
        db_table = 'TBL_ENTRENADORES'
        verbose_name = 'Entrenador'
        verbose_name_plural = 'Entrenadores'

    def __str__(self):
        return self.entr_nombre


class Cliente(models.Model):
    clie_id = models.AutoField(primary_key=True, db_column='CLIE_ID')
    clie_nombre = models.CharField(max_length=100, db_column='CLIE_NOMBRE')
    clie_fecha_nacimiento = models.DateField(null=True, blank=True, db_column='CLIE_FECHA_NACIMIENTO')
    clie_telefono = models.CharField(max_length=15, null=True, blank=True, db_column='CLIE_TELEFONO')
    clie_direccion = models.CharField(max_length=150, null=True, blank=True, db_column='CLIE_DIRECCION')
    clie_numero_documento = models.CharField(max_length=20, null=True, blank=True, db_column='CLIE_NUMERO_DOCUMENTO')
    dama_tipo_documento = models.ForeignKey(DatosMaestros, on_delete=models.SET_NULL, null=True, related_name='clientes', db_column='DAMA_TIPO_DOCUMENTO')

    class Meta:
        db_table = 'TBL_CLIENTES'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.clie_nombre


class Clase(models.Model):
    clas_id = models.AutoField(primary_key=True, db_column='CLAS_ID')
    clas_nombre = models.CharField(max_length=100, db_column='CLAS_NOMBRE')
    clas_fecha = models.DateField(db_column='CLAS_FECHA')
    entr_id = models.ForeignKey(Entrenador, on_delete=models.CASCADE, db_column='ENTR_ID')
    dama_horario_id = models.ForeignKey(DatosMaestros, on_delete=models.SET_NULL, null=True, related_name='clases', db_column='DAMA_HORARIO_ID')

    class Meta:
        db_table = 'TBL_CLASES'
        verbose_name = 'Clase'
        verbose_name_plural = 'Clases'

    def __str__(self):
        return f"{self.clas_nombre} - {self.clas_fecha}"


class AsistenciaClase(models.Model):
    ascl_id = models.AutoField(primary_key=True, db_column='ASCL_ID')
    clas_id = models.ForeignKey(Clase, on_delete=models.CASCADE, db_column='CLAS_ID')
    clie_id = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='CLIE_ID')

    class Meta:
        db_table = 'TBL_ASISTENCIAS_CLASES'
        verbose_name = 'Asistencia a Clase'
        verbose_name_plural = 'Asistencias a Clases'
        unique_together = [['clas_id', 'clie_id']]  # Un cliente no puede asistir dos veces a la misma clase

    def __str__(self):
        return f"Asistencia de {self.clie_id.clie_nombre} a {self.clas_id.clas_nombre}"


class ClienteMembresia(models.Model):
    clme_id = models.AutoField(primary_key=True, db_column='CLME_ID')
    clime_fecha_inicio = models.DateField(db_column='CLIME_FECHA_INICIO')
    clime_fecha_fin = models.DateField(null=True, blank=True, db_column='CLIME_FECHA_FIN')
    clie_id = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='CLIE_ID')
    dama_membresia_id = models.ForeignKey(DatosMaestros, on_delete=models.SET_NULL, null=True, related_name='membresias', db_column='DAMA_MEMBRESIA_ID')

    class Meta:
        db_table = 'TBL_CLIENTES_MEMBRESIAS'
        verbose_name = 'Membresía de Cliente'
        verbose_name_plural = 'Membresías de Clientes'

    def __str__(self):
        return f"{self.clie_id.clie_nombre} - {self.dama_membresia_id.dama_nombre if self.dama_membresia_id else 'Sin membresía'}"
    
    def esta_activa(self):
        """Verifica si la membresía está activa (fecha fin >= hoy)"""
        from datetime import date
        if not self.clime_fecha_fin:
            return True  # Si no tiene fecha fin, se considera activa
        return self.clime_fecha_fin >= date.today()
    
    esta_activa.boolean = True  # Para mostrar iconos en el admin
    esta_activa.short_description = 'Activa'


class EspecialidadEntrenador(models.Model):
    esen_id = models.AutoField(primary_key=True, db_column='ESEN_ID')
    entr_id = models.ForeignKey(Entrenador, on_delete=models.CASCADE, db_column='ENTR_ID')
    dama_especialidad_id = models.ForeignKey(DatosMaestros, on_delete=models.SET_NULL, null=True, related_name='especialidades', db_column='DAMA_ESPECIALIDAD_ID')

    class Meta:
        db_table = 'TBL_ESPECIALIDAD_ENTRENADOR'
        verbose_name = 'Especialidad de Entrenador'
        verbose_name_plural = 'Especialidades de Entrenadores'

    def __str__(self):
        return f"{self.entr_id.entr_nombre} - {self.dama_especialidad_id.dama_nombre if self.dama_especialidad_id else 'Sin especialidad'}"
