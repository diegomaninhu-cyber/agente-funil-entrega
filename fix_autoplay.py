import glob

def fix_autoplay(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace 'loop muted playsinline' with 'autoplay loop muted playsinline'
    if 'autoplay loop muted playsinline' not in content:
        content = content.replace('loop muted playsinline', 'autoplay loop muted playsinline')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Fixed {filepath}")

for f in glob.glob("oferta16_*.html"):
    fix_autoplay(f)
