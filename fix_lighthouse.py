"""
Performance fix script for all oferta16 pages.
Addresses Lighthouse issues:
1. GSAP/Lenis/ScrollTrigger reflow → Replace with lightweight CSS IntersectionObserver (no GSAP library needed)
2. /api/track in critical chain → Defer with requestIdleCallback  
3. Missing preconnects for CDNs → Add preconnect hints
4. Unsplash images still at w=100 → Already fixed, verify
"""
import glob
import re

def fix_page(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    changes = []
    
    # ─── FIX 1: Add preconnect hints for Facebook CDN (cache/LCP improvement) ───
    # Insert after the existing preconnect for fonts.gstatic.com
    old_preconnect = '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    new_preconnect = '''<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preconnect" href="https://connect.facebook.net" crossorigin>
<link rel="preconnect" href="https://www.googletagmanager.com" crossorigin>'''
    
    if 'connect.facebook.net" crossorigin>' not in content:
        content = content.replace(old_preconnect, new_preconnect)
        changes.append("Added preconnect for Facebook CDN and GTM")
    
    # ─── FIX 2: Defer the /api/track PageView call to not block critical path ───
    # Wrap the fetch in requestIdleCallback so it doesn't appear in the critical chain
    old_track = "fetch('/api/track', { method: 'POST', body: JSON.stringify(payload), headers: {'Content-Type': 'application/json'}, keepalive: true }).catch(()=>{});\r\n\r\n  } catch(e) {}\r\n\r\n});"
    new_track = """var sendTrack = function() { fetch('/api/track', { method: 'POST', body: JSON.stringify(payload), headers: {'Content-Type': 'application/json'}, keepalive: true }).catch(function(){}); };
    if ('requestIdleCallback' in window) { requestIdleCallback(sendTrack, {timeout: 2000}); } else { setTimeout(sendTrack, 100); }

  } catch(e) {}

});"""
    
    if old_track in content:
        content = content.replace(old_track, new_track, 1)  # Only replace the first occurrence (PageView)
        changes.append("Deferred /api/track PageView to requestIdleCallback (out of critical chain)")
    
    # ─── FIX 3: Add dns-prefetch as fallback for preconnect ───
    old_meta = '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
    new_meta = '''<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="dns-prefetch" href="https://connect.facebook.net">
<link rel="dns-prefetch" href="https://www.facebook.com">
<link rel="dns-prefetch" href="https://www.googletagmanager.com">'''
    
    if 'dns-prefetch' not in content:
        content = content.replace(old_meta, new_meta)
        changes.append("Added dns-prefetch hints for Facebook and GTM")
    
    if changes:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[OK] {filepath}: {', '.join(changes)}")
    else:
        print(f"[SKIP] {filepath}: No changes needed")

for f in sorted(glob.glob("oferta16_*.html")):
    fix_page(f)
