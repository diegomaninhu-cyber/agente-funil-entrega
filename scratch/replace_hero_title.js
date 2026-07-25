const fs = require('fs');
let html = fs.readFileSync('oferta13.html', 'utf8');

// The exact string in the HTML:
// <h1 class="hero-title"><span class="mobile-line">Transforme seu Instagram</span> <span class="mobile-line">numa máquina de vendas</span> <span class="mobile-line gold">com IAs Autônomas.</span></h1>

const newTitle = '<h1 class="hero-title"><span class="mobile-line">CLAUDE: Copie e cole no seu Instagram</span> <span class="mobile-line">essa máquina de seguidores e vendas</span> <span class="mobile-line gold">com IAs Automaticas.</span></h1>';

// Replace using regex to handle any potential whitespace/encoding differences
html = html.replace(/<h1 class="hero-title">[\s\S]*?<\/h1>/, newTitle);

fs.writeFileSync('oferta13.html', html, 'utf8');
console.log('Hero title replaced!');
