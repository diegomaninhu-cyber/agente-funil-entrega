const fs = require('fs');
let html = fs.readFileSync('oferta13.html', 'utf8');
html = html.replace('+3.000', '+1.000');
fs.writeFileSync('oferta13.html', html, 'utf8');
console.log('Replaced +3.000 with +1.000');
