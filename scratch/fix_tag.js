const fs = require('fs');
let html = fs.readFileSync('oferta13.html', 'utf8');

const replacement = `<section class="seals-section container" style="padding-bottom: 60px;">
  <div class="hero-seals" style="margin: 0 auto;">
            <div class="hero-seal"><i data-lucide="zap"></i> Acesso imediato</div>
            <div class="hero-seal"><i data-lucide="shield-check"></i> Garantia 7 dias</div>
            <div class="hero-seal"><i data-lucide="credit-card"></i> Pagamento único</div>
            <div class="hero-seal"><i data-lucide="timer"></i> Implementação rápida</div>
  </div>
  </section>`;

const sealsSectionRegex = /<section class="seals-section container" style="padding-bottom: 60px;">[\s\S]*?<\/section>/;

html = html.replace(sealsSectionRegex, replacement);

fs.writeFileSync('oferta13.html', html, 'utf8');
console.log("Fixed unclosed tag!");
