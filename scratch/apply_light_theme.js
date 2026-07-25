const fs = require('fs');
let html = fs.readFileSync('oferta14.html', 'utf8');

// 1. Replace CSS variables
const oldVars = `:root {
    --background: #050505;
    --surface: #0A0A0A;
    --surface-2: #151515;
    --surface-3: #1A1A1A;
    --border: #222222;
    --primary: #D97757;
    --primary-light: #E69D84;
    --primary-dark: #A64E33;
    --white: #FFFFFF;
    --gray-50: #F5F5F5;
    --gray-100: #E5E5E5;
    --gray-200: #CFCFCF;
    --gray-300: #B5B5B5;
    --gray-400: #909090;
    --gray-500: #707070;
    --gray-600: #5C5C5C;
    --gray-700: #444444;
    --gray-800: #2A2A2A;
    --gray-900: #181818;`;

const newVars = `:root {
    --background: #faf9f5;
    --surface: #ffffff;
    --surface-2: #f2f1ec;
    --surface-3: #e8e6dc;
    --border: #e0ded5;
    --primary: #D97757;
    --primary-light: #E69D84;
    --primary-dark: #A64E33;
    --white: #141413;
    --gray-50: #141413;
    --gray-100: #2A2A2A;
    --gray-200: #444444;
    --gray-300: #5C5C5C;
    --gray-400: #707070;
    --gray-500: #909090;
    --gray-600: #B5B5B5;
    --gray-700: #CFCFCF;
    --gray-800: #E5E5E5;
    --gray-900: #F5F5F5;`;

html = html.replace(oldVars, newVars);

// 2. Replace hardcoded dark colors
html = html.replace(/#050505/g, 'var(--background)');
html = html.replace(/#090909/g, 'var(--surface)');
html = html.replace(/#080808/g, 'var(--surface)');
html = html.replace(/#0A0A0A/g, 'var(--surface)');
html = html.replace(/#111/g, 'var(--surface-2)');
html = html.replace(/#1A1A1A/g, 'var(--surface-2)');
html = html.replace(/#151515/g, 'var(--surface-2)');
html = html.replace(/#000/g, 'var(--surface-3)');

// Borders
html = html.replace(/#202020/g, 'var(--border)');
html = html.replace(/#222/g, 'var(--border)');
html = html.replace(/#242424/g, 'var(--border)');

// Opacity backgrounds
html = html.replace(/rgba\(0,0,0,0\.38\)/g, 'rgba(0,0,0,0.03)');
html = html.replace(/rgba\(0,0,0,0\.2\)/g, 'rgba(0,0,0,0.02)');
html = html.replace(/rgba\(0,0,0,0\.35\)/g, 'rgba(0,0,0,0.08)');
html = html.replace(/rgba\(0,0,0,0\.55\)/g, 'rgba(0,0,0,0.12)');
html = html.replace(/rgba\(0,0,0,0\.7\)/g, 'rgba(0,0,0,0.1)');
html = html.replace(/rgba\(0,0,0,0\.8\)/g, 'rgba(0,0,0,0.1)');
html = html.replace(/rgba\(8,8,8,0\.96\)/g, 'rgba(255,255,255,0.96)');
html = html.replace(/rgba\(8,8,8,1\)/g, 'rgba(255,255,255,1)');

fs.writeFileSync('oferta14.html', html, 'utf8');
console.log('Light theme applied to oferta14.html');
