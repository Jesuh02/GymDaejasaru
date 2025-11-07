# Script para ejecutar el proyecto Django GymDaejaSaru
# Uso: .\run.ps1

Write-Host "🏋️ Iniciando GymDaejaSaru..." -ForegroundColor Green

# Activar el entorno virtual
Write-Host "Activando entorno virtual..." -ForegroundColor Yellow
. .\.venv\Scripts\Activate.ps1

# Configurar SQLite para desarrollo local
$env:USE_SQLITE = '1'

# Navegar al directorio del proyecto Django
Set-Location .\GymDaejaSaru

# Aplicar migraciones (solo si hay cambios)
Write-Host "Verificando migraciones..." -ForegroundColor Yellow
python manage.py migrate --check 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Host "Aplicando migraciones..." -ForegroundColor Yellow
    python manage.py migrate
}

# Iniciar el servidor
Write-Host ""
Write-Host "✅ Servidor iniciado en http://127.0.0.1:8000" -ForegroundColor Green
Write-Host "Presiona Ctrl+C para detener el servidor" -ForegroundColor Cyan
Write-Host ""

python manage.py runserver 127.0.0.1:8000
