# Complete Game Mechanics Extraction - Tasks

## Overview
Generate a browsable GitHub Pages website with all game mechanics extracted from IL2CPP dump. Include icons, search functionality, and modern UI.

## Task List

### Phase 1: Core Extraction System (COMPLETE ✓)
- [x] 1.1 Create ProperExtractor class with IL2CPP dump parsing
- [x] 1.2 Implement class extraction with regex patterns
- [x] 1.3 Implement enum extraction with regex patterns
- [x] 1.4 Implement field extraction from class bodies
- [x] 1.5 Implement enum value extraction
- [x] 1.6 Handle backing field cleanup (`<Name>k__BackingField` → `Name`)
- [x] 1.7 Implement categorization by game system

### Phase 2: Icon Extraction System
- [ ] 2.1 Create IconExtractor class
- [ ] 2.2 Implement APK unzipping and asset exploration
- [ ] 2.3 Locate icon directories in APK assets
- [ ] 2.4 Extract skill icons (18 skills from CombatSkill enum)
- [ ] 2.5 Extract currency icons (9 currencies from CurrencyType enum)
- [ ] 2.6 Extract weapon icons (from weapon types)
- [ ] 2.7 Implement placeholder SVG generation for missing icons
- [ ] 2.8 Implement icon optimization (resize to 64x64, compress)
- [ ] 2.9 Generate category icons (9 categories with colors)

### Phase 3: Website Generator
- [ ] 3.1 Create WebsiteGenerator class
- [ ] 3.2 Implement JSON data generation (mechanics.json for search)
- [ ] 3.3 Implement homepage generation (index.html)
  - [ ] 3.3.1 Category cards with stats
  - [ ] 3.3.2 Key mechanics highlights
  - [ ] 3.3.3 Search button
- [ ] 3.4 Implement category page generation (9 category pages)
  - [ ] 3.4.1 Category header with icon
  - [ ] 3.4.2 Enum grid
  - [ ] 3.4.3 Class grid
- [ ] 3.5 Implement mechanic page generation (1000+ pages)
  - [ ] 3.5.1 Mechanic header with icon
  - [ ] 3.5.2 Code reference section
  - [ ] 3.5.3 Fields/values table
  - [ ] 3.5.4 Notes section
  - [ ] 3.5.5 Related mechanics section
- [ ] 3.6 Implement search page generation (search.html)

### Phase 4: Frontend Assets
- [ ] 4.1 Create CSS stylesheet (assets/css/style.css)
  - [ ] 4.1.1 Color scheme with category colors
  - [ ] 4.1.2 Typography (Inter font)
  - [ ] 4.1.3 Layout and grid system
  - [ ] 4.1.4 Component styles (cards, tables, badges)
- [ ] 4.2 Create responsive CSS (assets/css/responsive.css)
  - [ ] 4.2.1 Mobile styles (< 640px)
  - [ ] 4.2.2 Tablet styles (640px - 1024px)
  - [ ] 4.2.3 Desktop styles (> 1024px)
- [ ] 4.3 Add dark mode support (prefers-color-scheme)
- [ ] 4.4 Add syntax highlighting (Prism.js)
  - [ ] 4.4.1 Include prism.css
  - [ ] 4.4.2 Include prism.js
- [ ] 4.5 Create search functionality (assets/js/search.js)
  - [ ] 4.5.1 Load mechanics.json
  - [ ] 4.5.2 Implement fuzzy search
  - [ ] 4.5.3 Implement category filters
  - [ ] 4.5.4 Render search results
- [ ] 4.6 Create main JavaScript (assets/js/main.js)
  - [ ] 4.6.1 Navigation handling
  - [ ] 4.6.2 Theme toggle (if needed)

### Phase 5: Integration & Testing
- [ ] 5.1 Update ProperExtractor to call WebsiteGenerator
- [ ] 5.2 Update ProperExtractor to call IconExtractor
- [ ] 5.3 Test extraction on full IL2CPP dump
- [ ] 5.4 Verify all 1,008 classes have pages
- [ ] 5.5 Verify all 1,116 enums have pages
- [ ] 5.6 Test search functionality
- [ ] 5.7 Test responsive design on mobile/tablet/desktop
- [ ] 5.8 Test dark mode
- [ ] 5.9 Verify all links work
- [ ] 5.10 Verify icons display correctly

### Phase 6: GitHub Pages Deployment
- [ ] 6.1 Create docs/ folder structure
- [ ] 6.2 Generate all HTML pages to docs/
- [ ] 6.3 Copy assets to docs/assets/
- [ ] 6.4 Copy icons to docs/assets/icons/
- [ ] 6.5 Create docs/README.md with deployment instructions
- [ ] 6.6 Create .nojekyll file (disable Jekyll processing)
- [ ] 6.7 Test locally with Python HTTP server
- [ ] 6.8 Commit docs/ folder to repository
- [ ] 6.9 Enable GitHub Pages in repository settings
- [ ] 6.10 Verify website is live at github.io URL

### Phase 7: Documentation & Cleanup
- [ ] 7.1 Update main README.md with website link
- [ ] 7.2 Create DEPLOYMENT.md with instructions
- [ ] 7.3 Document icon extraction process
- [ ] 7.4 Document website generation process
- [ ] 7.5 Create example screenshots
- [ ] 7.6 Remove old GAME_MECHANICS_MANUAL.md (or keep as backup)

## Detailed Task Breakdown

### Task 2.1: Create IconExtractor Class
**File:** `tools/icon_extractor.py`

**Requirements:**
- Extract icons from APK assets
- Generate placeholder SVGs for missing icons
- Optimize icons for web (64x64px)
- Match icons to mechanics by name

**Implementation:**
```python
class IconExtractor:
    def __init__(self, apk_path: str, output_dir: str):
        self.apk_path = Path(apk_path)
        self.output_dir = Path(output_dir)
    
    def extract_all(self):
        """Extract all icons from APK."""
        self._unzip_apk()
        self._extract_skill_icons()
        self._extract_currency_icons()
        self._extract_weapon_icons()
        self._generate_category_icons()
        self._generate_placeholders()
    
    def _unzip_apk(self):
        """Unzip APK to temp directory."""
        pass
    
    def _extract_skill_icons(self):
        """Extract icons for 18 combat skills."""
        pass
    
    def _generate_placeholder(self, name: str, color: str) -> str:
        """Generate SVG placeholder icon."""
        pass
```

### Task 3.2: Implement JSON Data Generation
**File:** `tools/proper_extraction.py` (update)

**Requirements:**
- Generate mechanics.json with all classes and enums
- Include searchable fields (name, category, fields, values)
- Include URLs to mechanic pages

**Implementation:**
```python
def _generate_json(self):
    """Generate JSON data for search."""
    data = {
        "classes": [cls.to_dict() for cls in self.classes.values()],
        "enums": [enum.to_dict() for enum in self.enums.values()]
    }
    
    output_path = self.output_dir / "data" / "mechanics.json"
    with open(output_path, 'w') as f:
        json.dump(data, f, indent=2)
```

### Task 3.3: Implement Homepage Generation
**File:** `tools/website_generator.py`

**Requirements:**
- Display total stats (1,008 classes, 1,116 enums)
- Show 9 category cards with icons and counts
- Highlight key mechanics (currency, weapons, RNG, combat)
- Link to search page

**Implementation:**
```python
def generate_index(self):
    """Generate homepage."""
    template = self._load_template("index.html")
    
    categories = self._get_category_stats()
    highlights = self._get_key_mechanics()
    
    html = template.render(
        total_classes=len(self.classes),
        total_enums=len(self.enums),
        categories=categories,
        highlights=highlights
    )
    
    self._write_html("index.html", html)
```

### Task 4.5: Create Search Functionality
**File:** `docs/assets/js/search.js`

**Requirements:**
- Load mechanics.json on page load
- Implement fuzzy search (Fuse.js or custom)
- Filter by category checkboxes
- Display results with links to mechanic pages

**Implementation:**
```javascript
let mechanicsData = null;

async function loadData() {
    const response = await fetch('../data/mechanics.json');
    mechanicsData = await response.json();
}

function search(query) {
    const results = [];
    
    // Search classes
    for (const cls of mechanicsData.classes) {
        if (cls.name.toLowerCase().includes(query.toLowerCase())) {
            results.push(cls);
        }
    }
    
    // Search enums
    for (const enm of mechanicsData.enums) {
        if (enm.name.toLowerCase().includes(query.toLowerCase())) {
            results.push(enm);
        }
    }
    
    return results;
}

function renderResults(results) {
    const container = document.getElementById('search-results');
    container.innerHTML = results.map(r => `
        <a href="${r.url}" class="search-result">
            <h3>${r.name}</h3>
            <span class="category">${r.category}</span>
            <span class="line">Line ${r.line}</span>
        </a>
    `).join('');
}
```

### Task 6.7: Test Locally
**Command:**
```bash
cd docs
python -m http.server 8000
# Open http://localhost:8000 in browser
```

**Verify:**
- Homepage loads
- Category pages load
- Mechanic pages load
- Search works
- Icons display
- Links work
- Responsive design works
- Dark mode works

### Task 6.9: Enable GitHub Pages
**Steps:**
1. Go to repository Settings
2. Navigate to Pages section
3. Source: Deploy from a branch
4. Branch: main
5. Folder: /docs
6. Save
7. Wait for deployment (1-2 minutes)
8. Visit https://[username].github.io/[repo-name]/

## Dependencies

### Python Packages
```
Pillow>=10.0.0        # Image processing
jinja2>=3.1.0         # HTML templating
```

### JavaScript Libraries
```
prism.js              # Code syntax highlighting
```

### Optional
```
fuse.js               # Better fuzzy search (if needed)
```

## File Structure

```
tournament-pro/
├── tools/
│   ├── proper_extraction.py      # Main extraction script (updated)
│   ├── website_generator.py      # NEW: Website generation
│   ├── icon_extractor.py         # NEW: Icon extraction
│   └── templates/                # NEW: HTML templates
│       ├── index.html
│       ├── category.html
│       ├── mechanic.html
│       └── search.html
├── docs/                          # NEW: GitHub Pages output
│   ├── index.html
│   ├── search.html
│   ├── categories/
│   ├── mechanics/
│   ├── assets/
│   └── data/
└── .kiro/specs/complete-extraction/
    ├── requirements.md
    ├── design.md
    └── tasks.md
```

## Success Criteria

### Extraction
✓ 1,008 game mechanics classes extracted
✓ 1,116 enums extracted
✓ Every entry has line number
✓ Zero assumptions made

### Website
- [ ] GitHub Pages website is live
- [ ] All 1,008 classes have individual pages
- [ ] All 1,116 enums have individual pages
- [ ] 9 category pages exist
- [ ] Search functionality works
- [ ] Icons display (extracted or placeholder)
- [ ] Mobile responsive
- [ ] Dark mode support
- [ ] All links work
- [ ] Fast loading (<2s per page)

### Quality
- [ ] 100% code-based content
- [ ] 0% assumptions
- [ ] Every mechanic verifiable with line numbers
- [ ] Professional UI/UX
- [ ] Accessible (WCAG AA)

## Timeline Estimate

- **Phase 1:** Complete ✓
- **Phase 2:** 4-6 hours (icon extraction)
- **Phase 3:** 6-8 hours (website generation)
- **Phase 4:** 4-6 hours (frontend assets)
- **Phase 5:** 2-3 hours (integration & testing)
- **Phase 6:** 1-2 hours (deployment)
- **Phase 7:** 1-2 hours (documentation)

**Total:** 18-27 hours

## Next Steps

1. Review and approve this task list
2. Start with Phase 2 (Icon Extraction)
3. Proceed through phases sequentially
4. Test thoroughly before deployment
5. Deploy to GitHub Pages
6. Share website URL

The spec is now updated for GitHub Pages website generation!
