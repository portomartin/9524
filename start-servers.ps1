<#
.SYNOPSIS
    Inicia en simultáneo los servidores de desarrollo (Backend y Frontends) del proyecto Intercambia.

.DESCRIPTION
    Abre cada servicio en una ventana independiente de PowerShell con su respectivo título y color:
      - Backend API (FastAPI / Uvicorn):        http://127.0.0.1:8000 (Docs: /docs)
      - Frontend v0 (Codex / PrimeVue original): http://localhost:5171
      - Frontend v1 (MVP V3 completo PrimeVue): http://localhost:5172
      - Frontend v2 (MVP V3 moderno Tailwind):  http://localhost:5173

.PARAMETER OpenBrowser
    Abre automáticamente las URLs en el navegador predeterminado.

.PARAMETER NoBackend
    Omite el inicio del servidor backend.

.PARAMETER NoFrontend
    Omite el inicio de los servidores frontend.

.EXAMPLE
    .\start-servers.ps1

.EXAMPLE
    .\start-servers.ps1 -OpenBrowser
#>

param(
    [switch]$OpenBrowser,
    [switch]$NoBackend,
    [switch]$NoFrontend
)

$root = $PSScriptRoot

Write-Host ""
Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "       Iniciando Servidores - Proyecto Intercambia        " -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host ""

# ------------------------------------------------------------
# 1. Backend (FastAPI / Uvicorn)
# ------------------------------------------------------------
if (-not $NoBackend) {
    $backendDir = Join-Path $root "proyecto-sdd\backend"
    if (Test-Path $backendDir) {
        Write-Host "-> Levantando Backend (FastAPI) en puerto 8000..." -ForegroundColor Cyan
        $backendCmd = @"
Set-Location -LiteralPath '$backendDir'
`$host.UI.RawUI.WindowTitle = 'Backend API [Puerto 8000]'
Write-Host '=== Iniciando Backend API (FastAPI) en http://127.0.0.1:8000 ===' -ForegroundColor Cyan
if (Test-Path '.\.venv\Scripts\python.exe') {
    & '.\.venv\Scripts\python.exe' -m uvicorn main:app --reload --port 8000
} elseif (Get-Command python -ErrorAction SilentlyContinue) {
    python -m uvicorn main:app --reload --port 8000
} elseif (Get-Command py -ErrorAction SilentlyContinue) {
    py -m uvicorn main:app --reload --port 8000

} else {
    Write-Error 'No se encontro Python instalado en el sistema.'
}
"@
        Start-Process powershell.exe -ArgumentList "-NoExit", "-Command", $backendCmd
    } else {
        Write-Warning "No se encontró el directorio de backend: $backendDir"
    }
}

# ------------------------------------------------------------
# 2. Frontends (Vite)
# ------------------------------------------------------------
if (-not $NoFrontend) {
    $frontends = @(
        @{ RelativePath = "proyecto-sdd\frontend\v0"; Port = 5171; Title = "V0 - Codex Original"; Desc = "Original Codex (PrimeVue)"; Color = "Yellow" },
        @{ RelativePath = "proyecto-sdd\frontend\v1"; Port = 5172; Title = "V1 - PrimeVue 4"; Desc = "MVP V3 Completo (PrimeVue 4)"; Color = "Magenta" },
        @{ RelativePath = "proyecto-sdd\frontend\v2"; Port = 5173; Title = "V2 - Tailwind + Shadcn"; Desc = "MVP V3 Moderno (Tailwind + Shadcn)"; Color = "Green" }
    )

    foreach ($fe in $frontends) {
        $dir = Join-Path $root $fe.RelativePath
        if (-not (Test-Path $dir)) {
            Write-Warning "No se encontró la carpeta $dir"
            continue
        }

        Write-Host "-> Levantando $($fe.Title) en puerto $($fe.Port) ($($fe.Desc))..." -ForegroundColor $fe.Color

        $frontendCmd = @"
Set-Location -LiteralPath '$dir'
`$host.UI.RawUI.WindowTitle = '$($fe.Title) [Puerto $($fe.Port)]'
Write-Host '=== Iniciando $($fe.Title) en http://localhost:$($fe.Port) ===' -ForegroundColor $($fe.Color)
npm run dev
"@
        Start-Process powershell.exe -ArgumentList "-NoExit", "-Command", $frontendCmd
    }
}

Write-Host ""
Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "   Servicios y URLs disponibles                           " -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan
if (-not $NoBackend) {
    Write-Host "  Backend API:   http://127.0.0.1:8000 (Swagger docs: http://127.0.0.1:8000/docs)" -ForegroundColor Cyan
}
if (-not $NoFrontend) {
    Write-Host "  v0 (Codex):    http://localhost:5171" -ForegroundColor Yellow
    Write-Host "  v1 (PrimeVue): http://localhost:5172" -ForegroundColor Magenta
    Write-Host "  v2 (Tailwind): http://localhost:5173" -ForegroundColor Green
}
Write-Host ""
Write-Host "💡 Cada servidor se ejecuta en una ventana separada. Cerrá la ventana o pulsá Ctrl+C para detenerlo." -ForegroundColor DarkGray
Write-Host ""

if ($OpenBrowser) {
    Write-Host "Abriendo URLs en tu navegador predeterminado..." -ForegroundColor Cyan
    Start-Sleep -Seconds 2
    if (-not $NoBackend) {
        Start-Process "http://127.0.0.1:8000/docs"
    }
    if (-not $NoFrontend) {
        Start-Process "http://localhost:5171"
        Start-Process "http://localhost:5172"
        Start-Process "http://localhost:5173"
    }
}
