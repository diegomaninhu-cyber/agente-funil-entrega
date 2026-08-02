import os
import glob
import re

lazy_script = """
<script>
document.addEventListener("DOMContentLoaded", function() {
  var lazyVideos = [].slice.call(document.querySelectorAll("video.lazy"));
  if ("IntersectionObserver" in window) {
    var lazyVideoObserver = new IntersectionObserver(function(entries, observer) {
      entries.forEach(function(video) {
        if (video.isIntersecting) {
          if (video.target.dataset.src) {
            video.target.src = video.target.dataset.src;
          }
          video.target.load();
          video.target.classList.remove("lazy");
          lazyVideoObserver.unobserve(video.target);
        }
      });
    }, { rootMargin: "200px 0px" });
    lazyVideos.forEach(function(lazyVideo) {
      lazyVideoObserver.observe(lazyVideo);
    });
  } else {
    // Fallback for older browsers
    lazyVideos.forEach(function(video) {
      if (video.dataset.src) video.src = video.dataset.src;
      video.load();
      video.classList.remove("lazy");
    });
  }
});
</script>
"""

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update the Hero video to load instantly with poster and optimized source
    # The current tag is: <video class="lazy" data-src="/VIDEO-2026-07-26-01-31-38.mp4" ...>
    hero_video_old = 'class="lazy" data-src="/VIDEO-2026-07-26-01-31-38.mp4"'
    hero_video_new = 'src="/VIDEO-2026-07-26-01-31-38-opt.mp4" poster="/VIDEO-2026-07-26-01-31-38-poster.webp" preload="auto"'
    
    if hero_video_old in content:
        content = content.replace(hero_video_old, hero_video_new)
        print(f"[{filepath}] Hero video updated for immediate loading.")
        
    # 2. Inject lazy load script if it doesn't exist
    if "IntersectionObserver" not in content and "lazyVideos" not in content:
        content = content.replace('</body>', lazy_script + '\n</body>')
        print(f"[{filepath}] Lazy load script injected.")
    else:
        print(f"[{filepath}] Lazy load script already exists.")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for html_file in glob.glob("oferta16_*.html"):
    process_file(html_file)
