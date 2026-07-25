const fs = require('fs');
let html = fs.readFileSync('oferta13.html', 'utf8');

const regex = /Veja como o mecanismo funciona <span class="gold">na pr[\s\S]*?tica<\/span>/;
const newText = 'Veja como o mecanismo de agentes Claude interagindo <span class="gold">para venda</span>';

html = html.replace(regex, newText);

fs.writeFileSync('oferta13.html', html, 'utf8');
console.log('Mechanism title replaced successfully!');
