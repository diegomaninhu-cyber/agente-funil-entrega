const fs = require("fs");
const path = require("path");

const filePath = path.join(__dirname, "..", "oferta13.html");
let html = fs.readFileSync(filePath, "utf-8");

const map = {
  "Ã¡": "á",
  "Ã¢": "â",
  "Ã£": "ã",
  "Ã©": "é",
  "Ãª": "ê",
  "Ã­": "í", // might be this one
  "Ã\u00AD": "í", // soft hyphen explicit
  "Ã³": "ó",
  "Ã´": "ô",
  "Ãµ": "õ",
  "Ãº": "ú",
  "Ã§": "ç",
  "Ã€": "À",
  "Ã ": "Á", // MÃ QUINA
  "Ã‚": "Â",
  "Ãƒ": "Ã",
  "Ã„": "Ä",
  "Ã‰": "É",
  "ÃŠ": "Ê",
  "Ã“": "Ó",
  "Ã”": "Ô",
  "Ã•": "Õ",
  "Ãš": "Ú",
  "Ã‡": "Ç"
};

let fixes = 0;
for (const [bad, good] of Object.entries(map)) {
  const regex = new RegExp(bad, "g");
  const before = html;
  html = html.replace(regex, good);
  if (before !== html) fixes++;
}

fs.writeFileSync(filePath, html, "utf-8");
console.log(`Fixed ${fixes} different types of corrupted characters.`);
