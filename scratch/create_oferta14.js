const fs = require('fs');

// 1. Copy oferta13.html to oferta14.html
const html13 = fs.readFileSync('oferta13.html', 'utf8');
let html14 = html13;

// 2. Replace CSS vars for Claude colors
html14 = html14.replace('--primary: #D7A84B;', '--primary: #D97757;');
html14 = html14.replace('--primary-light: #E8C574;', '--primary-light: #E69D84;');
html14 = html14.replace('--primary-dark: #9D6B19;', '--primary-dark: #A64E33;');

// Also replace any specific gold hex colors that might be hardcoded in styles
html14 = html14.replace(/rgba\(215,168,75,/g, 'rgba(217,119,87,'); // D97757 in RGB is 217,119,87
html14 = html14.replace(/#D7A84B/ig, '#D97757');

fs.writeFileSync('oferta14.html', html14, 'utf8');
console.log('oferta14.html created and colors updated');

// 3. Update server.js
let serverJs = fs.readFileSync('server.js', 'utf8');
if (!serverJs.includes('/oferta14')) {
    const routeCode = `app.get('/oferta13', (req, res) => {
  res.sendFile(path.join(__dirname, 'oferta13.html'));
});

app.get('/oferta14', (req, res) => {
  res.sendFile(path.join(__dirname, 'oferta14.html'));
});`;
    
    serverJs = serverJs.replace(`app.get('/oferta13', (req, res) => {
  res.sendFile(path.join(__dirname, 'oferta13.html'));
});`, routeCode);
    
    fs.writeFileSync('server.js', serverJs, 'utf8');
    console.log('server.js updated with /oferta14 route');
}
