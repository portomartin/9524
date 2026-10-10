<#
.SYNOPSIS
    Inicia en simultáneo los 3 servidores de desarrollo de los frontends del proyecto Intercambia.

.DESCRIPTION
    Abre cada aplicación en una ventana de PowerShell independiente:
      - frontend-v0 (Codex / PrimeVue original): http://localhost:5171
      - frontend-v1 (MVP V3 completo PrimeVue 4): http://localhost:5172
      - frontend-v2 (MVP V3 moderno Tailwind CSS + Shadcn): http://localhost:5173

.EXAMPLE
    .\start-frontends.ps1

.EXAMPLE
    .\start-frontends.ps1 -OpenBrowser
#>

param(
    [switch]$OpenBrowser
)

$root = $PSScriptRoot

Write-Host ""
Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "   Iniciando los 3 frontends del proyecto Intercambia     " -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host ""

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

    # Abre una ventana independiente de PowerShell para cada servidor con su propio título
    $cmd = "Set-Location -LiteralPath '$dir'; `$host.UI.RawUI.WindowTitle = '$($fe.Title) [Puerto $($fe.Port)]'; npm run dev"
    Start-Process powershell.exe -ArgumentList "-NoExit", "-Command", $cmd
}

Write-Host ""
Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "   URLs para comparar en tu navegador                     " -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "  v0 (Codex):    http://localhost:5171" -ForegroundColor Yellow
Write-Host "  v1 (PrimeVue): http://localhost:5172" -ForegroundColor Magenta
Write-Host "  v2 (Tailwind): http://localhost:5173" -ForegroundColor Green
Write-Host ""
Write-Host "💡 Cada servidor corre en su propia ventana. Podés cerrarla o presionar Ctrl+C para detenerlo." -ForegroundColor DarkGray
Write-Host ""

if ($OpenBrowser) {
    Write-Host "Abriendo las 3 pestañas en tu navegador predeterminado..." -ForegroundColor Cyan
    Start-Sleep -Seconds 2
    Start-Process "http://localhost:5171"
    Start-Process "http://localhost:5172"
    Start-Process "http://localhost:5173"
}
