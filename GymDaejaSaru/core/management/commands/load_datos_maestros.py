from django.core.management.base import BaseCommand
from core.models import DatosMaestros


class Command(BaseCommand):
    help = 'Carga los datos maestros iniciales en la base de datos'

    def handle(self, *args, **options):
        self.stdout.write('Cargando datos maestros...')
        
        # Verificar si ya existen datos
        if DatosMaestros.objects.exists():
            self.stdout.write(self.style.WARNING('Ya existen datos maestros en la base de datos.'))
            respuesta = input('¿Desea continuar y crear los datos de todos modos? (s/n): ')
            if respuesta.lower() != 's':
                self.stdout.write(self.style.ERROR('Operación cancelada.'))
                return
        
        # Limpiar datos existentes si se confirma
        DatosMaestros.objects.all().delete()
        self.stdout.write('Datos anteriores eliminados.')
        
        # 1. TIPO_DOCUMENTOS (padre)
        tipo_doc = DatosMaestros.objects.create(
            dama_id=1,
            dama_nombre='TIPO_DOCUMENTOS',
            dama_valor='TIDO',
            dama_padre_id=None,
            dama_dependencia_id=None,
            dama_estado=1
        )
        self.stdout.write(self.style.SUCCESS(f'✓ Creado: {tipo_doc.dama_nombre}'))
        
        # 2. CEDULA DE CIUDADANIA
        cc = DatosMaestros.objects.create(
            dama_id=2,
            dama_nombre='CEDULA DE CIUDADANIA',
            dama_valor='CC',
            dama_padre_id=tipo_doc,
            dama_dependencia_id=None,
            dama_estado=1
        )
        self.stdout.write(self.style.SUCCESS(f'✓ Creado: {cc.dama_nombre}'))
        
        # 3. TARJETA DE IDENTIDAD
        ti = DatosMaestros.objects.create(
            dama_id=3,
            dama_nombre='TARJETA DE IDENTIDAD',
            dama_valor='TI',
            dama_padre_id=tipo_doc,
            dama_dependencia_id=None,
            dama_estado=1
        )
        self.stdout.write(self.style.SUCCESS(f'✓ Creado: {ti.dama_nombre}'))
        
        # 4. CEDULA DE EXTRANJERIA
        ce = DatosMaestros.objects.create(
            dama_id=4,
            dama_nombre='CEDULA DE EXTRANJERIA',
            dama_valor='CE',
            dama_padre_id=tipo_doc,
            dama_dependencia_id=None,
            dama_estado=1
        )
        self.stdout.write(self.style.SUCCESS(f'✓ Creado: {ce.dama_nombre}'))
        
        # 5. TIPO_MEMBRESIAS (padre)
        tipo_memb = DatosMaestros.objects.create(
            dama_id=5,
            dama_nombre='TIPO_MEMBRESIAS',
            dama_valor='TIME',
            dama_padre_id=None,
            dama_dependencia_id=None,
            dama_estado=1
        )
        self.stdout.write(self.style.SUCCESS(f'✓ Creado: {tipo_memb.dama_nombre}'))
        
        # 6. BASICA
        basica = DatosMaestros.objects.create(
            dama_id=6,
            dama_nombre='BASICA',
            dama_valor='BASE',
            dama_padre_id=tipo_memb,
            dama_dependencia_id=None,
            dama_estado=1
        )
        self.stdout.write(self.style.SUCCESS(f'✓ Creado: {basica.dama_nombre}'))
        
        # 7. PREMIUM
        premium = DatosMaestros.objects.create(
            dama_id=7,
            dama_nombre='PREMIUM',
            dama_valor='PREMI',
            dama_padre_id=tipo_memb,
            dama_dependencia_id=None,
            dama_estado=1
        )
        self.stdout.write(self.style.SUCCESS(f'✓ Creado: {premium.dama_nombre}'))
        
        # 8. VIP
        vip = DatosMaestros.objects.create(
            dama_id=8,
            dama_nombre='VIP',
            dama_valor='VIP',
            dama_padre_id=tipo_memb,
            dama_dependencia_id=None,
            dama_estado=1
        )
        self.stdout.write(self.style.SUCCESS(f'✓ Creado: {vip.dama_nombre}'))
        
        # 9. PROMO HALLOWEEN (inactiva)
        promo = DatosMaestros.objects.create(
            dama_id=9,
            dama_nombre='PROMO HALLOWEEN',
            dama_valor='HALLOPROMO',
            dama_padre_id=tipo_memb,
            dama_dependencia_id=None,
            dama_estado=0
        )
        self.stdout.write(self.style.SUCCESS(f'✓ Creado: {promo.dama_nombre} (inactiva)'))
        
        # 10. TIPO_HORARIO (padre)
        tipo_horario = DatosMaestros.objects.create(
            dama_id=10,
            dama_nombre='TIPO_HORARIO',
            dama_valor='TIHO',
            dama_padre_id=None,
            dama_dependencia_id=None,
            dama_estado=1
        )
        self.stdout.write(self.style.SUCCESS(f'✓ Creado: {tipo_horario.dama_nombre}'))
        
        # 11. MAÑANA
        manana = DatosMaestros.objects.create(
            dama_id=11,
            dama_nombre='MAÑANA',
            dama_valor='06:00:00 - 12:00:00',
            dama_padre_id=tipo_horario,
            dama_dependencia_id=None,
            dama_estado=1
        )
        self.stdout.write(self.style.SUCCESS(f'✓ Creado: {manana.dama_nombre}'))
        
        # 12. TARDE
        tarde = DatosMaestros.objects.create(
            dama_id=12,
            dama_nombre='TARDE',
            dama_valor='12:00:00 - 18:00:00',
            dama_padre_id=tipo_horario,
            dama_dependencia_id=None,
            dama_estado=1
        )
        self.stdout.write(self.style.SUCCESS(f'✓ Creado: {tarde.dama_nombre}'))
        
        # 13. NOCHE
        noche = DatosMaestros.objects.create(
            dama_id=13,
            dama_nombre='NOCHE',
            dama_valor='18:00:00 - 22:00:00',
            dama_padre_id=tipo_horario,
            dama_dependencia_id=None,
            dama_estado=1
        )
        self.stdout.write(self.style.SUCCESS(f'✓ Creado: {noche.dama_nombre}'))
        
        self.stdout.write(self.style.SUCCESS('\n✓ Todos los datos maestros han sido cargados exitosamente!'))
        self.stdout.write(f'Total de registros creados: {DatosMaestros.objects.count()}')

