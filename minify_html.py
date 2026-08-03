"""
Aggressive HTML minification for oferta16 pages.
- Remove blank lines
- Collapse multiple whitespace in HTML (not in script/style)
- Strip leading whitespace from HTML lines
"""
import glob
import re

def aggressive_minify(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_size = len(content)
    
    # Remove blank lines  
    lines = content.split('\n')
    non_blank = [line for line in lines if line.strip()]
    
    # Now process: strip leading whitespace from pure HTML lines
    # But preserve indentation inside <script> and <style> blocks
    result = []
    in_script = False
    in_style = False
    
    for line in non_blank:
        stripped = line.strip()
        
        if '<script' in stripped.lower():
            in_script = True
        if '</script>' in stripped.lower():
            in_script = False
            result.append(stripped)
            continue
        if '<style' in stripped.lower():
            in_style = True
        if '</style>' in stripped.lower():
            in_style = False
            result.append(stripped)
            continue
            
        if in_script or in_style:
            # Keep script/style content but strip trailing whitespace
            result.append(line.rstrip())
        else:
            # HTML: strip leading whitespace aggressively
            result.append(stripped)
    
    minified = '\n'.join(result) + '\n'
    
    new_size = len(minified)
    savings = original_size - new_size
    pct = (savings / original_size) * 100
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(minified)
    
    print(f"[OK] {filepath}: {original_size/1024:.1f}KB -> {new_size/1024:.1f}KB (saved {savings/1024:.1f}KB, {pct:.0f}%)")

for f in sorted(glob.glob("oferta16_*.html")):
    aggressive_minify(f)
