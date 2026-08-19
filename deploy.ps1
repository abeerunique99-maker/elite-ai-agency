
Write-Host "=== Elite AI Agency Deployment Automation ===" -ForegroundColor Cyan

# التأكد من التواجد في مجلد المشروع
Set-Location $PSScriptRoot

# فحص حالة Git ورفع التحديثات
Write-Host "[1/3] Adding changes to Git..." -ForegroundColor Yellow
git add .
$commitMsg = Read-Host "Enter commit message (or press Enter for default)"
if ([string]::IsNullOrWhiteSpace($commitMsg)) {
    $commitMsg = "Auto-update Elite AI Agency framework"
}
git commit -m "$commitMsg"

Write-Host "[2/3] Pushing to GitHub main branch..." -ForegroundColor Yellow
git push origin main

Write-Host "[3/3] Deployment triggered successfully via GitHub integration!" -ForegroundColor Green
Write-Host "=== Done! Railway will now auto-build your updates. ===" -ForegroundColor Cyan
