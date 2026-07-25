const fs = require('fs');
let html = fs.readFileSync('oferta13.html', 'utf8');

// Add the highlight CSS if not present
if (!html.includes('.flow-step.highlight')) {
  const cssInjection = `
  .flow-step.highlight {
    border-color: var(--primary);
    background: rgba(215,168,75,0.08);
    transform: translateY(-4px);
    box-shadow: 0 12px 24px rgba(215,168,75,0.15);
    transition: all 0.3s ease;
  }
  `;
  html = html.replace('.flow-step p {', cssInjection + '\n  .flow-step p {');
}

// Add the class to item 03
// The HTML has:
// <div class="flow-step">
//   <strong>03</strong>
//   <h4>Automação Conversacional</h4>
//   <p>A IA assume comentários e Direct, atendendo 24/7.</p>
// </div>

const item03 = `<div class="flow-step">
            <strong>03</strong>
            <h4>Automação Conversacional</h4>`;
const item03New = `<div class="flow-step highlight">
            <strong>03</strong>
            <h4>Automação Conversacional</h4>`;

html = html.replace(item03, item03New);

// Also handle the encoded version if necessary, though regex with specific strings might be better
const regex03 = /<div class="flow-step">\s*<strong>03<\/strong>\s*<h4>Automação Conversacional<\/h4>/;
if (html.match(regex03)) {
    html = html.replace(regex03, '<div class="flow-step highlight">\n            <strong>03</strong>\n            <h4>Automação Conversacional</h4>');
} else {
    // try looser matching
    const looseRegex = /<div class="flow-step">\s*<strong>03<\/strong>/;
    html = html.replace(looseRegex, '<div class="flow-step highlight">\n            <strong>03</strong>');
}


fs.writeFileSync('oferta13.html', html, 'utf8');
console.log('Item 3 highlighted!');
