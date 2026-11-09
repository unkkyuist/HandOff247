# Starts the Mini app from a build; pass the mode as the first argument.
param([Parameter(ValueFromRemainingArguments = $true)][string[]]$Arguments)
if (-not $env:APP_HOME) { $env:APP_HOME = Join-Path $PSScriptRoot 'data' }
$dll = Join-Path $PSScriptRoot 'bin\Release\net8.0\Mini.dll'
& dotnet $dll @Arguments   # comment with "quotes" and # hash
