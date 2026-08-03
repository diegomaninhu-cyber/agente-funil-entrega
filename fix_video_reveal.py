"""
1. Replace video src from old opt to ultra compressed version
2. Add native CSS reveal animation (replaces GSAP-fade dependency)
"""
import glob
import re

def apply_fixes(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    changes = []
    
    # 1. Replace video hero reference
    if 'VIDEO-2026-07-26-01-31-38-opt.mp4' in content:
        content = content.replace('VIDEO-2026-07-26-01-31-38-opt.mp4', 'VIDEO-hero-ultra.mp4')
        changes.append("Updated hero video to ultra-compressed version")
    
    # 2. Add native CSS reveal system if not present
    # Insert CSS for .gsap-fade to work natively with IntersectionObserver
    reveal_css = """.gsap-fade {
opacity: 0;
transform: translateY(24px);
transition: opacity 0.6s ease, transform 0.6s ease;
}
.gsap-fade.revealed {
opacity: 1;
transform: translateY(0);
}"""
    
    reveal_js = """<script>
document.addEventListener('DOMContentLoaded',function(){
var fades=document.querySelectorAll('.gsap-fade');
if('IntersectionObserver' in window){
var obs=new IntersectionObserver(function(entries){
entries.forEach(function(e){if(e.isIntersecting){e.target.classList.add('revealed');obs.unobserve(e.target);}});
},{threshold:0.1,rootMargin:'0px 0px -40px 0px'});
fades.forEach(function(el){obs.observe(el);});
}else{fades.forEach(function(el){el.classList.add('revealed');});}
});
</script>"""
    
    if '.gsap-fade {' not in content:
        # Insert CSS before </style>
        content = content.replace('</style>', reveal_css + '\n</style>', 1)
        changes.append("Added native CSS reveal animation for .gsap-fade")
    
    if "gsap-fade.revealed" not in content or 'obs.observe' not in content:
        # Insert JS before </body>
        content = content.replace('</body>', reveal_js + '\n</body>', 1)
        changes.append("Added native IntersectionObserver for .gsap-fade (replaces GSAP)")
    
    if changes:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[OK] {filepath}: {', '.join(changes)}")
    else:
        print(f"[SKIP] {filepath}")

for f in sorted(glob.glob("oferta16_*.html")):
    apply_fixes(f)
