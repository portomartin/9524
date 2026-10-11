<#
.SYNOPSIS
    Inicia en paralelo el Backend (FastAPI) y el Frontend deseado (v5 por defecto, o v4 / v3 / v2 / v1) conectados.

.DESCRIPTION
    Abre dos consolas independientes:
      1. Backend FastAPI:   http://127.0.0.1:8000 (Docs: /docs)
      2. Frontend v5 (Human Visual): http://localhost:5176 (por defecto) o v4: 5175 / v3: 5174 / v2: 5173 / v1: 5172

.PARAMETER V5
    Levanta la version Frontend v5 Human Visual (puerto 5176, por defecto).

.PARAMETER V4
    Levanta la version Frontend v4 Spatial Canvas (puerto 5175).

.PARAMETER V3
    Levanta la version Frontend v3 Agentic Experience (puerto 5174).

.PARAMETER V2
    Levanta la version Frontend v2 Tailwind (puerto 5173).

.PARAMETER V1
    Levanta la version Frontend v1 PrimeVue (puerto 5172).

.PARAMETER OpenBrowser
    Abre automaticamente las URLs en el navegador web predeterminado tras iniciar.
#>

param(
    [switch]$V5,
    [switch]$V4,
    [switch]$V3,
    [switch]$V2,
    [switch]$V1,
    [switch]$OpenBrowser
)

$root = $PSScriptRoot

$feVersion = "v5"
$fePort = "5176"
$feName = "Frontend v5 (Human Visual - Enseno y Aprendo)"

if ($V4) {
    $feVersion = "v4"
    $fePort = "5175"
    $feName = "Frontend v4 (Spatial Canvas)"
} elseif ($V3) {
    $feVersion = "v3"
    $fePort = "5174"
    $feName = "Frontend v3 (Agentic Experience)"
} elseif ($V2) {
    $feVersion = "v2"
    $fePort = "5173"
    $feName = "Frontend v2 (Tailwind)"
} elseif ($V1) {
    $feVersion = "v1"
    $fePort = "5172"
    $feName = "Frontend v1 (PrimeVue 4)"
}

Write-Host ""
Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "     Iniciando Entorno Conectado: $feName                 " -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host ""

$backendDir = Join-Path $root "proyecto-sdd\backend"
$frontendDir = Join-Path $root "proyecto-sdd\frontend\$feVersion"

if (-not (Test-Path $backendDir)) {
    Write-Error "No se encontro el directorio de backend en: $backendDir"
    exit 1
}

if (-not (Test-Path $frontendDir)) {
    Write-Error "No se encontro el directorio de frontend en: $frontendDir"
    exit 1
}

Write-Host "-> Iniciando Backend (FastAPI en http://127.0.0.1:8000)..." -ForegroundColor Yellow
$backendCmd = "Set-Location -LiteralPath '$backendDir'; `$host.UI.RawUI.WindowTitle = 'Backend FastAPI [8000]'; Write-Host 'Iniciando Backend en http://127.0.0.1:8000' -ForegroundColor Cyan; if (Test-Path '.\.venv\Scripts\uvicorn.exe') { & '.\.venv\Scripts\uvicorn.exe' main:app --reload --port 8000 } elseif (Test-Path '.\.venv\Scripts\python.exe') { & '.\.venv\Scripts\python.exe' -m uvicorn main:app --reload --port 8000 } else { python -m uvicorn main:app --reload --port 8000 }"

Start-Process powershell.exe -ArgumentList "-NoExit", "-Command", $backendCmd

Write-Host "-> Iniciando $feName (en http://localhost:$fePort)..." -ForegroundColor Green
$frontendCmd = "Set-Location -LiteralPath '$frontendDir'; `$host.UI.RawUI.WindowTitle = '$feName [$fePort]'; Write-Host 'Iniciando Frontend en http://localhost:$fePort' -ForegroundColor Green; npm run dev"

Start-Process powershell.exe -ArgumentList "-NoExit", "-Command", $frontendCmd

Write-Host ""
Write-Host "Servidores iniciados en ventanas separadas." -ForegroundColor Cyan
Write-Host "  - Backend API: http://127.0.0.1:8000 (Docs: http://127.0.0.1:8000/docs)" -ForegroundColor Gray
Write-Host ("  - {0} - http://localhost:{1}" -f $feName, $fePort) -ForegroundColor Gray
Write-Host ""

if ($OpenBrowser) {
    Start-Sleep -Seconds 2
    Start-Process ("http://localhost:{0}" -f $fePort)
    Start-Process "http://127.0.0.1:8000/docs"
}
