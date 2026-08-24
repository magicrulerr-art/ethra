$content = Get-Content 'C:\Users\magic_new.BETOS-AIO.000\.qwenpaw\workspaces\default\ethra_site\content\story\chapters\chapter-arc6-01.md' -Raw
$patterns = @(
    'well now that'"'"'s out of the way',
    'hmm the council worked as designed',
    'The next scene is a couple of hours after ajani',
    'so these are the ones',
    'Ambassador these are your people',
    'Let'"'"'s follow the rest of the cast',
    'Now let'"'"'s see Yvaria',
    'its worse than I thought',
    'theyre brutes'
)
foreach ($pattern in $patterns) {
    $matches = [regex]::Matches($content, $pattern, 'IgnoreCase')
    foreach ($m in $matches) {
        $pos = $m.Index
        $lineNum = ($content.Substring(0, $pos) -split "`n").Count
        Write-Host ("Found '{0}' at line ~{1}" -f $pattern, $lineNum)
    }
}