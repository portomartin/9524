<#
.SYNOPSIS
    Inicia en paralelo el Backend (FastAPI) y el Frontend v2 (Tailwind/Vite) conectados.

.DESCRIPTION
    Abre dos consolas independientes:
      1. Backend FastAPI:   http://127.0.0.1:8000 (Docs: /docs)
      2. Frontend v2:       http://localhost:5173

.PARAMETER OpenBrowser
    Abre automáticamente las URLs en el navegador web predeterminado tras iniciar.

.EXAMPLE
    .\start-dev.ps1
    .\start-dev.ps1 -OpenBrowser
#>

param(
    [switch]$OpenBrowser
)

$root = $PSScriptRoot

Write-Host ""
Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "     Iniciando Entorno Conectado (Backend + Frontend v2)  " -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host ""

# 1. Verificar directorios
$backendDir = Join-Path $root "proyecto-sdd\backend"
$frontendDir = Join-Path $root "proyecto-sdd\frontend\v2"

if (-not (Test-Path $backendDir)) {
    Write-Error "No se encontró el directorio de backend en: $backendDir"
    exit 1
}

if (-not (Test-Path $frontendDir)) {
    Write-Error "No se encontró el directorio de frontend v2 en: $frontendDir"
    exit 1
}

# 2. Comando Backend
Write-Host "-> Iniciando Backend (FastAPI / Uvicorn en http://127.0.0.1:8000)..." -ForegroundColor Yellow
$backendCmd = @"
Set-Location -LiteralPath '$backendDir'
`$host.UI.RawUI.WindowTitle = 'Backend FastAPI [8000]'
Write-Host '===================================================' -ForegroundColor Cyan
Write-Host '  Backend API (FastAPI)                            ' -ForegroundColor Cyan
Write-Host '  URL:  http://127.0.0.1:8000                      ' -ForegroundColor Cyan
Write-Host '  Docs: http://127.0.0.1:8000/docs                 ' -ForegroundColor Cyan
Write-Host '===================================================' -ForegroundColor Cyan
if (Test-Path '.\.venv\Scripts\uvicorn.exe') {
    & '.\.venv\Scripts\uvicorn.exe' main:app --reload --port 8000
} elseif (Test-Path '.\.venv\Scripts\python.exe') {
    & '.\.venv\Scripts\python.exe' -m uvicorn main:app --reload --port 8000
} else {
    python -m uvicorn main:app --reload --port 8000
}
"@

Start-Process powershell.exe -ArgumentList "-NoExit", "-Command", $backendCmd

# 3. Comando Frontend v2
Write-Host "-> Iniciando Frontend v2 (Vite en http://localhost:5173)..." -ForegroundColor Green
$frontendCmd = @"
Set-Location -LiteralPath '$frontendDir'
`$host.UI.RawUI.WindowTitle = 'Frontend v2 Vite [5173]'
Write-Host '===================================================' -ForegroundColor Green
Write-Host '  Frontend v2 (Vue 3 + Tailwind CSS + Lucide)      ' -ForegroundColor Green
Write-Host '  URL: http://localhost:5173                       ' -ForegroundColor Green
Write-Host '  Proxy: /api -> http://127.0.0.1:8000             ' -ForegroundColor Green
Write-Host '===================================================' -ForegroundColor Green
npm run dev
"@

Start-Process powershell.exe -ArgumentList "-NoExit", "-Command", $frontendCmd

Write-Host ""
Write-Host "Servidores iniciados en ventanas separadas." -ForegroundColor Cyan
Write-Host "  - Backend API: http://127.0.0.1:8000 / Documentación Swagger: http://127.0.0.1:8000/docs" -ForegroundColor Gray
Write-Host "  - Frontend v2: http://localhost:5173" -ForegroundColor Gray
Write-Host ""

if ($OpenBrowser) {
    Start-Sleep -Seconds 2
    Start-Process "http://localhost:5173"
    Start-Process "http://127.0.0.1:8000/docs"
}
