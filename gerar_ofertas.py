import os
import re

base_file = "oferta13.html"

niches = {
    "estetica": {
        "title": '<h1 class="hero-title"><span class="mobile-line">CLAUDE: Copie e cole na sua Clínica</span> <span class="mobile-line">essa máquina de agendamentos na clínica</span> <span class="mobile-line gold">com IAs Automáticas.</span></h1>',
        "desc": '<p class="hero-description">Lote a agenda da sua clínica de estética com pacientes qualificados para procedimentos estéticos todos os dias, utilizando a tecnologia <strong style="color:var(--white)">claudeCode</strong>. Sem que sua clínica precise de especialistas em marketing.</p>',
        "problem_eyebrow": '<span class="problem-eyebrow">A Clínica Vazia</span>',
        "problem_title": '<h2 style="font-size: 52px; font-weight: 800; margin-bottom: 32px; line-height: 1.15;">A captação da clínica falhou <br><span class="gold">até agora</span></h2>',
        "prob_text1": 'A maioria das clínicas foca em postar "antes e depois" sem Agentes de IA na clínica e - pior - ainda "no escuro".<br>\n          O resultado? Ficam sem entender porque o Instagram da clínica não gera agendamentos, apenas seguidores curiosos.',
        "prob_text2": 'E Com "skills especiais" para diagnosticar o que o paciente da sua clínica quer (como botox, harmonização), garantimos conversão extrema na clínica.',
        "prob_text3": 'O FIM de curiosos: traga clientes para a clínica a partir de R$ 0,90.<br>\n          O FIM da recepção da clínica sobrecarregada.'
    },
    "medicos": {
        "title": '<h1 class="hero-title"><span class="mobile-line">CLAUDE: Copie e cole no Consultório Médico</span> <span class="mobile-line">essa máquina de pacientes particulares</span> <span class="mobile-line gold">com IAs Automáticas.</span></h1>',
        "desc": '<p class="hero-description">Atraia pacientes particulares para o seu consultório e gere agendamentos médicos todos os dias, utilizando a tecnologia <strong style="color:var(--white)">claudeCode</strong>. 100% alinhado às regras do CFM para consultórios.</p>',
        "problem_eyebrow": '<span class="problem-eyebrow">O Consultório Refém do Convênio</span>',
        "problem_title": '<h2 style="font-size: 52px; font-weight: 800; margin-bottom: 32px; line-height: 1.15;">O consultório não lota só <br><span class="gold">com indicação</span></h2>',
        "prob_text1": 'A maioria dos consultórios médicos foca em posts técnicos sem Agentes de IA e atraindo apenas pacientes de plano de saúde.<br>\n          O resultado? Consultório médico cheio de quem paga pouco e zero tempo livre.',
        "prob_text2": 'E Com "skills especiais" para triar o paciente médico, garantimos consultas particulares para o consultório de forma ética.',
        "prob_text3": 'O FIM dos planos médicos baratos: traga pacientes particulares para o consultório a partir de R$ 0,90.<br>\n          O FIM da secretária do consultório não dando conta do WhatsApp.'
    },
    "dentistas": {
        "title": '<h1 class="hero-title"><span class="mobile-line">CLAUDE: Copie e cole no Consultório</span> <span class="mobile-line">essa máquina de captação odontológica</span> <span class="mobile-line gold">com IAs Automáticas.</span></h1>',
        "desc": '<p class="hero-description">Feche mais tratamentos premium (lentes, implantes) no seu consultório odontológico todos os dias, utilizando a tecnologia <strong style="color:var(--white)">claudeCode</strong>. Captação automática para dentistas.</p>',
        "problem_eyebrow": '<span class="problem-eyebrow">A Cadeira do Dentista Vazia</span>',
        "problem_title": '<h2 style="font-size: 52px; font-weight: 800; margin-bottom: 32px; line-height: 1.15;">A indicação de boca a boca <br><span class="gold">não basta mais</span></h2>',
        "prob_text1": 'A maioria dos consultórios odontológicos vive de indicação sem Agentes de IA.<br>\n          O resultado? Pacientes fogem do consultório quando o dentista passa o orçamento de um tratamento premium.',
        "prob_text2": 'E Com "skills especiais" para qualificar o paciente odontológico antes dele sentar na cadeira, o consultório tem conversão extrema.',
        "prob_text3": 'O FIM de orçamentos odontológicos negados: traga pacientes decididos para o consultório.<br>\n          O FIM do dentista ficar no vácuo no WhatsApp.'
    },
    "advogados": {
        "title": '<h1 class="hero-title"><span class="mobile-line">CLAUDE: Copie e cole no Escritório</span> <span class="mobile-line">essa máquina de clientes jurídicos</span> <span class="mobile-line gold">com IAs Automáticas.</span></h1>',
        "desc": '<p class="hero-description">Receba contatos de clientes com causas de alto valor no seu escritório de advocacia todos os dias, com a tecnologia <strong style="color:var(--white)">claudeCode</strong>. 100% dentro da ética do escritório e da OAB.</p>',
        "problem_eyebrow": '<span class="problem-eyebrow">O Escritório sem Novos Casos</span>',
        "problem_title": '<h2 style="font-size: 52px; font-weight: 800; margin-bottom: 32px; line-height: 1.15;">O escritório de advocacia <br><span class="gold">perdeu clientes</span></h2>',
        "prob_text1": 'Muitos escritórios de advocacia têm medo do provimento da OAB e não prospectam, deixando o escritório sem Agentes de IA.<br>\n          O resultado? O escritório vive de processos pingados e perde para as bancas de advogados mais modernos.',
        "prob_text2": 'E Com "skills especiais" de informação jurídica ética, o escritório de advocacia atrai clientes com alta probabilidade.',
        "prob_text3": 'O FIM de correspondência jurídica: traga clientes finais para o escritório.<br>\n          O FIM do advogado com angústia sobre os honorários do mês.'
    },
    "psicologos": {
        "title": '<h1 class="hero-title"><span class="mobile-line">CLAUDE: Copie e cole na Psicoterapia</span> <span class="mobile-line">essa máquina de sessões particulares</span> <span class="mobile-line gold">com IAs Automáticas.</span></h1>',
        "desc": '<p class="hero-description">Lote sua agenda de sessões de psicoterapia com pacientes particulares sem precisar fazer dancinhas, utilizando a tecnologia <strong style="color:var(--white)">claudeCode</strong> nas suas consultas.</p>',
        "problem_eyebrow": '<span class="problem-eyebrow">A Exaustão da Sessão de Terapia</span>',
        "problem_title": '<h2 style="font-size: 52px; font-weight: 800; margin-bottom: 32px; line-height: 1.15;">As sessões por convênio <br><span class="gold">esgotam você</span></h2>',
        "prob_text1": 'Muitos psicólogos focam em frases motivacionais para vender terapia e acabam cobrando valores baixos por sessão.<br>\n          O resultado? Exaustão mental na clínica e baixa remuneração pelo seu trabalho psicoterapêutico.',
        "prob_text2": 'E Com "skills especiais" para acolher o paciente de terapia, garantimos fechamento de sessões particulares.',
        "prob_text3": 'O FIM de sessões de clínica mal pagas: traga pacientes que valorizam sua terapia.<br>\n          O FIM da insegurança financeira do psicólogo.'
    },
    "nutricionistas": {
        "title": '<h1 class="hero-title"><span class="mobile-line">CLAUDE: Copie e cole no Consultório</span> <span class="mobile-line">essa máquina de consultas de nutrição</span> <span class="mobile-line gold">com IAs Automáticas.</span></h1>',
        "desc": '<p class="hero-description">Lote sua agenda de consultas nutricionais e venda mais planos alimentares todos os dias, utilizando a tecnologia <strong style="color:var(--white)">claudeCode</strong> no consultório.</p>',
        "problem_eyebrow": '<span class="problem-eyebrow">A Consulta Prescrita de Graça</span>',
        "problem_title": '<h2 style="font-size: 52px; font-weight: 800; margin-bottom: 32px; line-height: 1.15;">O mercado da nutrição <br><span class="gold">sugou seu tempo</span></h2>',
        "prob_text1": 'Muitos nutricionistas postam receitas sem captação pro consultório nutricional e sem Agentes de IA.<br>\n          O resultado? Muito seguidor pegando dieta de graça, mas ninguém marcando consulta com a nutricionista.',
        "prob_text2": 'E Com "skills especiais" para converter curiosos que querem dieta, garantimos mais consultas no consultório nutricional.',
        "prob_text3": 'O FIM das dicas alimentares não valorizadas: venda planos nutricionais e consultas.<br>\n          O FIM da nutricionista passando dieta no direct de graça.'
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
