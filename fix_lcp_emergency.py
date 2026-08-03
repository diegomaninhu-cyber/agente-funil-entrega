"""
EMERGENCY FIX: Revert LCP-killing CSS and fix critical issues.

Root causes of score drop from 90 to 59:
1. .gsap-fade { opacity: 0 } hides the hero → LCP 7.8s (was fine before)
2. /api/track still in critical chain despite requestIdleCallback
3. Images without width/height causing CLS
"""
import glob
import re

def fix_page(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    changes = []
    
    # ─── FIX 1: Make hero elements visible immediately ───
    # Replace the .gsap-fade CSS to NOT hide above-fold elements
    # Hero elements (.hero-content, .hero-media) must start visible
    old_css = """.gsap-fade {
opacity: 0;
transform: translateY(24px);
transition: opacity 0.6s ease, transform 0.6s ease;
}
.gsap-fade.revealed {
opacity: 1;
transform: translateY(0);
}"""
    
    new_css = """.gsap-fade {
opacity: 0;
transform: translateY(24px);
transition: opacity 0.6s ease, transform 0.6s ease;
}
.gsap-fade.revealed {
opacity: 1;
transform: translateY(0);
}
.hero-section .gsap-fade {
opacity: 1;
transform: none;
}"""
    
    if old_css in content and '.hero-section .gsap-fade' not in content:
        content = content.replace(old_css, new_css)
        changes.append("Hero elements now visible immediately (fixes LCP)")
    
    # ─── FIX 2: Replace requestIdleCallback with navigator.sendBeacon ───
    # sendBeacon is fire-and-forget, does NOT create a network dependency chain entry
    old_track = """var sendTrack = function() { fetch('/api/track', { method: 'POST', body: JSON.stringify(payload), headers: {'Content-Type': 'application/json'}, keepalive: true }).catch(function(){}); };
    if ('requestIdleCallback' in window) { requestIdleCallback(sendTrack, {timeout: 2000}); } else { setTimeout(sendTrack, 100); }"""
    
    new_track = """if (navigator.sendBeacon) { navigator.sendBeacon('/api/track', new Blob([JSON.stringify(payload)], {type: 'application/json'})); } else { fetch('/api/track', { method: 'POST', body: JSON.stringify(payload), headers: {'Content-Type': 'application/json'}, keepalive: true }).catch(function(){}); }"""
    
    if old_track in content:
        content = content.replace(old_track, new_track)
        changes.append("Replaced requestIdleCallback with sendBeacon (removes /api/track from critical chain)")
    
    # ─── FIX 3: Add width/height to mecanismo image ───
    old_img_pattern = 'alt="Mecanismo'
    # Find the img tag for mecanismo and add width/height
    mecanismo_pattern = r'<img src="assets/mecanismos/[^"]*-desktop\.webp" alt="Mecanismo [^"]*" style="max-width: 100%; height: auto;'
    match = re.search(mecanismo_pattern, content)
    if match and 'width="800"' not in match.group():
        old_tag = match.group()
        new_tag = old_tag.replace('<img ', '<img width="800" height="600" ')
        content = content.replace(old_tag, new_tag)
        changes.append("Added width/height to mecanismo image (fixes CLS)")
    
    # ─── FIX 4: Add loading="lazy" to bonus images that have empty src ───
    # These are loaded dynamically by JS, add explicit dimensions
    content = re.sub(
        r'<img loading="lazy" src="" style="width: 100%; display: block; border-radius: 16px;" alt="([^"]*)"',
        r'<img loading="lazy" src="" width="400" height="300" style="width: 100%; display: block; border-radius: 16px;" alt="\1"',
        content
    )
    
    if changes:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[OK] {filepath}: {'; '.join(changes)}")
    else:
        print(f"[SKIP] {filepath}")

for f in sorted(glob.glob("oferta16_*.html")):
    fix_page(f)
