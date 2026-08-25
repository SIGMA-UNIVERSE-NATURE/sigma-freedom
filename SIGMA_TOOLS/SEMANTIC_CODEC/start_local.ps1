$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

Write-Host "SIGMA Semantic Capsule Codec v0.1"
Write-Host "Local-only mode: 127.0.0.1:8765"

if (-not (Test-Path ".venv")) {
    py -m venv .venv
}

& ".\.venv\Scripts\python.exe" -m pip install -r requirements.txt
& ".\.venv\Scripts\python.exe" self_test.py

Write-Host "Web UI: http://127.0.0.1:8765/"
Write-Host "API docs: http://127.0.0.1:8765/docs"
& ".\.venv\Scripts\python.exe" sigma_semantic_codec_service.py --host 127.0.0.1 --port 8765
