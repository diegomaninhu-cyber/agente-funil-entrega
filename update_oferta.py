import re

with open('oferta10.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update fonts
content = content.replace(
    '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">',
    '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Merriweather:ital,wght@0,300;0,400;0,700;0,900;1,300;1,400&display=swap" rel="stylesheet">'
)

# 2. Update :root
new_root = '''  :root {
    --bg: #1C1A19;
    --bg-2: #242221;
    --panel: #2A2826;
    --panel-2: #33312F;
    --light: #FAF8F5;
    --light-2: #F0EAE1;
    --ink: #EAE4D9;
    --ink-dark: #221F1E;
    --muted: #A39B95;
    --muted-dark: #66615E;
    --line: #3D3937;
    --line-light: #D9D2C5;
    
    --accent: #D97757;
    --accent-deep: #B85636;
    --accent-soft: rgba(217, 119, 87, 0.15);
    
    --green: #D97757;
    --green-2: #B85636;
    
    --shadow: 0 30px 60px rgba(0,0,0,0.6);
    --shadow-sm: 0 10px 30px rgba(0,0,0,0.4);
    --radius: 8px;
    --radius-lg: 12px;
    --maxw: 1040px;
    --fs: 'Inter', sans-serif;
    --fs-serif: 'Merriweather', serif;
  }'''
content = re.sub(r'  :root \{[^}]+\}', new_root, content)

# 3. Typography
content = content.replace('h1,h2,h3{line-height:1.2;font-weight:600;letter-spacing:-0.03em}', 'h1,h2,h3{line-height:1.2;font-family:var(--fs-serif);font-weight:700;letter-spacing:-0.01em;}')
content = re.sub(r'\.eyebrow\{[^}]+\}', '.eyebrow{display:inline-block;font-weight:600;letter-spacing:0.1em;text-transform:uppercase;font-size:0.8rem;color:var(--accent);margin-bottom:24px;font-family:var(--fs);}', content)
content = content.replace('.em{font-style:italic;font-weight:500}', '.em{font-style:italic;font-weight:400;font-family:var(--fs-serif)}')

# 4. Add Cycle CSS
cycle_css = '''
/* CYCLE CONTAINER */
.cycle-container { max-width: 900px; margin: 0 auto; background: var(--panel); border: 1px solid var(--line); border-radius: var(--radius-lg); padding: 48px; box-shadow: var(--shadow); }
.cycle-grid { display: flex; align-items: flex-start; justify-content: space-between; gap: 16px; }
.cycle-item { flex: 1; text-align: center; position: relative; }
.cycle-num { width: 40px; height: 40px; border-radius: 50%; background: var(--accent-soft); color: var(--accent); display: flex; align-items: center; justify-content: center; font-family: var(--fs-serif); font-size: 1.2rem; font-weight: 700; margin: 0 auto 24px; border: 1px solid var(--accent); }
.cycle-item h3 { font-size: 1rem; color: #fff; margin-bottom: 12px; }
.cycle-item p { font-size: 0.8rem; color: var(--muted); line-height: 1.5; }
.cycle-arrow { flex: 0 0 auto; padding-top: 10px; color: var(--line-light); }
@media(max-width: 860px) {
  .cycle-grid { flex-direction: column; align-items: center; gap: 40px; }
  .cycle-arrow { transform: rotate(90deg); padding-top: 0; }
}
'''
content = content.replace('/* VISUAL CARDS (UI MOCKUPS EM CSS) */', cycle_css + '\n/* VISUAL CARDS (UI MOCKUPS EM CSS) */')

# 5. Add Cycle HTML
cycle_html = '''
<!-- MECANISMO ÚNICO - CICLO AGÊNTICO -->
<section class="section" style="background:var(--bg-2)">
  <div class="wrap">
    <div class="center" style="margin-bottom:60px">
      <span class="eyebrow">A Diferença que Gera Vendas</span>
      <h2 style="color:#fff">O Ciclo Agêntico de Conversão</h2>
      <p class="lead" style="max-width:600px;margin:16px auto 0">Ao contrário das estratégias comuns de "postar e rezar", as IAs autônomas de 2026 executam um processo fechado de atração e venda.</p>
    </div>
    
    <div class="cycle-container">
      <div class="cycle-grid">
        <div class="cycle-item">
          <div class="cycle-num">1</div>
          <h3>Mapeamento <br>Profundo</h3>
          <p>A IA analisa o seu nicho, identifica as dores e cria o ângulo da oferta perfeito.</p>
        </div>
        <div class="cycle-arrow"><svg width="24" height="24" fill="none" stroke="var(--accent)" stroke-width="2" viewBox="0 0 24 24"><path d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg></div>
        <div class="cycle-item">
          <div class="cycle-num">2</div>
          <h3>Atração <br>de Precisão</h3>
          <p>Modelos de criativos gerados para pescar exatamente o cliente que quer comprar.</p>
        </div>
        <div class="cycle-arrow"><svg width="24" height="24" fill="none" stroke="var(--accent)" stroke-width="2" viewBox="0 0 24 24"><path d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg></div>
        <div class="cycle-item">
          <div class="cycle-num">3</div>
          <h3>Automação <br>Conversacional</h3>
          <p>A IA assume os comentários e o Direct, atendendo cada lead como um humano 24/7.</p>
        </div>
        <div class="cycle-arrow"><svg width="24" height="24" fill="none" stroke="var(--accent)" stroke-width="2" viewBox="0 0 24 24"><path d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg></div>
        <div class="cycle-item">
          <div class="cycle-num">4</div>
          <h3>Conversão e <br>Retroalimentação</h3>
          <p>O lead compra, o algoritmo do Instagram entende o perfil, e entrega mais leads parecidos.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- VALUE STACK -->'''
content = content.replace('<!-- VALUE STACK -->', cycle_html)

with open('oferta10.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Update successful')
