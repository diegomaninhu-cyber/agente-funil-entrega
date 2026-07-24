import os
import re

base_file = "oferta13.html"

niches = {
    "estetica": {
        "title": '<h1 class="hero-title"><span class="mobile-line">CLAUDE: Copie e cole na sua Clínica</span> <span class="mobile-line">essa máquina de agendamentos e vendas</span> <span class="mobile-line gold">com IAs Automáticas.</span></h1>',
        "desc": '<p class="hero-description">Lote a agenda da sua clínica de estética com pacientes qualificados para procedimentos todos os dias, utilizando o poder da tecnologia <strong style="color:var(--white)">claudeCode</strong> de 2026. Mesmo sem saber nada de tecnologia.</p>',
        "problem_eyebrow": '<span class="problem-eyebrow">A Agenda Vazia</span>',
        "problem_title": '<h2 style="font-size: 52px; font-weight: 800; margin-bottom: 32px; line-height: 1.15;">Sua captação falhou <br><span class="gold">até agora</span></h2>',
        "prob_text1": 'A maioria das clínicas foca em postar "antes e depois" sem Agentes de IA e - pior - ainda "no escuro".<br>\n          O resultado? Ficam sem entender porque o Instagram não gera agendamentos, apenas seguidores curiosos.',
        "prob_text2": 'E Com "skills especiais" para diagnosticar o que seu paciente de estética quer, garantimos conversão extrema.',
        "prob_text3": 'O FIM de curiosos: traga clientes qualificados a partir de R$ 0,90.<br>\n          O FIM da recepção sobrecarregada.'
    },
    "medicos": {
        "title": '<h1 class="hero-title"><span class="mobile-line">CLAUDE: Copie e cole no Consultório</span> <span class="mobile-line">essa máquina de pacientes particulares</span> <span class="mobile-line gold">com IAs Automáticas.</span></h1>',
        "desc": '<p class="hero-description">Atraia pacientes particulares que valorizam o seu trabalho e gere agendamentos todos os dias, utilizando o poder da tecnologia <strong style="color:var(--white)">claudeCode</strong> de 2026. Dentro das regras do CFM.</p>',
        "problem_eyebrow": '<span class="problem-eyebrow">O Marketing Médico Comum</span>',
        "problem_title": '<h2 style="font-size: 52px; font-weight: 800; margin-bottom: 32px; line-height: 1.15;">Sua secretária não dá conta <br><span class="gold">sozinha</span></h2>',
        "prob_text1": 'A maioria dos médicos foca em posts técnicos sem Agentes de IA e atraindo apenas pacientes de plano.<br>\n          O resultado? Consultório cheio de quem paga pouco e tempo escasso para a vida pessoal.',
        "prob_text2": 'E Com "skills especiais" para triar pacientes, garantimos conversão extrema de particulares de forma ética.',
        "prob_text3": 'O FIM de planos de saúde: traga pacientes particulares a partir de R$ 0,90.<br>\n          O FIM do WhatsApp atrasado.'
    },
    "dentistas": {
        "title": '<h1 class="hero-title"><span class="mobile-line">CLAUDE: Copie e cole no Consultório</span> <span class="mobile-line">essa máquina de captação de pacientes</span> <span class="mobile-line gold">com IAs Automáticas.</span></h1>',
        "desc": '<p class="hero-description">Feche mais tratamentos premium (lentes, implantes) todos os dias, utilizando o poder da tecnologia <strong style="color:var(--white)">claudeCode</strong> de 2026. Tudo automático.</p>',
        "problem_eyebrow": '<span class="problem-eyebrow">A Cadeira Vazia</span>',
        "problem_title": '<h2 style="font-size: 52px; font-weight: 800; margin-bottom: 32px; line-height: 1.15;">A indicação não <br><span class="gold">basta mais</span></h2>',
        "prob_text1": 'A maioria dos dentistas vive de indicação sem Agentes de IA.<br>\n          O resultado? Pacientes fogem no orçamento de um tratamento premium.',
        "prob_text2": 'E Com "skills especiais" para qualificar o paciente antes da cadeira, garantimos conversão extrema.',
        "prob_text3": 'O FIM de orçamentos negados: traga pacientes decididos.<br>\n          O FIM do WhatsApp ignorado.'
    },
    "advogados": {
        "title": '<h1 class="hero-title"><span class="mobile-line">CLAUDE: Copie e cole na Advocacia</span> <span class="mobile-line">essa máquina de clientes rentáveis</span> <span class="mobile-line gold">com IAs Automáticas.</span></h1>',
        "desc": '<p class="hero-description">Receba contatos de clientes com causas de alto valor todos os dias, com <strong style="color:var(--white)">claudeCode</strong> de 2026. 100% dentro dos limites éticos da OAB.</p>',
        "problem_eyebrow": '<span class="problem-eyebrow">A Captação Antiética</span>',
        "problem_title": '<h2 style="font-size: 52px; font-weight: 800; margin-bottom: 32px; line-height: 1.15;">Você limita seus <br><span class="gold">honorários</span></h2>',
        "prob_text1": 'Muitos têm medo do provimento da OAB e não prospectam, ficando sem Agentes de IA.<br>\n          O resultado? Vivem de processos pingados e perdem para escritórios modernos.',
        "prob_text2": 'E Com "skills especiais" de informação jurídica ética, atraímos clientes com alta probabilidade.',
        "prob_text3": 'O FIM de correspondência: traga clientes finais qualificados.<br>\n          O FIM da angústia de honorários.'
    },
    "psicologos": {
        "title": '<h1 class="hero-title"><span class="mobile-line">CLAUDE: Copie e cole no seu Perfil</span> <span class="mobile-line">essa máquina de pacientes particulares</span> <span class="mobile-line gold">com IAs Automáticas.</span></h1>',
        "desc": '<p class="hero-description">Lote sua agenda de psicoterapia com pacientes particulares sem precisar fazer dancinhas, utilizando <strong style="color:var(--white)">claudeCode</strong> de 2026.</p>',
        "problem_eyebrow": '<span class="problem-eyebrow">A Exaustão da Agenda</span>',
        "problem_title": '<h2 style="font-size: 52px; font-weight: 800; margin-bottom: 32px; line-height: 1.15;">Atender por convênio <br><span class="gold">esgota você</span></h2>',
        "prob_text1": 'A maioria foca em postar frases motivacionais e cobrar valores baixos.<br>\n          O resultado? Exaustão mental e baixa remuneração pelo seu trabalho clínico.',
        "prob_text2": 'E Com "skills especiais" para acolher o paciente, garantimos fechamento de particulares.',
        "prob_text3": 'O FIM de consultas mal pagas: traga pacientes que valorizam sua terapia.<br>\n          O FIM da insegurança financeira.'
    },
    "nutricionistas": {
        "title": '<h1 class="hero-title"><span class="mobile-line">CLAUDE: Copie e cole no Instagram</span> <span class="mobile-line">essa máquina de consultas e desafios</span> <span class="mobile-line gold">com IAs Automáticas.</span></h1>',
        "desc": '<p class="hero-description">Lote sua agenda de consultas e venda mais e-books todos os dias, utilizando a tecnologia <strong style="color:var(--white)">claudeCode</strong> de 2026.</p>',
        "problem_eyebrow": '<span class="problem-eyebrow">O Mercado Saturado</span>',
        "problem_title": '<h2 style="font-size: 52px; font-weight: 800; margin-bottom: 32px; line-height: 1.15;">A concorrência esmagou <br><span class="gold">seu engajamento</span></h2>',
        "prob_text1": 'Nutricionistas postam receitas sem captação e sem Agentes de IA.<br>\n          O resultado? Muito seguidor pegando dica de graça, mas ninguém marcando consulta.',
        "prob_text2": 'E Com "skills especiais" para converter curiosos, garantimos conversão extrema.',
        "prob_text3": 'O FIM das dicas não valorizadas: venda planos e consultas.<br>\n          O FIM de responder direct de graça.'
    }
}

orig_title = '<h1 class="hero-title"><span class="mobile-line">CLAUDE: Copie e cole no seu Instagram</span> <span class="mobile-line">essa máquina de seguidores e vendas</span> <span class="mobile-line gold">com IAs Automaticas.</span></h1>'
orig_desc = '<p class="hero-description">Prospecte seguidores e leads qualificados a partir de R$ 0,90 e gere vendas todos os dias, utilizando o poder da tecnologia <strong style="color:var(--white)">claudeCode</strong> de 2026. Mesmo que você não saiba nada de tecnologia.</p>'
orig_prob_eyebrow = '<span class="problem-eyebrow">A Criação no Escuro</span>'
orig_prob_title = '<h2 style="font-size: 52px; font-weight: 800; margin-bottom: 32px; line-height: 1.15;">Você fez errado <br><span class="gold">até agora</span></h2>'

# Regexes for the inner texts, because spacing can be tricky.
p1_re = re.compile(r'A maioria dos perfis foca em vendas sem Agentes de IA e - pior - ainda "no escuro"\.<br>.*?O resultado\? Ficam sem entender porque o Instagram não gera vendas do seu produto, sempre está com poucos comentários e views nos Stories\.', re.DOTALL)
p2_re = re.compile(r'E Com "skills especiais" para diagnosticar o que seu nicho quer, garantimos conversão extrema\.', re.DOTALL)
p3_re = re.compile(r'O FIM de leads caros: traga pessoas qualificadas a partir de R\$ 0,90\.<br>.*?O FIM de perfil com poucos seguidores e desengajados\.', re.DOTALL)

def generate():
    if not os.path.exists(base_file):
        print(f"Error: {base_file} not found.")
        return

    with open(base_file, 'r', encoding='utf-8') as f:
        html = f.read()

    for niche, data in niches.items():
        new_html = html.replace(orig_title, data["title"])
        new_html = new_html.replace(orig_desc, data["desc"])
        new_html = new_html.replace(orig_prob_eyebrow, data["problem_eyebrow"])
        new_html = new_html.replace(orig_prob_title, data["problem_title"])
        
        new_html = p1_re.sub(data["prob_text1"], new_html)
        new_html = p2_re.sub(data["prob_text2"], new_html)
        new_html = p3_re.sub(data["prob_text3"], new_html)

        out_name = f"oferta13_{niche}.html"
        with open(out_name, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print(f"Created {out_name}")

if __name__ == "__main__":
    generate()
