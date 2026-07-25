const fs = require('fs');
let html = fs.readFileSync('oferta13.html', 'utf8');

const old1 = 'Cria conteúdo sem saber qual ângulo vende.';
const old2 = 'A conversa morre antes de chegar na oferta.';

const new1 = 'Cria conteúdo sem saber como oferecer seu produto.';
const new2 = 'A conversa morre antes de chegar na venda.';

html = html.replace(old1, new1);
html = html.replace(old2, new2);

fs.writeFileSync('oferta13.html', html, 'utf8');
console.log('Sem IA list updated');
