const fs = require('fs'); 
let html = fs.readFileSync('oferta13.html', 'utf8'); 
html = html.replace(/<div class="hero-actions">\s*<span class="hero-note">A compra acontece apenas na última dobra\. Aqui o botão serve para levar o lead direto ao preço\.<\/span>\s*<\/div>/g, ''); 
fs.writeFileSync('oferta13.html', html, 'utf8');
