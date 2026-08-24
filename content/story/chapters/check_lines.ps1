$content = Get-Content 'C:\Users\magic_new.BETOS-AIO.000\.qwenpaw\workspaces\default\ethra_site\content\story\chapters\chapter-arc6-01.md'
$lines = @(123,197,313,439,443,485,810,905,963,1042)
foreach ($ln in $lines) {
    if ($ln -le $content.Count) {
        $line = $content[$ln-1]
        Write-Host ("Line {0}: {1}" -f $ln, $line)
    } else {
        Write-Host ("Line {0}: OUT OF RANGE (max {1})" -f $ln, $content.Count)
    }
}