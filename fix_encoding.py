import os
import glob

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Apply specific fixes
    content = content.replace('B\ufffd”NUS', 'BÔNUS')
    content = content.replace('\ufffd”\ufffd”', '-')
    content = content.replace('\ufffd“', '"')
    content = content.replace('\ufffd”', '"')
    content = content.replace('“', '"')
    content = content.replace('”', '"')
    
    # Catch any remaining replacement characters
    content = content.replace('\ufffd', '"')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Fixed {filepath}")

for f in glob.glob("oferta16_*.html"):
    fix_file(f)
