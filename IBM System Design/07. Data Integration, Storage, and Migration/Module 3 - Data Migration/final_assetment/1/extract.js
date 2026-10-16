const fs = require('fs');

const html = fs.readFileSync('D:/Ent/Learning/Cousera/IBM System Design/07. Data Integration, Storage, and Migration/Module 3 - Data Migration/final_assetment/1/Assignment_ Final Project Submission _ Coursera.html', 'utf8');

// Find all c-peer-review-submit-text or similar answer divs or cml-viewer
const regex = /<div[^>]*class="[^"]*rc-CML[^"]*"[^>]*>([\s\S]*?)<\/div>/g;
let m;
let count = 0;
while ((m = regex.exec(html)) !== null) {
  const text = m[1].replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim();
  if (text.length > 0) {
    console.log(`\n=== BLOCK ${++count} ===\n${text}`);
  }
}
