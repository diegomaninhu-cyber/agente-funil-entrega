const fs = require('fs');
let html = fs.readFileSync('oferta13.html', 'utf8');

const heroSealsRegex = /(<div class="hero-seals">[\s\S]*?<\/div>\s*<\/div>)/;
const match = html.match(/(<div class="hero-seals">[\s\S]*?)(<\/div>\s*<\/div>\s*<div class="hero-media)/);

if(match) {
  const sealsBlock = match[1];
  
  // Remove from hero
  html = html.replace(sealsBlock, '');
  
  // Now find seals-section
  const sealsSectionRegex = /<section class="seals-section container">[\s\S]*?<\/section>/;
  const newSealsSection = `<section class="seals-section container" style="padding-bottom: 60px;">\n  ` + sealsBlock.replace('class="hero-seals"', 'class="hero-seals" style="margin: 0 auto;"') + `\n  </section>`;
  
  html = html.replace(sealsSectionRegex, newSealsSection);
  
  fs.writeFileSync('oferta13.html', html, 'utf8');
  console.log("Moved seals to the bottom!");
} else {
  console.log("hero-seals not found!");
}
