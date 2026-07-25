const fs = require('fs');
let html = fs.readFileSync('oferta13.html', 'utf8');

const regex1 = /<i data-lucide="check"><\/i> Coment.rio vira conversa automaticamente\./g;
html = html.replace(regex1, '<i data-lucide="check"></i> Comentário vira vendas automaticamente.');

const regex3 = /<i data-lucide="check"><\/i> Scripts e prompts deixam a mensagem mais persuasiva\./g;
html = html.replace(regex3, '<i data-lucide="check"></i> Scripts e prompts deixam a mensagem mais persuasiva e na sua comunicação.');

const regex4 = /<i data-lucide="check"><\/i> O lead chega no checkout entendendo a oferta\./g;
html = html.replace(regex4, '<i data-lucide="check"></i> O lead chega no momento da venda e compra.');


fs.writeFileSync('oferta13.html', html, 'utf8');
console.log('Com IA list updated again');
