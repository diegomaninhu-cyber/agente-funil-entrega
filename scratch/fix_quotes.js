const fs = require("fs");
const path = require("path");

const filePath = path.join(__dirname, "..", "oferta13.html");
let html = fs.readFileSync(filePath, "utf-8");

const map = {
  "â€”": "—",
  "âŸº": "⟷",
  "â† ": "← ", // left arrow with space
  "â†’": "→",
  "â€œ": "“",
  "â€\x9D": "”", // right double quote (invisible 9D)
  "â”€": "─"
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
