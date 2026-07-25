const fs = require('fs');
let html = fs.readFileSync('oferta13.html', 'utf8');

const oldList = `<li><i data-lucide="check" class="gold"></i> Automações de comentários, DMs e vendas</li>
            <li><i data-lucide="check" class="gold"></i> Scripts, Workflows e Prompts de "copiar e colar"</li>`;

const newList = `<li><i data-lucide="check" class="gold"></i> Skills de Seguidores e Vendas, Scripts, Workflows e Prompts de "copiar e colar"</li>`;

// Replace using a regex that handles whitespace flexibility
const regex = /<li><i data-lucide="check" class="gold"><\/i>\s*Automações de comentários, DMs e vendas<\/li>\s*<li><i data-lucide="check" class="gold"><\/i>\s*Scripts, Workflows e Prompts de "copiar e colar"<\/li>/;

html = html.replace(regex, newList);

fs.writeFileSync('oferta13.html', html, 'utf8');
console.log('List merged successfully!');
