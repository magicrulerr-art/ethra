$root = "C:\Users\magic_new.BETOS-AIO.000\.qwenpaw\workspaces\default"
$trees = @("ethra_site", "ethra_linux_migration\ethra_site", "archive\ethra_site_v1")
$names = @()
1..6 | ForEach-Object { $names += ("chapter-arc1-{0:d2}.md" -f $_) }
1..6 | ForEach-Object { $names += ("chapter-arc2-{0:d2}.md" -f $_) }
foreach ($t in $trees) {
    $base = Join-Path $root $t
    if (-not (Test-Path $base)) { Write-Output ("TREE MISSING: " + $t); continue }
    foreach ($n in $names) {
        $p = Join-Path $base ("content\story\chapters\" + $n)
        if (Test-Path $p) {
            $h = (Get-FileHash $p -Algorithm MD5).Hash
            Write-Output ("{0} | {1} | {2}" -f $t, $n, $h)
        } else {
            Write-Output ("{0} | {1} | MISSING" -f $t, $n)
        }
    }
}
