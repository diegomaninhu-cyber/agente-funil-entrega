import os
import re

def main():
    files = [f for f in os.listdir('.') if f.startswith('oferta16_') and f.endswith('.html') and f != 'oferta16_nutricionistas.html']
    
    for filename in files:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        print(f"Processing {filename}...")
        
        # 1. Extract the video card block
        video_pattern = re.compile(r'(\s*<div class="video-card" style="margin-top: 32px;">.*?</div>\s*</div>\s*</div>)', re.DOTALL)
        # Wait, the video card has nested divs. A simple regex dotall won't easily match matching divs.
        # Let's use a more exact match since the block is identical across these files.
        video_block_regex = r'(<div class="video-card" style="margin-top: 32px;">\s*<div class="video-img" style="aspect-ratio: 80/121;">\s*<video class="lazy" data-src="/VIDEO-[^"]+" style="width: 100%; height: 100%; object-fit: cover;" loop muted playsinline></video>\s*</div>\s*<div class="video-footer">.*?<strong>\+1\.000 alunos</strong>\s*Resultados comprovados\s*</div>\s*</div>\s*</div>)'
        
        match_video = re.search(video_block_regex, content, re.DOTALL)
        if not match_video:
            print(f"  [!] Video block not found in {filename}!")
            continue
            
        video_block_original = match_video.group(1)
        # We need the video block but with margin-top: 0; to put in the hero
        video_block_hero = video_block_original.replace('margin-top: 32px;', 'margin-top: 0;')
        
        # 2. Find the hero-media block containing the phone-mockup and slider
        hero_pattern = r'(<div class="hero-media gsap-fade" style="transition-delay: 200ms;">)\s*<div class="phone-mockup".*?<p class="cmp-hint".*?</p>\s*</div>'
        
        match_hero = re.search(hero_pattern, content, re.DOTALL)
        if not match_hero:
            print(f"  [!] Hero block not found in {filename}!")
            continue
            
        # Replace hero block content with video block
        new_hero = match_hero.group(1) + '\n\n' + '  ' + video_block_hero + '\n\n        </div>'
        content = re.sub(hero_pattern, new_hero, content, count=1, flags=re.DOTALL)
        
        # 3. Remove the original video block from the middle section
        content = content.replace(video_block_original, '')
        
        # 4. Replace the "Veja a transformação" DM images with Fogaça images
        dm_after_pattern = r'<div class="cmp-img cmp-after"><img loading="lazy" decoding="async" src="assets/handoff-oferta16/[^"]+-depois\.webp" alt="[^"]+" style="object-fit: contain;"><small>Depois</small></div>'
        dm_before_pattern = r'<div class="cmp-img cmp-before"><img loading="lazy" decoding="async" src="assets/handoff-oferta16/[^"]+-antes\.webp" alt="[^"]+" style="object-fit: contain;"><small>Antes</small></div>'
        
        replacement_after = '<div class="cmp-img cmp-after"><img loading="lazy" decoding="async" src="/depois-fogaca.webp" alt="Depois - Antonio Fogaça" style="object-fit: contain;"><small>Depois</small></div>'
        replacement_before = '<div class="cmp-img cmp-before"><img loading="lazy" decoding="async" src="/antes-fogaca.webp" alt="Antes - Antonio Fogaça" style="object-fit: contain;"><small>Antes</small></div>'
        
        content = re.sub(dm_after_pattern, replacement_after, content, count=1)
        content = re.sub(dm_before_pattern, replacement_before, content, count=1)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"  [OK] Successfully updated {filename}")

if __name__ == '__main__':
    main()
