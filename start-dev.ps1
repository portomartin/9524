<#
.SYNOPSIS
    Inicia en paralelo el Backend (FastAPI) y el Frontend deseado (v3 por defecto, o v2 / v1) conectados.

.DESCRIPTION
    Abre dos consolas independientes:
      1. Backend FastAPI:   http://127.0.0.1:8000 (Docs: /docs)
      2. Frontend v3 (AX):  http://localhost:5174 (por defecto) o v2: 5173 / v1: 5172

.PARAMETER V2
    Levanta la versión Frontend v2 (puerto 5173).

.PARAMETER V1
    Levanta la versión Frontend v1 PrimeVue (puerto 5172).

.PARAMETER OpenBrowser
    Abre automáticamente las URLs en el navegador web predeterminado tras iniciar.

.EXAMPLE
    .\start-dev.ps1                 # Levanta Backend + Frontend v3 (Agentic Experience)
    .\start-dev.ps1 -OpenBrowser    # Levanta Backend + Frontend v3 y abre el navegador
    .\start-dev.ps1 -V2             # Levanta Backend + Frontend v2
#>

param(
    [switch]$V2,
    [switch]$V1,
    [switch]$OpenBrowser
)

$root = $PSScriptRoot

$feVersion = "v3"
$fePort = 5174
$feName = "Frontend v3 (Agentic Experience & Live Community)"

if ($V2) {
    $feVersion = "v2"
    $fePort = 5173
    $feName = "Frontend v2 (Tailwind Utilitario)"
} elseif ($V1) {
    $feVersion = "v1"
    $fePort = 5172
    $feName = "Frontend v1 (PrimeVue 4)"
}

Write-Host ""
Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "     Iniciando Entorno Conectado (Backend + $feName)      " -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host ""

# 1. Verificar directorios
$backendDir = Join-Path $root "proyecto-sdd\backend"
$frontendDir = Join-Path $root "proyecto-sdd\frontend\$feVersion"

if (-not (Test-Path $backendDir)) {
    Write-Error "No se encontró el directorio de backend en: $backendDir"
    exit 1
}

if (-not (Test-Path $frontendDir)) {
    Write-Error "No se encontró el directorio de frontend en: $frontendDir"
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

# 3. Comando Frontend
Write-Host "-> Iniciando $feName (Vite en http://localhost:$fePort)..." -ForegroundColor Green
$frontendCmd = @"
Set-Location -LiteralPath '$frontendDir'
`$host.UI.RawUI.WindowTitle = '$feName [$fePort]'
Write-Host '===================================================' -ForegroundColor Green
Write-Host '  $feName                                          ' -ForegroundColor Green
Write-Host '  URL: http://localhost:$fePort                    ' -ForegroundColor Green
Write-Host '  Proxy: /api -> http://127.0.0.1:8000             ' -ForegroundColor Green
Write-Host '===================================================' -ForegroundColor Green
npm run dev
"@

Start-Process powershell.exe -ArgumentList "-NoExit", "-Command", $frontendCmd

Write-Host ""
Write-Host "Servidores iniciados en ventanas separadas." -ForegroundColor Cyan
Write-Host "  - Backend API: http://127.0.0.1:8000 (Swagger: http://127.0.0.1:8000/docs)" -ForegroundColor Gray
Write-Host "  - $feName: http://localhost:$fePort" -ForegroundColor Gray
Write-Host ""

if ($OpenBrowser) {
    Start-Sleep -Seconds 2
    Start-Process "http://localhost:$fePort"
    Start-Process "http://127.0.0.1:8000/docs"
}
