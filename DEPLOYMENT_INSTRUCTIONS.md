# Deployment Instructions for GitHub Pages

## Current Status
✅ Git repository initialized
✅ Files committed locally
✅ Remote added: https://github.com/harlickwin/fm_docs.git
❌ Push pending (requires authentication)

## To Deploy the Website

### Step 1: Push to GitHub
```bash
git push -u origin main
```

You'll be prompted for GitHub authentication. Use one of these methods:
- **Personal Access Token** (recommended)
- **GitHub Desktop** (easiest)
- **SSH Key**

### Step 2: Enable GitHub Pages
1. Go to https://github.com/harlickwin/fm_docs
2. Click **Settings**
3. Scroll to **Pages** section
4. Under **Source**, select:
   - Branch: `main`
   - Folder: `/docs`
5. Click **Save**

### Step 3: Wait for Deployment
- GitHub will build and deploy your site (1-2 minutes)
- Your site will be live at: **https://harlickwin.github.io/fm_docs/**

## What's Included

### Homepage (`docs/index.html`)
- ⚔️ Combat mechanics (attack speed, damage, crit, dodge, block)
- 🎲 Summoning & RNG (seeded system explained)
- 💰 Currency system (all 9 currencies with optimization)
- 📈 Progression & investment (ROI calculations)

### War & PvP Page (`docs/war-pvp.html`)
- 🛡️ Guild war matchmaking (two-week cycle confirmed)
- ⚔️ PvP arena leagues (promotion/demotion system)
- 🏰 Dungeon scaling (how level affects drops)
- 🎲 Egg drop mechanics (deterministic seeding explained)

### Styling (`docs/assets/css/style.css`)
- Modern, responsive design
- Mobile-friendly
- Dark/light theme support
- Professional look

## Files Structure
```
docs/
├── index.html              # Main page
├── war-pvp.html           # War & PvP mechanics
├── assets/
│   └── css/
│       └── style.css      # Styling
└── README.md              # Documentation
```

## Local Testing
To test locally before pushing:
```bash
cd docs
python -m http.server 8000
# Open http://localhost:8000
```

## What Still Needs Investigation

### Guild War
- ✅ Two-week matchmaking cycle (dev confirmed)
- ❓ Exact tier point thresholds (need GuildTierConfig values)
- ❓ Tier point gain/loss formulas

### PvP Arena
- ✅ League system structure (LeagueId, PromotionEnd, DemotionStart)
- ❓ Exact PvP stat multipliers (need PvpBaseConfig values)
- ❓ Rating calculation formula

### Dungeons
- ✅ Level scaling concept (DifficultyMultiplier)
- ❓ Exact multiplier values per level
- ❓ Drop table values per dungeon level

### Shop
- ❓ Whether shop is seeded (like eggs)
- ❓ Refresh algorithm details
- ❓ Item selection logic

## How to Add More Content

### To add a new page:
1. Create `docs/new-page.html`
2. Copy structure from existing pages
3. Add link in navigation
4. Commit and push

### To update existing content:
1. Edit the HTML files in `docs/`
2. Test locally
3. Commit and push
4. GitHub Pages auto-updates

## Troubleshooting

### Push fails with authentication error
- Use GitHub Desktop (easiest)
- Or create Personal Access Token:
  1. GitHub → Settings → Developer settings → Personal access tokens
  2. Generate new token with `repo` scope
  3. Use token as password when pushing

### Site not updating
- Wait 1-2 minutes for GitHub to rebuild
- Hard refresh browser (Ctrl+F5)
- Check GitHub Actions tab for build status

### Styling looks broken
- Ensure `assets/css/style.css` is committed
- Check browser console for errors
- Verify file paths are relative

## Next Steps

1. **Push to GitHub** (see Step 1 above)
2. **Enable GitHub Pages** (see Step 2 above)
3. **Share the URL**: https://harlickwin.github.io/fm_docs/
4. **Add more mechanics** as you discover them
5. **Update values** when you verify exact numbers

## Contact
If you need help with deployment, check:
- GitHub Pages documentation: https://pages.github.com/
- GitHub authentication: https://docs.github.com/en/authentication

---

**The website is ready to deploy!** Just push to GitHub and enable Pages.
