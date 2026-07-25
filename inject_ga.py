import os
import re

dir_path = r'c:\Users\DELL\Documents\agente-funil\entrega'
ga_id = 'G-8Q4CT4XQQ1'
ga_script = f'''
  <!-- Google Analytics -->
  <script async src="https://www.googletagmanager.com/gtag/js?id={ga_id}"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', '{ga_id}');
  </script>
'''

files = [f for f in os.listdir(dir_path) if f.endswith('.html')]
modified = 0

for file in files:
    filepath = os.path.join(dir_path, file)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    dirty = False
    
    # Injeta script base no head se nao tiver
    if ga_id not in content:
        content = content.replace('</head>', f'{ga_script}</head>')
        dirty = True
        
    # Adiciona evento de Purchase no index.html se nao tiver
    if file == 'index.html' and "gtag('event', 'purchase'" not in content:
        purchase_event = f'''
    gtag('event', 'purchase', {{
      currency: 'BRL',
      value: 49.90,
      transaction_id: 'trans_' + Date.now()
    }});
'''
        content = content.replace("fbq('track', 'Purchase', { currency: 'BRL', value: 49.90 });", f"fbq('track', 'Purchase', {{ currency: 'BRL', value: 49.90 }});\n{purchase_event}")
        dirty = True
        
    if dirty:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        modified += 1
        print(f"Modificado: {file}")

print(f"Total modificado: {modified}")
