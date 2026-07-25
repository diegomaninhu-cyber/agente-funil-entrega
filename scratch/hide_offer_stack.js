const fs = require('fs');
let html = fs.readFileSync('oferta13.html', 'utf8');

const startStr = '<!-- OFFER STACK PREVIEW -->\n  <section class="container" style="padding-top: 70px; padding-bottom: 70px;">';
const newStr = '<!-- OFFER STACK PREVIEW -->\n  <section class="container" style="display: none; padding-top: 70px; padding-bottom: 70px;">';

html = html.replace(startStr, newStr);

fs.writeFileSync('oferta13.html', html, 'utf8');
console.log('Section hidden');
