import glob
import re

def defer_track(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the PageView fetch and wrap it in requestIdleCallback
    old_pattern = "fetch('/api/track', { method: 'POST', body: JSON.stringify(payload), headers: {'Content-Type': 'application/json'}, keepalive: true }).catch(()=>{});"
    
    # Only replace within the PageView section (first occurrence)
    new_code = """var sendTrack = function() { fetch('/api/track', { method: 'POST', body: JSON.stringify(payload), headers: {'Content-Type': 'application/json'}, keepalive: true }).catch(function(){}); };
    if ('requestIdleCallback' in window) { requestIdleCallback(sendTrack, {timeout: 2000}); } else { setTimeout(sendTrack, 100); }"""
    
    # Replace only the first occurrence (PageView), leave InitiateCheckout alone
    idx = content.find(old_pattern)
    if idx != -1 and 'requestIdleCallback' not in content:
        content = content[:idx] + new_code + content[idx + len(old_pattern):]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[OK] Deferred /api/track in {filepath}")
    else:
        print(f"[SKIP] {filepath}")

for f in sorted(glob.glob("oferta16_*.html")):
    defer_track(f)
