# Validate Claude Code capability infrastructure at session start.
param(
    [switch]$Verify,
    [switch]$Status
)

$ClaudeRoot = Join-Path $env:USERPROFILE ".claude"
$OverseerRoot = Join-Path $ClaudeRoot "overseer"

function Test-ClaudeRegistry {
    $required = @(
        (Join-Path $OverseerRoot "smart_selector.py"),
        (Join-Path $OverseerRoot "validate_claude_config.py"),
        (Join-Path $OverseerRoot "index.tsv"),
        (Join-Path $OverseerRoot "BUNDLE-REGISTRY.tsv")
    )

    $missing = @($required | Where-Object { -not (Test-Path -LiteralPath $_) })
    if ($missing.Count -gt 0) {
        Write-Host ("Missing registry files: " + ($missing -join ", ")) -ForegroundColor Red
        return $false
    }

    $validation = & python (Join-Path $OverseerRoot "validate_claude_config.py") 2>&1
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Capability registry validation failed." -ForegroundColor Red
        $validation | Write-Host
        return $false
    }

    $env:UNIFIED_SYSTEM_ACTIVE = "true"
    $env:BUNDLES_PATH = Join-Path $ClaudeRoot "skills"
    $env:OVERSEER_PATH = $OverseerRoot
    Write-Host "Claude capability registry validated." -ForegroundColor Green
    return $true
}

function Show-ClaudeStatus {
    if ($env:UNIFIED_SYSTEM_ACTIVE -eq "true") {
        Write-Host "Status: ACTIVE" -ForegroundColor Green
        Write-Host "Routing: explicit skill search plus supported hooks" -ForegroundColor Green
        Write-Host "Metrics: reported only when emitted by a runtime hook" -ForegroundColor Green
    } else {
        Write-Host "Status: INACTIVE" -ForegroundColor Red
    }
}

if ($Status) {
    Show-ClaudeStatus
} else {
    $ok = Test-ClaudeRegistry
    if ($ok -and $Verify) {
        Show-ClaudeStatus
    }
    if (-not $ok) {
        exit 1
    }
}
