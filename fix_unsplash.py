import glob

def fix_unsplash(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    old_suffix = "?w=100&h=100&fit=crop"
    new_suffix = "?w=50&h=50&fit=crop&fm=webp&q=80"
    
    if old_suffix in content:
        content = content.replace(old_suffix, new_suffix)
        # Also replace the width/height attributes if they are set to 100
        content = content.replace('width="100" height="100" alt="User"', 'width="50" height="50" alt="User"')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed images in {filepath}")

for f in glob.glob("oferta16_*.html"):
    fix_unsplash(f)
