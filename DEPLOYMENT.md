# 🚀 GitHub Deployment & Team Sharing Guide

This guide explains how to host the **Email Template Designer Tool** on **GitHub Pages** and share it with your team members for instant, zero-setup access.

---

## ⚡ Instant GitHub Pages Deployment (Free, 1-Click)

The application is completely self-contained in `index.html`. It runs directly in any modern web browser without requiring a backend server, Node.js, or Python.

### Step 1: Initialize & Push to GitHub

If you haven't already initialized your Git repository:

```bash
git init
git add .
git commit -m "feat: complete email template designer with 12 synchronized themes and github pages deployment"
```

Create a new repository on [GitHub](https://github.com/new) (public or private organization repository), then link and push:

```bash
git remote add origin https://github.com/<your-username-or-org>/<repo-name>.git
git branch -M main
git push -u origin main
```

---

### Step 2: Enable GitHub Pages

1. Navigate to your repository on GitHub.
2. Click **⚙️ Settings** (top repository tabs).
3. In the left navigation menu, click **Pages** (under *Code and automation*).
4. Under **Build and deployment**:
   - **Source**: Select `Deploy from a branch`.
   - **Branch**: Select `main` (or your default branch) and folder `/ (root)`.
5. Click **Save**.

Within 30–60 seconds, GitHub Pages will deploy your dashboard. Your live URL will be:
```
https://<your-username-or-org>.github.io/<repo-name>/
```

Share this URL directly with your admissions, marketing, and operations teams!

---

## 🔒 Security & Client Privacy Hardening

This project has been fully audited and secured for production and public/team hosting:

| Security Vector | Implementation Detail | Status |
|---|---|:---:|
| **Zero Client Identifiers** | All real school client names, sensitive paths, and credentials have been completely purged from the codebase. | ✅ Verified (0 matches) |
| **Sandboxed Preview** | Rendered email templates execute inside isolated `iframe.srcdoc` containers, shielding host UI from CSS or script injection. | ✅ Hardened |
| **Zero External Secrets** | No API keys, passwords, or confidential database credentials exist in this repository. | ✅ Safe |
| **External Link Shielding** | All external links (maps, CDN icons, docs) use `rel="noopener noreferrer"`. | ✅ Enforced |
| **Client-Side JSZip** | Bulk export (`Export All 22 as ZIP`) and CRM CSV generation happen 100% in-browser without sending template data to any third-party server. | ✅ 100% Private |
| **Offline & Intranet Ready** | Can also be distributed as a ZIP archive or opened via `file://` / local intranet without internet access. | ✅ Ready |

---

## 🎨 12 Synchronized Brand Themes & Palette Tokens

Selecting any theme automatically synchronizes:
- **Brand Accent Color**: Primary buttons, top accent border, milestone step active indicator.
- **Outer Canvas Tint**: Background wrapper table.
- **Card Background**: Inner container box (`#ffffff` for clean light themes, `#131b2e` for dark mode).
- **Headlines & Subheadings**: High-contrast typography matching the color family.
- **Body Font Color**: Curated text reading hierarchy (`#334155`, `#1f2937`, or `#cbd5e1`).
- **Highlight Pills & Chips**: OTP codes, credentials boxes, notice strips, and badges.
- **Button Contrast Text**: WCAG AAA/AA compliant text (`#ffffff` or `#0f172a`).

### Available Curated Presets:
1. **Simply Blue** (`#2563eb`) • Clean corporate blue
2. **Emerald Luxe** (`#059669`) • Deep forest mint
3. **Classic Crimson** (`#991b1b`) • Heritage academic red
4. **Royal Indigo** (`#4f46e5`) • Regal modern indigo
5. **Sunset Amber** (`#d97706`) • Warm golden ochre
6. **Slate Noir** (`#0f172a`) • Minimalist slate monochrome
7. **Nordic Teal** (`#0d9488`) • Crisp arctic cyan
8. **Midnight Obsidian** (`#38bdf8`) • Premium dark mode velvet edition
9. **Amethyst Purple** (`#7c3aed`) • Sophisticated violet
10. **Coral Blossom** (`#e11d48`) • Vibrant terracotta rose
11. **Cyber Bronze** (`#854d0e`) • Warm espresso ivory
12. **Titanium Tech** (`#475569`) • High-tech platinum gray

---

## 👥 How Team Members Can Use the Tool

### Option A: Via Live Hosted GitHub Pages URL (Recommended)
Simply open the GitHub Pages URL in Google Chrome, Microsoft Edge, Safari, or Firefox. No installation necessary!

### Option B: Local One-Click Execution (Windows)
1. Clone or download the repository.
2. Double-click **`run_server.bat`**.
3. Browser automatically opens at `http://localhost:8000`.

### Option C: Rebuilding After Modifying Templates
If template files in `samples/Canonical Suite/` or scripts are updated, recompile with:
```bash
python build_dashboard.py
```
Then commit and push the updated `index.html` to update GitHub Pages automatically.
