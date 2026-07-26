import os, re
d = r'C:\Users\DELL\Documents\agente-funil\entrega'
files = [f for f in os.listdir(d) if f.endswith('.html') and 'oferta16' in f]

fixes = {
    'nutricionistas': '<h1 class="hero-title"><span class="mobile-line">Copie e Cole agora essa Máquina de Seguidores com IA -</span> <span class="mobile-line">que atrai pacientes particulares para</span> <span class="mobile-line gold">Consultórios e Clínicas de Nutricionistas.</span></h1>',
    'medicos': '<h1 class="hero-title"><span class="mobile-line">Copie e Cole agora essa Máquina de Seguidores com IA -</span> <span class="mobile-line">que traz pacientes particulares para</span> <span class="mobile-line gold">seu Consultório Médico.</span></h1>',
    'advogados': '<h1 class="hero-title"><span class="mobile-line">Copie e Cole agora essa Máquina de Seguidores</span> <span class="mobile-line">que traz com ÉTICA clientes rentáveis para</span> <span class="mobile-line gold">Escritórios de Advocacia - com IA.</span></h1>',
    'dentistas': '<h1 class="hero-title"><span class="mobile-line">Copie e Cole agora essa Máquina de Seguidores com IA -</span> <span class="mobile-line">que fecha orçamentos premium para</span> <span class="mobile-line gold">Consultórios Odontológicos.</span></h1>',
    'estetica': '<h1 class="hero-title"><span class="mobile-line">Copie e Cole agora essa Máquina de Seguidores com IA -</span> <span class="mobile-line">que traz pacientes premium para a</span> <span class="mobile-line gold">sua Clínica de Estética.</span></h1>',
    'psicologos': '<h1 class="hero-title"><span class="mobile-line">Copie e Cole agora essa Máquina de Seguidores com IA</span> <span class="mobile-line">para lotar suas sessões e</span> <span class="mobile-line gold">sua Clínica Psicológica.</span></h1>'
}

for f in files:
    path = os.path.join(d, f)
    with open(path, 'rb') as fp:
        content_bytes = fp.read()
    
    try:
        content = content_bytes.decode('utf-8')
    except:
        content = content_bytes.decode('latin-1')

    niche = f.split('_')[1].split('.')[0]
    if niche in fixes:
        new_content = re.sub(r'<h1 class="hero-title">.*?</h1>', fixes[niche], content, flags=re.DOTALL)
        
        with open(path, 'w', encoding='utf-8') as fp:
            fp.write(new_content)
        print(f'Fixed {f}')
