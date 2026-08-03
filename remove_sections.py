"""
Remove two sections from all oferta16 pages:
1. flow-section ("O Ciclo Agêntico de Conversão")
2. mechanism-section ("Fluxos de Conversação com claudeCode")

All other fixes (hero-visible, sendBeacon, video-ultra, minification, preconnects) are preserved.
"""
import glob
import re

def remove_sections(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_size = len(content)
    changes = []

    # ─── Remove flow-section ("O Ciclo Agêntico de Conversão") ───
    # Pattern: <!-- CLAUDE FLOW --> ... </section>  followed by <!-- VIDEO SECTION -->
    flow_pattern = re.compile(
        r'<!--\s*CLAUDE FLOW\s*-->.*?</section>\s*(?=<!--)',
        re.DOTALL | re.IGNORECASE
    )
    new_content, n = flow_pattern.subn('', content)
    if n > 0:
        content = new_content
        changes.append(f"Removed flow-section (Ciclo Agêntico) x{n}")

    # ─── Remove mechanism-section ("Fluxos de Conversação com claudeCode") ───
    # Pattern: <!-- MECHANISM --> ... </section>  followed by <!-- BEFORE/AFTER or next section
    mech_pattern = re.compile(
        r'<!--\s*MECHANISM\s*-->.*?</section>\s*(?=<!--)',
        re.DOTALL | re.IGNORECASE
    )
    new_content, n = mech_pattern.subn('', content)
    if n > 0:
        content = new_content
        changes.append(f"Removed mechanism-section (Fluxos de Conversação) x{n}")

    new_size = len(content)
    saved = (original_size - new_size) / 1024

    if changes:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[OK] {filepath}: {'; '.join(changes)} | -{saved:.1f}KB")
    else:
        print(f"[SKIP] {filepath}: sections not found with comment markers")

for f in sorted(glob.glob("oferta16_*.html")):
    remove_sections(f)
