const fs = require('fs');
let html = fs.readFileSync('oferta13.html', 'utf8');

const startStr = '<!-- OFFER STACK PREVIEW -->';
const endStr = '<!-- PROBLEM -->';

const startIndex = html.indexOf(startStr);
const endIndex = html.indexOf(endStr);

if(startIndex !== -1 && endIndex !== -1) {
  const replacement = `<!-- OFFER STACK PREVIEW -->
  <section class="container" style="padding-top: 70px; padding-bottom: 70px;">
    <div class="stack-preview" style="display: block; text-align: center;">
      <div class="gsap-fade">
        <span class="hero-eyebrow">Treinamento e Ferramentas</span>
        <h2>Tudo que você acessa <span class="gold">Imediatamente</span></h2>
        <p style="margin-top: 20px; color: var(--gray-300); margin-left: auto; margin-right: auto; max-width: 600px;">O método entrega "skills especiais" para diagnosticar o que seu nicho quer comprar, garantindo conversão extrema sem desafios técnicos.</p>
      </div>
    </div>
  </section>

  `;
  
  html = html.substring(0, startIndex) + replacement + html.substring(endIndex);
  fs.writeFileSync('oferta13.html', html, 'utf8');
  console.log('Fixed offer stack preview');
} else {
  console.log('Could not find offer stack section');
}
