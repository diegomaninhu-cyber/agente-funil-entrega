
const fs = require("fs");
const path = require("path");

const filePath = path.join(__dirname, "..", "oferta13.html");
let html = fs.readFileSync(filePath, "utf-8");

html = html.replace(
  /<title>.*?<\/title>/g,
  "<title>Máquina de Seguidores com IAs Autônomas 2026</title>"
);

html = html.replace(
  /TREINAMENTO PRÃ TICO E COMPLETO &nbsp;&bull;&nbsp; ACESSO IMEDIATO &nbsp;&bull;&nbsp; ATUALIZAÃ‡Ã•ES INCLUSAS/g,
  "TREINAMENTO PRÁTICO: COPIE, COLE E VEJA A MÁGICA ACONTECER EM 50 MINUTOS &nbsp;&bull;&nbsp; SEM PRECISAR SABER TECNOLOGIA"
);

html = html.replace(
  /<span class="hero-eyebrow">Oferta especial para quem veio pelo Instagram<\/span>/g,
  `<span class="hero-eyebrow">Inteligência Artificial Agêntica</span>`
);

html = html.replace(
  /<h1 class="hero-title">.*?<\/h1>/s,
  `<h1 class="hero-title"><span class="mobile-line">Transforme seu Instagram</span> <span class="mobile-line">numa máquina de vendas</span> <span class="mobile-line gold">com IAs Autônomas.</span></h1>`
);

html = html.replace(
  /<p class="hero-description">.*?<\/p>/s,
  `<p class="hero-description">Gere criativos, crie fluxos de conversa e capte leads por apenas R$ 0,90 utilizando o poder da tecnologia <strong style="color:var(--white)">claudeCode</strong> de 2026. Mesmo que você não saiba nada de tecnologia.</p>`
);

html = html.replace(
  /<ul class="hero-list">.*?<\/ul>/s,
  `<ul class="hero-list">
            <li><i data-lucide="check" class="gold"></i> Automações de comentários, DMs e vendas</li>
            <li><i data-lucide="check" class="gold"></i> Scripts, Workflows e Prompts de "copiar e colar"</li>
            <li><i data-lucide="check" class="gold"></i> Bônus: Aprenda a ter 6 meses de Claude Grátis</li>
          </ul>`
);

html = html.replace(
  /<h2>Do comentÃ¡rio <span class="gold">CLAUDE<\/span> atÃ© a compra<\/h2>\s*<p.*?>A \/oferta13 foi pensada para quem chegou pelo post ou anÃºncio. Ela conecta a curiosidade do comentÃ¡rio com uma sequÃªncia simples: conversa, desejo, clique e checkout.<\/p>/s,
  `<h2>O Ciclo Agêntico <span class="gold">de Conversão</span></h2>
          <p style="margin-top: 18px; color: var(--gray-300); font-size: 17px;">Ao contrário das estratégias comuns de "postar e rezar", as IAs autônomas de 2026 executam um processo fechado de atração e venda.</p>`
);

html = html.replace(
  /<span class="hero-eyebrow">O caminho do lead<\/span>/g,
  `<span class="hero-eyebrow">A Diferença que Gera Vendas</span>`
);

html = html.replace(
  /<div class="flow-steps">.*?<\/div>\s*<\/div>/s,
  `<div class="flow-steps">
          <div class="flow-step">
            <strong>01</strong>
            <h4>Mapeamento Profundo</h4>
            <p>A IA analisa seu nicho e dores para criar o ângulo perfeito.</p>
          </div>
          <div class="flow-step">
            <strong>02</strong>
            <h4>Atração de Precisão</h4>
            <p>Modelos de criativos para pescar o cliente exato.</p>
          </div>
          <div class="flow-step">
            <strong>03</strong>
            <h4>Automação Conversacional</h4>
            <p>A IA assume comentários e Direct, atendendo 24/7.</p>
          </div>
          <div class="flow-step">
            <strong>04</strong>
            <h4>Conversão &amp; Venda</h4>
            <p>O lead compra, o algoritmo entende e entrega mais leads.</p>
          </div>
        </div>
      </div>`
);

html = html.replace(
  /<span class="hero-eyebrow">VocÃª recebe hoje<\/span>\s*<h2>NÃ£o Ã© sÃ³ uma aula: Ã© a mÃ¡quina completa para copiar, adaptar e colocar para rodar.<\/h2>\s*<p.*?>A oferta antecipa o valor antes do preÃ§o: o lead entende exatamente o que recebe, por que isso resolve o problema e por que R\$49,90 parece uma decisÃ£o simples.<\/p>/s,
  `<span class="hero-eyebrow">Treinamento e Ferramentas</span>
        <h2>Tudo que você acessa <span class="gold">Imediatamente</span></h2>
        <p style="margin-top: 20px; color: var(--gray-300);">O método entrega "skills especiais" para diagnosticar o que seu nicho quer comprar, garantindo conversão extrema sem desafios técnicos.</p>`
);

html = html.replace(
  /<div class="stack-list gsap-fade">.*?<\/div>\s*<\/div>/s,
  `<div class="stack-list gsap-fade">
        <div class="stack-item"><i data-lucide="bot"></i><div><strong>Skill Especial de Diagnóstico e Funil</strong><span>Instruções exatas para a IA descobrir o produto perfeito para o seu nicho.</span></div></div>
        <div class="stack-item"><i data-lucide="megaphone"></i><div><strong>Criação de Anúncios e Criativos com IA</strong><span>10 modelos validados gerados por IA para atrair demanda.</span></div></div>
        <div class="stack-item"><i data-lucide="message-circle"></i><div><strong>Workflows de Conversação e Atendimento</strong><span>Scripts e templates testados para conduzir o lead até a venda no Direct.</span></div></div>
        <div class="stack-item"><i data-lucide="book-open"></i><div><strong>Biblioteca de Prompts Sêniores</strong><span>Os exatos comandos para o claudeCode gerar sua automação.</span></div></div>
        <div class="stack-item"><i data-lucide="unlock"></i><div><strong>6 meses de Claude Grátis</strong><span>O segredo prático para acessar a IA mais avançada sem custos.</span></div></div>
      </div>
    </div>`
);

html = html.replace(
  /<span class="problem-eyebrow">O gargalo escondido<\/span>\s*<h2 style="font-size: 52px; font-weight: 800; margin-bottom: 32px; line-height: 1.15;">O problema nÃ£o Ã© sÃ³ atrair lead. <br><span class="gold">Ã‰ perder o lead no atendimento.<\/span><\/h2>.*?<\/div>\s*<div class="problem-grid">/s,
  `<span class="problem-eyebrow">A Criação no Escuro</span>
      <h2 style="font-size: 52px; font-weight: 800; margin-bottom: 32px; line-height: 1.15;">Você está criando conteúdo <br><span class="gold">baseado em suposições?</span></h2>
      
      <p style="margin-bottom: 24px; color: var(--gray-300); font-size: 18px; line-height: 1.6;">
        A maioria dos perfis foca em criar conteúdo "no escuro" e tenta atrair "qualquer um".<br>
        O resultado? Seguidores desqualificados que apenas curtem e nunca compram o seu produto.
      </p>
      
      <p style="margin-bottom: 24px; color: var(--gray-300); font-size: 18px; line-height: 1.6;">
        Mas existe um segredo usado por grandes nomes: a produção orientada à demanda com automação conversacional.<br>
        Seu Instagram precisa trabalhar por você.
      </p>
      
      <p style="margin-bottom: 24px; color: var(--white); font-weight: 700; font-size: 20px;">
        O anúncio e a postagem são ditados pela oferta e pela dor do cliente.
      </p>
      
      <p style="margin-bottom: 48px; color: var(--gray-300); font-size: 18px; line-height: 1.6;">
        Com "skills especiais" para diagnosticar o que seu nicho quer, garantimos conversão extrema.<br>
        Chega de leads caros: traga pessoas qualificadas a partir de R$ 0,90.
      </p>
    </div>
    
    <div class="problem-grid">`
);

html = html.replace(
  /<h2>O que muda quando a DM deixa de depender sÃ³ de vocÃª\?<\/h2>/g,
  `<h2>O que muda com <span class="gold">IAs Autônomas</span> na sua operação?</h2>`
);

html = html.replace(
  /<h3>Sem IA estratÃ©gica<\/h3>/g,
  `<h3>Sem IA Estratégica</h3>`
);

html = html.replace(
  /<h3>Com a MÃ¡quina<\/h3>/g,
  `<h3>Com IAs Autônomas</h3>`
);

html = html.replace(
  /<div class="mini-proof-card"><strong>â€œComentou, entrou no fluxo.â€ <\/strong>.*?<\/div>\s*<div class="mini-proof-card"><strong>â€œDM nÃ£o pode esfriar.â€ <\/strong>.*?<\/div>\s*<div class="mini-proof-card"><strong>â€œOferta precisa estar clara.â€ <\/strong>.*?<\/div>/s,
  `<div class="mini-proof-card"><strong>Automações 24/7</strong><p>A IA nunca dorme e inicia o atendimento instantaneamente, aumentando a conversão.</p></div>
      <div class="mini-proof-card"><strong>Persuasão Agêntica</strong><p>O roteiro inteligente mantém velocidade, contexto e conduz a chamada para a ação.</p></div>
      <div class="mini-proof-card"><strong>Venda Imediata</strong><p>A página apresenta bônus, prova visual, preço e garantia antes de pedir a compra.</p></div>`
);

html = html.replace(
  /<span class="mech-eyebrow">O mecanismo da \/oferta13<\/span>\s*<h2 style="font-size: 48px; font-weight: 800; margin-bottom: 32px; line-height: 1.15;">Um funil simples: <br><span class="gold">post, comentÃ¡rio, DM e checkout<\/span><\/h2>.*?<div class="mech-btn">/s,
  `<span class="mech-eyebrow">O Mecanismo de 2026</span>
          <h2 style="font-size: 48px; font-weight: 800; margin-bottom: 32px; line-height: 1.15;">Fluxos de Conversação <br><span class="gold">com claudeCode</span></h2>
          
          <p style="margin-bottom: 24px; color: var(--gray-300); font-size: 17px; line-height: 1.6;">
            Imagine uma estrutura onde a IA cria seus anúncios,<br>
            analisa seu produto e, assim que você posta, assume o controle.<br>
            O seguidor comenta, e instantaneamente um <span style="color:var(--primary); font-weight:700;">fluxo de conversa</span> se inicia.
          </p>
          
          <p style="margin-bottom: 24px; color: var(--gray-300); font-size: 17px; line-height: 1.6;">
            A IA nutre o lead, entrega a oferta, realiza o atendimento<br>
            básico e <span style="color:var(--primary); font-weight:700;">guia a pessoa até o fechamento</span>.<br>
            Tudo enquanto você está focado em entregar o seu serviço.
          </p>
          
          <p style="margin-bottom: 32px; color: var(--gray-300); font-size: 17px; line-height: 1.6;">
            E a melhor parte? Independente do seu nicho, nós<br>
            entregamos uma <span style="color:var(--primary); font-weight:700;">Biblioteca de Prompts Sêniores Testados e<br>Validados</span>. Basta plugar no seu negócio.
          </p>

          <div class="mech-btn">`
);

fs.writeFileSync(filePath, html, "utf-8");
console.log("Replacement complete!");

