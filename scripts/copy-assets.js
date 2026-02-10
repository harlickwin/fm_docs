/**
 * Copy Assets Script
 * Copies necessary assets to the dist directory for packaging
 */

const fs = require('fs');
const path = require('path');

// Ensure dist directory exists
const distDir = path.join(__dirname, '..', 'dist');
if (!fs.existsSync(distDir)) {
  fs.mkdirSync(distDir, { recursive: true });
}

// Copy documentation files
const docsToCoopy = [
  'USER_GUIDE.md',
  'QUICK_START.md',
  'TROUBLESHOOTING.md',
  'README.md'
];

const docsDir = path.join(distDir, 'docs');
if (!fs.existsSync(docsDir)) {
  fs.mkdirSync(docsDir, { recursive: true });
}

docsToCoopy.forEach(doc => {
  const src = path.join(__dirname, '..', doc);
  const dest = path.join(docsDir, doc);
  
  if (fs.existsSync(src)) {
    fs.copyFileSync(src, dest);
    console.log(`Copied ${doc} to dist/docs/`);
  } else {
    console.warn(`Warning: ${doc} not found, skipping`);
  }
});

console.log('Asset copying complete!');
