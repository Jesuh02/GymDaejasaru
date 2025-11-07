# GymDaejaSaru

Sistema de gestión para gimnasio desarrollado con Django.

## 🚀 Ejecución Rápida

Desde la raíz del proyecto, ejecuta:

```powershell
.\run.ps1
```

Eso es todo. El script automáticamente:
- Activa el entorno virtual
- Aplica migraciones si es necesario
- Inicia el servidor en http://127.0.0.1:8000

Para detener el servidor: `Ctrl+C`

## 📋 Requisitos

- Python 3.9+
- Entorno virtual ya configurado en `.venv`

## 🔧 Configuración Manual (opcional)

Si prefieres ejecutar manualmente:

```powershell
# Activar entorno virtual
.\.venv\Scripts\Activate.ps1

# Configurar para usar SQLite (desarrollo local)
$env:USE_SQLITE='1'

# Navegar al proyecto
cd GymDaejaSaru

# Aplicar migraciones
python manage.py migrate

# Iniciar servidor
python manage.py runserver 127.0.0.1:8000
```

## 🗄️ Base de Datos

- **Desarrollo local**: SQLite (automático con `run.ps1`)
- **Producción**: MySQL (configurado en `settings.py`)

Para usar MySQL localmente, no ejecutes `run.ps1` y configura las credenciales en `GymDaejaSaru/settings.py`.

## 📦 Módulos Principales

- **Clientes**: Gestión de miembros del gimnasio
- **Entrenadores**: Administración de personal
- **Clases**: Programación de sesiones
- **Membresías**: Control de suscripciones
- **Especialidades**: Áreas de entrenamiento
- **Asistencias**: Registro de participación

## 🛠️ Comandos Útiles

```powershell
# Crear superusuario (admin)
python manage.py createsuperuser

# Cargar datos maestros
python manage.py load_datos_maestros

# Acceder al shell de Django
python manage.py shell
```

## 📝 Notas

- El servidor de desarrollo corre en http://127.0.0.1:8000
- Panel de administración: http://127.0.0.1:8000/admin
- Zona horaria: America/Bogota (UTC-5)
- Idioma: Español (Colombia)
