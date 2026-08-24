import subprocess
result = subprocess.run(['git', 'diff', 'content/story/chapters/chapter-arc6-02.md'], 
                       capture_output=True, text=True, 
                       cwd='C:/Users/magic_new.BETOS-AIO.000/.qwenpaw/workspaces/default/ethra_site')
print(result.stdout[:10000])
if len(result.stdout) > 10000:
    print(f"... (truncated, total {len(result.stdout)} chars)")