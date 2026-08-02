import glob

standard_gtm = """<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-MH2JBSDJ');</script>
<!-- End Google Tag Manager -->"""

delayed_gtm_pattern = """<!-- Google Tag Manager (Delayed) -->



<script>



(function(w,d,s,l,i){w[l]=w[l]||[];



var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';



var loaded=false;



function loadGTM(){



  if(loaded) return; loaded=true;



  w[l].push({'gtm.start': new Date().getTime(),event:'gtm.js'});



  j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;



  f.parentNode.insertBefore(j,f);



}



// Load on interaction



['scroll','mousemove','touchstart','click'].forEach(function(e){



  window.addEventListener(e, loadGTM, {once:true, passive:true});



});



// Fallback: load after 7 seconds



setTimeout(loadGTM, 7000);



})(window,document,'script','dataLayer','GTM-MH2JBSDJ');



</script>"""

def fix_gtm(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We will use string replacement but ignoring all the whitespace differences
    import re
    # Create a regex to match the delayed GTM block regardless of exact newlines
    regex_pattern = r'<!-- Google Tag Manager \(Delayed\) -->\s*<script>\s*\(function\(w,d,s,l,i\)\{.*?setTimeout\(loadGTM,\s*7000\);\s*\}\)\(window,document,\'script\',\'dataLayer\',\'GTM-MH2JBSDJ\'\);\s*</script>'
    
    if re.search(regex_pattern, content, re.DOTALL):
        content = re.sub(regex_pattern, standard_gtm, content, flags=re.DOTALL)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed GTM in {filepath}")
    else:
        print(f"Delayed GTM not found in {filepath}")

for f in glob.glob("oferta16_*.html"):
    fix_gtm(f)
