const fs = require('fs');

const filePath = 'd:/Ent/Learning/Cousera/IBM System Design/07. Data Integration, Storage, and Migration/Module 3 - Data Migration/final_assetment/2/Assignment_ Final Project Submission _ Coursera.html';

if (!fs.existsSync(filePath)) {
  console.log('File does not exist:', filePath);
  process.exit(1);
}

const html = fs.readFileSync(filePath, 'utf8');

const regex = /<div[^>]*class="[^"]*rc-CML[^"]*"[^>]*>([\s\S]*?)<\/div>/g;
let m;
let count = 0;
while ((m = regex.exec(html)) !== null) {
  const text = m[1].replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim();
  if (text.length > 0) {
    console.log(`=== BLOCK ${++count} ===\n${text}\n`);
  }
}
