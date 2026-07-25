const fs = require('fs');
let html = fs.readFileSync('oferta13.html', 'utf8');
const start = html.indexOf('<div class="stack-list gsap-fade">');
const end = html.indexOf('</section>', start);

if(start !== -1 && end !== -1) {
  const replacement = '<div style="display: none;">\n' + html.substring(start, end) + '</div>\n';
  html = html.substring(0, start) + replacement + html.substring(end);
  html = html.replace('<div class="stack-preview">', '<div class="stack-preview" style="display: block; text-align: center;">');
  
  // also let's center the <p> description
  html = html.replace('<p style="margin-top: 20px; color: var(--gray-300);">', '<p style="margin-top: 20px; color: var(--gray-300); margin-left: auto; margin-right: auto; max-width: 600px;">');
  
  fs.writeFileSync('oferta13.html', html, 'utf8');
  console.log('Fixed');
}
