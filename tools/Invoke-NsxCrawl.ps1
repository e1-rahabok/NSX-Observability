<#
.SYNOPSIS
  Runs nsx_crawl.py against an NSX Manager using a DPAPI-encrypted credential.

.EXAMPLE
  ./tools/Invoke-NsxCrawl.ps1 -NsxHost nsxman1.liljestig.com

  The credential file is created once with:
  Get-Credential | Export-Clixml "$HOME\.secrets\nsx-<host>.xml"
#>
param(
    [Parameter(Mandatory)] [string] $NsxHost,
    [string] $CredentialPath = "$HOME\.secrets\nsx-$NsxHost.xml",
    [string] $Out = (Join-Path $PSScriptRoot "..\output\$NsxHost-$(Get-Date -Format yyyyMMdd-HHmmss)"),
    [Parameter(ValueFromRemainingArguments)] [string[]] $CrawlArgs
)

$cred = Import-Clixml $CredentialPath
$env:NSX_USER = $cred.UserName
$env:NSX_PASSWORD = $cred.GetNetworkCredential().Password
try {
    python -I (Join-Path $PSScriptRoot 'nsx_crawl.py') --host $NsxHost --out $Out @CrawlArgs
} finally {
    Remove-Item Env:NSX_USER, Env:NSX_PASSWORD -ErrorAction SilentlyContinue
}
