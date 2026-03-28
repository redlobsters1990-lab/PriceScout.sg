# PUBLISHING.md — PriceScout.sg Publishing Infrastructure

## Live Site

**URL:** https://redlobsters1990-lab.github.io/PriceScout.sg/  
**Repo:** https://github.com/redlobsters1990-lab/PriceScout.sg  
**Branch:** `main` (source of truth)

---

## CI/CD Pipeline

### Workflow: Deploy to GitHub Pages

**File:** `.github/workflows/pages.yml`

**Trigger:** Every push to `main` (also supports manual `workflow_dispatch`)

**What it does:**
1. Checks out the full repo
2. Configures GitHub Pages
3. Uploads all files as a Pages artifact
4. Deploys to GitHub Pages CDN

**Deploy time:** ~15–30 seconds after push  
**Status:** Check [Actions tab](https://github.com/redlobsters1990-lab/PriceScout.sg/actions)

### How to publish new content

Any agent or user with `push` access to `main` can publish by:
1. Adding or editing HTML files in the appropriate folder (see structure below)
2. Committing and pushing to `main`
3. The workflow fires automatically and the site updates within ~30s

---

## Folder Structure for Product Content

```
PriceScout.sg/
├── index.html                          # Homepage — links to all comparison pages
├── styles.css                          # Global stylesheet (shared by all pages)
├── comparisons/                        # PRIMARY: manually curated comparison pages
│   ├── index.html                      # Comparison category index
│   ├── {product-slug}-singapore.html   # One file per product category
│   └── ...
├── generated-pages/                    # Auto-generated pages (pipeline output)
│   ├── index.html                      # Generated page index
│   ├── {product-slug}.html             # Output from generate_with_affiliate_links.py
│   └── ...
├── assets/                             # Images, SVGs, icons
│   └── {product-slug}-singapore.svg   # One SVG hero per comparison page
├── _templates/                         # Page scaffolds for new content
│   └── product-comparison-template.html
└── .github/
    └── workflows/
        └── pages.yml                   # CI/CD deploy workflow
```

### Naming convention for product pages

| Folder | Naming pattern | Example |
|--------|---------------|---------|
| `comparisons/` | `{product-slug}-singapore.html` | `mini-rice-cookers-singapore.html` |
| `generated-pages/` | `{product-slug}.html` | `portable-power-stations.html` |

**Slug rules:**
- Lowercase, hyphen-separated
- No underscores
- Singapore-specific pages get `-singapore` suffix

### Linking new pages from the homepage

After creating a new comparison page, add a card to `index.html` in the `.grid` section:

```html
<a href="{product-slug}-singapore.html" class="card">
  <h3>{Category Name}</h3>
  <p>{Short description, 1 sentence}</p>
  <span class="price">{Price range}</span>
</a>
```

For pages in `comparisons/`, the href should be `comparisons/{product-slug}-singapore.html`.

---

## GitHub Credentials Required for Agents

### Personal Access Token (PAT) Scopes

To push new content files to this repo, an agent needs a GitHub PAT with:

| Scope | Required? | Reason |
|-------|-----------|--------|
| `public_repo` | **Required** | Read + write access to this public repository (push commits) |
| `workflow` | **Required** | Update `.github/workflows/*.yml` files (needed if modifying CI/CD) |
| `read:org` | Optional | Needed only if working with org-level settings |

> **Minimum required:** `public_repo` + `workflow`

### How to supply the token to agents

1. Generate a PAT at: https://github.com/settings/tokens → **Fine-grained tokens** (recommended) or **Classic tokens**
2. For classic tokens, enable scopes: `repo` (includes `public_repo`) + `workflow`
3. Set the token as an environment variable:
   ```bash
   export GITHUB_TOKEN=ghp_xxxxxxxxxxxx
   ```
4. Configure git to use it:
   ```bash
   git remote set-url origin https://x-access-token:${GITHUB_TOKEN}@github.com/redlobsters1990-lab/PriceScout.sg.git
   ```

### Fine-grained PAT (recommended for tighter security)

For a **fine-grained PAT** scoped to only this repo:
- Repository: `redlobsters1990-lab/PriceScout.sg`
- Permissions:
  - `Contents`: **Read and write** (push commits)
  - `Actions`: **Read and write** (only if agent modifies workflows)
  - `Pages`: **Read** (to check deployment status)

---

## Product Comparison Page Structure

Each comparison page follows this section layout:

1. **`comparison-hero`** — Product title, lede, demand/price signals, CTAs
2. **`verdict-panel`** — Quick answer: who this is best for, use-case chips
3. **`content-card` (comparison table)** — Provider/Product, Price, Key Feature, Best For, CTA
4. **`content-card` (top picks)** — `pick-card` per shortlisted product
5. **`content-card` (detailed breakdown)** — `detail-card` per product
6. **`content-card` (price comparison)** — Retailer price table
7. **`content-card compact-section` (buying guide)** — What to prioritize, SG considerations
8. **`content-card compact-section` (FAQ)** — `<details>` / `<summary>` Q&A
9. **`final-panel`** — Final recommendation + CTA buttons
10. **`note-banner`** — Affiliate disclosure

See `_templates/product-comparison-template.html` for the full scaffold.

---

## Content Generation Script

**File:** `generate_with_affiliate_links.py`

This script auto-generates comparison pages from a product catalog JSON. Output goes to `generated-pages/`.

Usage: run locally or from a CI step, then commit the output to `main`.

---

## Deployment Checklist (for new pages)

- [ ] HTML file added to `comparisons/` or `generated-pages/`
- [ ] Asset SVG added to `assets/` (optional but recommended)
- [ ] Card added to `index.html` homepage
- [ ] `<link rel="canonical">` set correctly in the new page `<head>`
- [ ] All `href` paths use `/PriceScout.sg/` prefix (site root)
- [ ] Affiliate links use `rel="nofollow sponsored noopener"`
- [ ] Committed and pushed to `main`
- [ ] Confirmed workflow run succeeded in [Actions tab](https://github.com/redlobsters1990-lab/PriceScout.sg/actions)
