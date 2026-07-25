import os
import re

base_file = "oferta13.html"

niches = {
    "estetica": {
        "title": '<h1 class="hero-title"><span class="mobile-line">CLAUDE: a máquina de seguidores</span> <span class="mobile-line">que vende pacientes premium para a</span> <span class="mobile-line gold">sua Clínica de Estética.</span></h1>',
        "desc": '<p class="hero-description">Pare de disputar preço na recepção. Instale a tecnologia <strong style="color:var(--white)">claudeCode</strong> na sua clínica e trie automaticamente apenas pacientes dispostos a pagar o preço justo pelos seus protocolos estéticos.</p>',
        "problem_eyebrow": '<span class="problem-eyebrow">A Recepção Esgotada</span>',
        "problem_title": '<h2 style="font-size: 52px; font-weight: 800; margin-bottom: 32px; line-height: 1.15;">Ter uma clínica cheia <br><span class="gold">não significa lucro</span></h2>',
        "prob_text1": 'Muitas donas de clínica vivem apagando incêndios, dependem de seguidores curiosos e não fecham pacotes premium por falta de automação.<br>\n          O resultado? Você trabalha 12h por dia mas o faturamento do mês fica empatado.',
        "prob_mecanismo": 'Existe um fenômeno comportamental chamado <strong style="color:var(--gold)">Fator Impulso</strong>. Na estética, as fotos de "Antes/Depois" rodam no tráfego pago pedindo a palavra "AVALIAÇÃO". Nossa IA chama na DM no exato milissegundo em que a paciente deseja a transformação, convertendo o impulso em agendamento imediato na sua recepção.',
        "prob_text2": 'Mas e se o seu Instagram filtrasse os curiosos e entregasse apenas pacientes agendados na recepção usando IAs de conversão?',
        "prob_text3": 'A solução definitiva para donos de clínica que precisam escalar.<br>\n          Lote sua agenda estética de forma automatizada a partir de R$ 0,90.'
    },
    "medicos": {
        "title": '<h1 class="hero-title"><span class="mobile-line">CLAUDE: a máquina de seguidores</span> <span class="mobile-line">que traz pacientes particulares para</span> <span class="mobile-line gold">Consultórios Médicos.</span></h1>',
        "desc": '<p class="hero-description">Ser um bom médico não enche consultório. A tecnologia <strong style="color:var(--white)">claudeCode</strong> cria um funil ético (CFM) que prospecta e agenda consultas particulares, libertando você dos convênios.</p>',
        "problem_eyebrow": '<span class="problem-eyebrow">O Refém do Convênio Médico</span>',
        "problem_title": '<h2 style="font-size: 52px; font-weight: 800; margin-bottom: 32px; line-height: 1.15;">Na faculdade não te ensinaram <br><span class="gold">a atrair pacientes particulares</span></h2>',
        "prob_text1": 'Médicos acreditam que apenas o boca-a-boca ou postar muito no Instagram resolverá a falta de consultas particulares.<br>\n          O resultado? A agenda até lota, mas de planos de saúde, sugando o seu tempo e gerando pouco lucro no consultório.',
        "prob_mecanismo": 'Existe um método de conversão inviolável chamado <strong style="color:var(--gold)">Isca Ética</strong>. Para o médico (e o CFM), a nossa IA entrega um material gratuito de alto valor automatizado antes de "vender" a consulta. Isso mantém a ética intacta, gera reciprocidade e qualifica o paciente brutalmente.',
        "prob_text2": 'Com agentes virtuais inteligentes, o paciente vê sua autoridade no anúncio, recebe sua isca e agenda a consulta sozinho.',
        "prob_text3": 'Recupere o controle da sua carreira médica e valorize sua consulta.<br>\n          Captação previsível para médicos modernos a partir de R$ 0,90.'
    },
    "dentistas": {
        "title": '<h1 class="hero-title"><span class="mobile-line">CLAUDE: a máquina de seguidores</span> <span class="mobile-line">que fecha orçamentos premium para</span> <span class="mobile-line gold">Consultórios Odontológicos.</span></h1>',
        "desc": '<p class="hero-description">Na cadeira você cuida da técnica, e a tecnologia <strong style="color:var(--white)">claudeCode</strong> cuida da sua captação. Traga clientes qualificados para Lentes, Implantes e Harmonização Orofacial todos os dias.</p>',
        "problem_eyebrow": '<span class="problem-eyebrow">A Cadeira do Suspiro</span>',
        "problem_title": '<h2 style="font-size: 52px; font-weight: 800; margin-bottom: 32px; line-height: 1.15;">Volume de pacientes não é estratégia <br><span class="gold">no seu consultório</span></h2>',
        "prob_text1": 'Por que seu consultório não lucra mesmo com a agenda cheia? Dentistas perdem tempo com orçamentos que dão trabalho e pacientes que pedem desconto.<br>\n          O resultado? Frustração e exaustão no final do dia na cadeira do dentista.',
        "prob_mecanismo": 'Existe um fenômeno comportamental chamado <strong style="color:var(--gold)">Fator Impulso</strong>. Na odontologia de alto padrão, depoimentos em vídeo rodam pedindo a palavra "AVALIAÇÃO". Nossa IA entra em ação na DM no exato instante em que o paciente quer aquele sorriso novo, convertendo desejo em orçamento fechado.',
        "prob_text2": 'Nossa IA converte o desejo de um sorriso novo em avaliações agendadas de forma automática, qualificando quem tem poder de compra.',
        "prob_text3": 'A captação ideal para a clínica odontológica que quer faturar alto.<br>\n          Chega de depender de panfletos ou agências ruins.'
    },
    "advogados": {
        "title": '<h1 class="hero-title"><span class="mobile-line">CLAUDE: a máquina de seguidores</span> <span class="mobile-line">que traz clientes rentáveis para</span> <span class="mobile-line gold">Escritórios de Advocacia.</span></h1>',
        "desc": '<p class="hero-description">Prospecte clientes com segurança sem ferir o Provimento da OAB. Instale a tecnologia <strong style="color:var(--white)">claudeCode</strong> no seu escritório e pare de esperar o cliente bater na sua porta.</p>',
        "problem_eyebrow": '<span class="problem-eyebrow">A Mesa Sem Processos Novos</span>',
        "problem_title": '<h2 style="font-size: 52px; font-weight: 800; margin-bottom: 32px; line-height: 1.15;">Você está perdendo honorários <br><span class="gold">por não saber escalar</span></h2>',
        "prob_text1": 'O medo da OAB e a falta de tempo impedem o advogado de prospectar clientes lucrativos.<br>\n          O resultado? Escritórios vivendo de correspondência jurídica barata enquanto outras bancas escalam faturamentos gigantes com tecnologia.',
        "prob_mecanismo": 'Existe um método de conversão inviolável chamado <strong style="color:var(--gold)">Isca Ética</strong>. Para bancas jurídicas e a OAB, a nossa IA entrega um manual de direitos básicos gratuito de forma automatizada antes de falar de honorários. Isso mantém a captação dentro da lei, gera reciprocidade e traz clientes prontos.',
        "prob_text2": 'Através da entrega ética de informações jurídicas no direct, a nossa IA cria autoridade imediata e filtra o cliente rentável para o escritório.',
        "prob_text3": 'Previsibilidade de honorários e causas de alto valor todos os meses.<br>\n          Coloque um Agente de IA para defender a captação da sua banca.'
    },
    "psicologos": {
        "title": '<h1 class="hero-title"><span class="mobile-line">CLAUDE: a máquina de seguidores</span> <span class="mobile-line">que escala as suas sessões e lota</span> <span class="mobile-line gold">sua Clínica Psicológica.</span></h1>',
        "desc": '<p class="hero-description">Saia da armadilha do convênio. A tecnologia <strong style="color:var(--white)">claudeCode</strong> prospecta pacientes particulares que valorizam a psicoterapia e preenche os buracos da sua agenda automaticamente.</p>',
        "problem_eyebrow": '<span class="problem-eyebrow">A Exaustão Emocional do Profissional</span>',
        "problem_title": '<h2 style="font-size: 52px; font-weight: 800; margin-bottom: 32px; line-height: 1.15;">Atender 10 pacientes de convênio <br><span class="gold">está esgotando você</span></h2>',
        "prob_text1": 'Psicólogos são treinados para ouvir, mas não para se promover. Muitos tentam dancinhas no Instagram para captar, sem sucesso.<br>\n          O resultado? Burnout profissional e uma remuneração incompatível com os anos de estudo.',
        "prob_mecanismo": 'Existe um método de conversão inviolável chamado <strong style="color:var(--gold)">Isca Ética</strong>. Para psicólogos (CRP), a nossa IA envia um teste de ansiedade ou checklist de bem-estar gratuito na DM antes de "vender" a terapia. Isso mantém a postura terapêutica impecável e qualifica o paciente.',
        "prob_text2": 'A automação envia triagens terapêuticas no direct, acolhendo o paciente e conduzindo-o suavemente ao fechamento da sessão particular.',
        "prob_text3": 'Valorize o seu conselho e a sua saúde mental de forma ética.<br>\n          Captação qualificada para psicólogos a partir de R$ 0,90.'
    },
    "nutricionistas": {
        "title": '<h1 class="hero-title"><span class="mobile-line">CLAUDE: a máquina de seguidores</span> <span class="mobile-line">que atrai pacientes particulares</span> <span class="mobile-line gold">para nutricionistas.</span></h1>',
        "desc": '<p class="hero-description">Chega de trabalhar de graça tirando dúvidas no direct. Aplique a tecnologia <strong style="color:var(--white)">claudeCode</strong> para transformar seguidores curiosos em agendamentos presenciais ou venda de e-books e desafios online.</p>',
        "problem_eyebrow": '<span class="problem-eyebrow">A Dieta Gratuita</span>',
        "problem_title": '<h2 style="font-size: 52px; font-weight: 800; margin-bottom: 32px; line-height: 1.15;">Seus seguidores adoram suas dicas, <br><span class="gold">mas fogem na hora de pagar</span></h2>',
        "prob_text1": 'Nutricionistas criam muito conteúdo gratuito (receitas, dicas), acreditando que a autoridade fará chover pacientes no consultório.<br>\n          O resultado? Pessoas sugam a dieta no Direct, mas a sua agenda clínica particular não sai do lugar.',
        "prob_mecanismo": 'Existe um fenômeno comportamental chamado <strong style="color:var(--gold)">Fator Impulso</strong>. Na nutrição, posts de transformação ou qualidade de vida rodam no tráfego pago pedindo a palavra "PLANO". Nossa IA entra em ação na DM no exato milissegundo em que o paciente deseja aquela mudança, convertendo o impulso em agendamento imediato da sua consulta particular.',
        "prob_text2": 'Nossa IA engaja o seguidor através de material gratuito e depois realiza uma triagem automatizada, ofertando o seu acompanhamento particular.',
        "prob_text3": 'Transforme o seu Instagram no melhor captador do seu consultório de nutrição.<br>\n          Feche planos trimestrais ou semestrais automaticamente.'
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

# The new mechanism paragraph replaces this generic sentence:
p_mecanismo_re = re.compile(r'Mas existe um fato usado por grandes nomes no mercado: O mecanismo que faz seu Instagram trabalhar por você\.', re.DOTALL)

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
        new_html = p_mecanismo_re.sub(data["prob_mecanismo"], new_html)
        new_html = p2_re.sub(data["prob_text2"], new_html)
        new_html = p3_re.sub(data["prob_text3"], new_html)

        out_name = f"oferta16_{niche}.html"
        with open(out_name, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print(f"Created {out_name}")

if __name__ == "__main__":
    generate()
