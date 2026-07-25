const fs = require('fs');
let html = fs.readFileSync('oferta13.html', 'utf8');

const oldTextRegex = /Gere criativos, crie fluxos de conversa e capte leads por apenas R\$ 0,90 utilizando o poder da tecnologia <strong style="color:var\(--white\)">claudeCode<\/strong> de 2026\. Mesmo que você não saiba nada de tecnologia\./;
const newText = 'Prospecte seguidores e leads qualificados a partir de R$ 0,90 e gere vendas todos os dias, utilizando o poder da tecnologia <strong style="color:var(--white)">claudeCode</strong> de 2026. Mesmo que você não saiba nada de tecnologia.';

html = html.replace(oldTextRegex, newText);

fs.writeFileSync('oferta13.html', html, 'utf8');
console.log('Description replaced successfully!');
