const fs = require('fs');
let html = fs.readFileSync('oferta13.html', 'utf8');

const regex = /A maioria dos perfis foca em criar[\s\S]*?R\$ 0,90\.\s*<\/p>/;

const newParagraphs = `A maioria dos perfis foca em vendas sem Agentes de IA e - pior - ainda "no escuro".<br>
          O resultado? Ficam sem entender porque o Instagram não gera vendas do seu produto, sempre está com poucos comentários e views nos Stories.
        </p>
        
        <p style="margin-bottom: 24px; color: var(--gray-300); font-size: 18px; line-height: 1.6;">
          Mas existe um fato usado por grandes nomes no mercado: O mecanismo que faz seu Instagram trabalhar por você.
        </p>
        
        <p style="margin-bottom: 24px; color: var(--white); font-weight: 700; font-size: 20px;">
          E Com "skills especiais" para diagnosticar o que seu nicho quer, garantimos conversão extrema.
        </p>
        
        <p style="margin-bottom: 48px; color: var(--gray-300); font-size: 18px; line-height: 1.6;">
          O FIM de leads caros: traga pessoas qualificadas a partir de R$ 0,90.<br>
          O FIM de perfil com poucos seguidores e desengajados.
        </p>`;
  
if (html.match(regex)) {
  html = html.replace(regex, newParagraphs);
  console.log('Text replaced successfully');
} else {
  console.log('Regex did not match.');
}

fs.writeFileSync('oferta13.html', html, 'utf8');
