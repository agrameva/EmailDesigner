import os

def build(clients_json, templates_json, campuses_json, crm_vars_json):
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Email Template Designer | Simply Admission</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js"></script>
    <style>
        :root {{
            --bg-base: #06090f;
            --bg-panel: #0d131f;
            --bg-surface: #141c2c;
            --bg-elevated: #1b263b;
            --bg-input: #080d15;
            --border-subtle: rgba(255, 255, 255, 0.08);
            --border-strong: rgba(255, 255, 255, 0.15);
            --border-focus: #3b82f6;
            --primary: #2563eb;
            --primary-hover: #1d4ed8;
            --primary-subtle: rgba(37, 99, 235, 0.15);
            --success: #10b981;
            --success-hover: #059669;
            --success-subtle: rgba(16, 185, 129, 0.15);
            --warning: #f59e0b;
            --danger: #ef4444;
            --text-main: #f8fafc;
            --text-secondary: #94a3b8;
            --text-dim: #64748b;
            --radius-xs: 4px;
            --radius-sm: 6px;
            --radius-md: 8px;
            --radius-lg: 12px;
            --radius-full: 9999px;
            --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.25);
            --shadow-md: 0 4px 20px rgba(0, 0, 0, 0.35);
            --shadow-float: 0 16px 40px rgba(0, 0, 0, 0.5);
        }}

        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
            background: var(--bg-base);
            color: var(--text-main);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            overflow: hidden;
            -webkit-font-smoothing: antialiased;
        }}

        /* ───── Top Command Navigation ───── */
        .top-nav {{
            min-height: 52px;
            height: auto;
            background: rgba(13, 19, 31, 0.92);
            backdrop-filter: blur(14px);
            border-bottom: 1px solid var(--border-subtle);
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            justify-content: space-between;
            align-items: center;
            padding: 8px 16px;
            flex-shrink: 0;
            z-index: 100;
        }}
        .nav-left {{
            display: flex;
            align-items: center;
            gap: 12px;
        }}
        .nav-brand {{
            display: flex;
            align-items: center;
            gap: 8px;
            text-decoration: none;
            cursor: pointer;
        }}
        .nav-logo-badge {{
            width: 28px;
            height: 28px;
            border-radius: var(--radius-sm);
            background: linear-gradient(135deg, #2563eb, #38bdf8);
            color: #ffffff;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 13px;
            font-weight: 800;
            letter-spacing: -0.5px;
            box-shadow: 0 2px 10px rgba(37, 99, 235, 0.45);
        }}
        .nav-brand-title {{
            font-size: 0.88rem;
            font-weight: 700;
            color: var(--text-main);
            display: flex;
            align-items: center;
            gap: 6px;
            letter-spacing: -0.2px;
        }}
        .nav-brand-title span {{
            font-size: 0.68rem;
            background: var(--bg-surface);
            color: var(--text-secondary);
            border: 1px solid var(--border-subtle);
            padding: 1px 6px;
            border-radius: var(--radius-xs);
            font-weight: 600;
        }}

        /* Campus Quick Pills */
        .campus-pills-bar {{
            display: flex;
            align-items: center;
            gap: 4px;
            background: rgba(0, 0, 0, 0.3);
            padding: 2px 4px;
            border-radius: var(--radius-sm);
            border: 1px solid var(--border-subtle);
        }}
        .campus-pill-btn {{
            background: transparent;
            border: none;
            color: var(--text-secondary);
            padding: 4px 9px;
            border-radius: var(--radius-xs);
            font-size: 0.72rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.15s ease;
            white-space: nowrap;
        }}
        .campus-pill-btn:hover {{
            color: var(--text-main);
            background: rgba(255, 255, 255, 0.06);
        }}
        .campus-pill-btn.active {{
            background: var(--primary);
            color: #ffffff;
            box-shadow: 0 1px 8px rgba(37, 99, 235, 0.4);
        }}

        /* Navigation View Tabs */
        .top-view-tabs {{
            display: flex;
            gap: 3px;
            background: rgba(0, 0, 0, 0.3);
            padding: 3px;
            border-radius: var(--radius-md);
            border: 1px solid var(--border-subtle);
        }}
        .top-view-tab {{
            padding: 5px 12px;
            font-size: 0.76rem;
            font-weight: 600;
            color: var(--text-secondary);
            background: transparent;
            border: none;
            border-radius: var(--radius-sm);
            cursor: pointer;
            transition: all 0.15s ease;
            display: flex;
            align-items: center;
            gap: 6px;
        }}
        .top-view-tab:hover {{
            color: var(--text-main);
        }}
        .top-view-tab.active {{
            background: var(--bg-surface);
            color: #ffffff;
            box-shadow: var(--shadow-sm);
        }}

        .nav-right-actions {{
            display: flex;
            align-items: center;
            gap: 6px;
            flex-wrap: wrap;
        }}

        /* More Actions Dropdown for responsive consolidation */
        .more-actions-dropdown-wrap {{
            display: none;
            position: relative;
        }}
        .more-actions-menu {{
            display: none;
            position: absolute;
            top: calc(100% + 6px);
            right: 0;
            min-width: 220px;
            background: var(--bg-surface);
            border: 1px solid var(--border-strong);
            border-radius: var(--radius-sm);
            box-shadow: var(--shadow-float);
            padding: 6px 0;
            z-index: 200;
        }}
        .more-actions-menu.show {{
            display: flex;
            flex-direction: column;
        }}
        .more-action-item {{
            display: flex;
            align-items: center;
            gap: 8px;
            padding: 8px 14px;
            background: transparent;
            border: none;
            color: var(--text-main);
            font-size: 0.76rem;
            font-weight: 500;
            text-align: left;
            cursor: pointer;
            transition: background 0.12s ease;
            width: 100%;
        }}
        .more-action-item:hover {{
            background: var(--primary-subtle);
            color: #60a5fa;
        }}

        /* ───── App Main Body ───── */
        .app-body {{
            flex: 1;
            display: flex;
            overflow: hidden;
            position: relative;
        }}

        .app-view {{
            flex: 1;
            display: none;
            overflow: hidden;
        }}
        .app-view.active {{
            display: flex;
        }}

        /* Mobile Segmented Switcher */
        .mobile-mode-switcher {{
            display: none;
            background: var(--bg-panel);
            border-bottom: 1px solid var(--border-subtle);
            padding: 6px 12px;
            justify-content: center;
            gap: 8px;
            flex-shrink: 0;
            width: 100%;
        }}
        .mobile-mode-btn {{
            flex: 1;
            max-width: 180px;
            padding: 6px 12px;
            background: transparent;
            border: 1px solid var(--border-subtle);
            border-radius: var(--radius-sm);
            color: var(--text-secondary);
            font-size: 0.74rem;
            font-weight: 600;
            cursor: pointer;
            text-align: center;
        }}
        .mobile-mode-btn.active {{
            background: var(--primary);
            color: #ffffff;
            border-color: var(--primary);
        }}

        /* ═══════════════════════════════════════════════════════
           VIEW 1: TEMPLATE STUDIO
        ═══════════════════════════════════════════════════════ */
        #view-studio {{
            flex-direction: row;
        }}

        /* Left Editor Panel */
        .studio-editor-panel {{
            flex: 0 0 350px;
            width: 350px;
            height: calc(100vh - 52px);
            overflow-y: auto;
            scrollbar-width: thin;
            background: var(--bg-panel);
            border-right: 1px solid var(--border-subtle);
            display: flex;
            flex-direction: column;
            flex-shrink: 0;
        }}
        .studio-editor-panel::-webkit-scrollbar {{
            width: 4px;
        }}
        .studio-editor-panel::-webkit-scrollbar-thumb {{
            background: rgba(255, 255, 255, 0.12);
            border-radius: 4px;
        }}
        .studio-editor-panel::-webkit-scrollbar-track {{
            background: transparent;
        }}
        .editor-header {{
            min-height: 44px;
            height: auto;
            background: var(--bg-surface);
            border-bottom: 1px solid var(--border-subtle);
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 8px 14px;
            flex-shrink: 0;
            gap: 6px;
            flex-wrap: wrap;
        }}
        .editor-header-title {{
            font-size: 0.8rem;
            font-weight: 700;
            color: var(--text-main);
            display: flex;
            align-items: center;
            gap: 6px;
        }}
        .editor-scroll-area {{
            flex: 1;
            overflow-y: auto;
            scrollbar-width: thin;
            padding: 14px 16px 80px;
        }}
        .editor-scroll-area::-webkit-scrollbar {{ width: 4px; }}
        .editor-scroll-area::-webkit-scrollbar-thumb {{ background: rgba(255, 255, 255, 0.12); border-radius: 4px; }}
        .editor-scroll-area::-webkit-scrollbar-track {{ background: transparent; }}

        /* Form Controls */
        .form-group {{
            margin-bottom: 13px;
        }}
        .form-label {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            font-size: 0.75rem;
            font-weight: 600;
            color: var(--text-secondary);
            margin-bottom: 4px;
        }}
        .form-input, .form-textarea, .form-select {{
            width: 100%;
            background: var(--bg-input);
            border: 1px solid var(--border-subtle);
            color: var(--text-main);
            padding: 7px 10px;
            border-radius: var(--radius-sm);
            font-family: inherit;
            font-size: 0.82rem;
            outline: none;
            transition: all 0.15s ease;
        }}
        .form-input:focus, .form-textarea:focus, .form-select:focus {{
            border-color: var(--border-focus);
            box-shadow: 0 0 0 1px var(--border-focus);
            background: #090f18;
        }}
        .form-textarea {{
            resize: vertical;
            line-height: 1.55;
            min-height: 85px;
        }}

        /* Subject Length Counter */
        .subj-counter-wrap {{
            display: flex;
            align-items: center;
            gap: 6px;
            font-size: 0.68rem;
            font-weight: 600;
        }}
        .subj-counter-badge {{
            padding: 1px 5px;
            border-radius: 3px;
            background: var(--bg-surface);
            color: var(--text-secondary);
        }}
        .subj-counter-badge.safe {{ color: #34d399; }}
        .subj-counter-badge.warn {{ color: #fbbf24; }}
        .subj-counter-badge.danger {{ color: #f87171; }}

        /* Formatting Toolbar */
        .editor-toolbar {{
            display: flex;
            align-items: center;
            gap: 3px;
            background: var(--bg-surface);
            border: 1px solid var(--border-subtle);
            border-bottom: none;
            border-radius: var(--radius-sm) var(--radius-sm) 0 0;
            padding: 4px 6px;
        }}
        .tool-btn {{
            background: transparent;
            border: none;
            color: var(--text-secondary);
            padding: 3px 6px;
            border-radius: var(--radius-xs);
            font-size: 0.72rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.1s ease;
        }}
        .tool-btn:hover {{
            background: var(--bg-elevated);
            color: #ffffff;
        }}

        /* Greeting Switcher Pills */
        .greeting-pills {{
            display: flex;
            gap: 4px;
            margin-top: 4px;
            flex-wrap: wrap;
        }}
        .greeting-pill-btn {{
            background: var(--bg-surface);
            border: 1px solid var(--border-subtle);
            color: var(--text-dim);
            padding: 2px 7px;
            border-radius: var(--radius-xs);
            font-size: 0.68rem;
            cursor: pointer;
        }}
        .greeting-pill-btn:hover {{
            color: var(--text-main);
            border-color: var(--primary);
        }}

        /* Quick Chips Area */
        .quick-chips-bar {{
            display: flex;
            flex-wrap: wrap;
            gap: 4px;
            margin-top: 6px;
        }}
        .quick-chip-btn {{
            background: var(--primary-subtle);
            border: 1px solid rgba(37, 99, 235, 0.35);
            color: #93c5fd;
            padding: 3px 8px;
            border-radius: var(--radius-xs);
            font-size: 0.69rem;
            font-family: 'JetBrains Mono', monospace;
            cursor: pointer;
            transition: all 0.12s ease;
        }}
        .quick-chip-btn:hover {{
            background: var(--primary);
            color: #ffffff;
            border-color: var(--primary);
            transform: translateY(-1px);
        }}

        /* Variable Drawer */
        .drawer-box {{
            background: var(--bg-surface);
            border: 1px solid var(--border-subtle);
            border-radius: var(--radius-md);
            padding: 10px;
            margin-top: 8px;
        }}
        .drawer-search-inp {{
            width: 100%;
            background: var(--bg-input);
            border: 1px solid var(--border-subtle);
            border-radius: var(--radius-xs);
            padding: 6px 9px;
            font-size: 0.74rem;
            color: var(--text-main);
            outline: none;
            margin-bottom: 7px;
        }}
        .drawer-pills {{
            display: flex;
            flex-wrap: wrap;
            gap: 4px;
            margin-bottom: 7px;
        }}
        .drawer-cat-pill {{
            background: var(--bg-elevated);
            border: 1px solid var(--border-subtle);
            color: var(--text-secondary);
            font-size: 0.68rem;
            padding: 2px 7px;
            border-radius: var(--radius-xs);
            cursor: pointer;
        }}
        .drawer-cat-pill.active, .drawer-cat-pill:hover {{
            background: var(--primary);
            color: #ffffff;
            border-color: var(--primary);
        }}
        .drawer-chips-grid {{
            max-height: 160px;
            overflow-y: auto;
            display: flex;
            flex-wrap: wrap;
            gap: 4px;
        }}
        .drawer-chip {{
            background: var(--bg-elevated);
            border: 1px solid var(--border-subtle);
            border-radius: var(--radius-xs);
            padding: 2px 6px;
            font-size: 0.7rem;
            color: var(--text-main);
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 4px;
            transition: all 0.12s ease;
        }}
        .drawer-chip:hover {{
            background: rgba(37, 99, 235, 0.2);
            border-color: var(--primary);
            color: #60a5fa;
        }}
        .drawer-chip code {{
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.65rem;
            color: #93c5fd;
        }}

        /* Modular Content Blocks (Roadmap, Notice, Login Box) */
        .modular-block-card {{
            background: rgba(0, 0, 0, 0.25);
            border: 1px solid var(--border-subtle);
            border-radius: var(--radius-md);
            padding: 10px 12px;
            margin-top: 10px;
        }}
        .checkbox-label {{
            display: flex;
            align-items: center;
            gap: 7px;
            font-size: 0.78rem;
            font-weight: 600;
            color: var(--text-main);
            cursor: pointer;
        }}

        /* Tag Lint Warning Box */
        .lint-alert-box {{
            display: none;
            background: rgba(239, 68, 68, 0.15);
            border: 1px solid rgba(239, 68, 68, 0.4);
            border-radius: var(--radius-sm);
            padding: 8px 10px;
            margin-top: 8px;
            font-size: 0.72rem;
            color: #fca5a5;
        }}

        /* Scenario Category Pills & Stepper */
        .scen-category-pills {{
            display: flex;
            flex-wrap: wrap;
            gap: 4px;
            margin: 6px 0 8px;
        }}
        .scen-cat-pill {{
            background: var(--bg-surface);
            border: 1px solid var(--border-subtle);
            color: var(--text-secondary);
            font-size: 0.65rem;
            font-weight: 600;
            padding: 2px 7px;
            border-radius: var(--radius-xs);
            cursor: pointer;
            transition: all 0.12s ease;
        }}
        .scen-cat-pill:hover, .scen-cat-pill.active {{
            background: var(--primary);
            color: #ffffff;
            border-color: var(--primary);
        }}

        /* Brand Presets Bar */
        .brand-presets-bar {{
            display: flex;
            gap: 6px;
            overflow-x: auto;
            scrollbar-width: none;
            -ms-overflow-style: none;
            padding: 3px 2px;
            scroll-behavior: smooth;
        }}
        .brand-presets-bar::-webkit-scrollbar {{
            display: none;
        }}
        .theme-preset-btn {{
            background: var(--bg-surface);
            border: 1px solid var(--border-subtle);
            border-radius: var(--radius-xs);
            color: var(--text-main);
            font-size: 0.67rem;
            font-weight: 600;
            padding: 4px 8px;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 5px;
            flex-shrink: 0;
            white-space: nowrap;
            transition: all 0.15s ease;
        }}
        .theme-preset-btn .dot {{
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background-color: var(--p-color);
            flex-shrink: 0;
        }}
        .theme-preset-btn:hover {{
            border-color: var(--p-color);
            background: var(--bg-elevated);
            transform: translateY(-1px);
        }}
        .theme-preset-btn.active {{
            border-color: var(--p-color);
            background: rgba(37, 99, 235, 0.16);
            box-shadow: 0 0 0 1px var(--p-color);
        }}

        /* Interactive Test Data Customizer */
        .sample-customizer-card {{
            background: #0b111e;
            border: 1px solid #1e293b;
            border-radius: var(--radius-sm);
            padding: 10px 14px;
            margin: 10px 14px 0;
            box-shadow: 0 4px 12px rgba(0,0,0,0.4);
        }}

        /* Template Readiness Meter */
        .readiness-meter {{
            font-size: 0.72rem;
            font-weight: 700;
            padding: 3px 8px;
            border-radius: var(--radius-full);
            background: rgba(16, 185, 129, 0.12);
            color: #34d399;
            border: 1px solid rgba(16, 185, 129, 0.3);
            display: inline-flex;
            align-items: center;
            gap: 4px;
            cursor: pointer;
            user-select: none;
        }}
        .readiness-meter.warning {{
            background: rgba(245, 158, 11, 0.12);
            color: #fbbf24;
            border-color: rgba(245, 158, 11, 0.3);
        }}

        /* Autosave Badge */
        .autosave-badge {{
            font-size: 0.68rem;
            color: #34d399;
            display: inline-flex;
            align-items: center;
            gap: 4px;
            padding: 3px 8px;
            background: rgba(16, 185, 129, 0.1);
            border: 1px solid rgba(16, 185, 129, 0.25);
            border-radius: var(--radius-full);
            font-weight: 600;
        }}
        .autosave-dot {{
            width: 6px;
            height: 6px;
            border-radius: 50%;
            background-color: #34d399;
            box-shadow: 0 0 6px #34d399;
        }}

        /* Mode Pill Toggle (Visual Form vs Code) */
        .mode-pill-toggle {{
            display: flex;
            background: var(--bg-input);
            border: 1px solid var(--border-subtle);
            border-radius: var(--radius-xs);
            padding: 2px;
            gap: 2px;
        }}
        .mode-pill-btn {{
            background: transparent;
            border: none;
            color: var(--text-secondary);
            font-size: 0.65rem;
            font-weight: 600;
            padding: 2px 6px;
            border-radius: 2px;
            cursor: pointer;
            transition: all 0.12s;
        }}
        .mode-pill-btn.active {{
            background: var(--primary);
            color: #ffffff;
        }}

        /* ═══════════════════════════════════════════════════════
           GLOBAL SCROLLERS & HORIZONTAL SCROLL CHEVRONS
        ═══════════════════════════════════════════════════════ */
        *::-webkit-scrollbar {{
            width: 6px;
            height: 6px;
        }}
        *::-webkit-scrollbar-track {{
            background: rgba(0, 0, 0, 0.25);
        }}
        *::-webkit-scrollbar-thumb {{
            background: rgba(255, 255, 255, 0.2);
            border-radius: 4px;
        }}
        *::-webkit-scrollbar-thumb:hover {{
            background: var(--primary);
        }}

        .horizontal-scroll-wrap {{
            display: flex;
            align-items: center;
            gap: 4px;
            position: relative;
            max-width: 100%;
        }}
        .scroll-arrow-btn {{
            width: 22px;
            height: 24px;
            background: var(--bg-surface);
            border: 1px solid var(--border-subtle);
            border-radius: var(--radius-xs);
            color: var(--text-secondary);
            font-size: 0.62rem;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            flex-shrink: 0;
            transition: all 0.12s ease;
            user-select: none;
        }}
        .scroll-arrow-btn:hover {{
            background: var(--primary);
            color: #ffffff;
            border-color: var(--primary);
        }}

        /* ═══════════════════════════════════════════════════════
           HAMBURGER MENU & MOBILE FLYOUT NAVIGATION DRAWER
        ═══════════════════════════════════════════════════════ */
        .hamburger-btn {{
            display: none;
            background: var(--bg-surface);
            border: 1px solid var(--border-subtle);
            border-radius: var(--radius-sm);
            padding: 6px 8px;
            cursor: pointer;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            gap: 4px;
            width: 32px;
            height: 32px;
            transition: all 0.18s ease;
            flex-shrink: 0;
        }}
        .hamburger-btn:hover {{
            background: var(--bg-elevated);
            border-color: var(--primary);
        }}
        .hamburger-line {{
            display: block;
            width: 16px;
            height: 2px;
            background: var(--text-main);
            border-radius: 1px;
            transition: all 0.2s ease;
        }}
        .hamburger-btn.active .hamburger-line:nth-child(1) {{
            transform: translateY(6px) rotate(45deg);
        }}
        .hamburger-btn.active .hamburger-line:nth-child(2) {{
            opacity: 0;
        }}
        .hamburger-btn.active .hamburger-line:nth-child(3) {{
            transform: translateY(-6px) rotate(-45deg);
        }}

        .drawer-backdrop {{
            display: none;
            position: fixed;
            inset: 0;
            background: rgba(0, 0, 0, 0.72);
            backdrop-filter: blur(4px);
            z-index: 99998;
            opacity: 0;
            transition: opacity 0.25s ease;
        }}
        .drawer-backdrop.show {{
            display: block;
            opacity: 1;
        }}
        .mobile-nav-drawer {{
            position: fixed;
            top: 0;
            left: -320px;
            width: 300px;
            height: 100vh;
            background: #080d16;
            border-right: 1px solid var(--border-subtle);
            box-shadow: 10px 0 30px rgba(0,0,0,0.85);
            z-index: 99999;
            display: flex;
            flex-direction: column;
            transition: left 0.28s cubic-bezier(0.16, 1, 0.3, 1);
            overflow-y: auto;
        }}
        .mobile-nav-drawer.open {{
            left: 0;
        }}
        .mobile-drawer-header {{
            padding: 14px 16px;
            border-bottom: 1px solid var(--border-subtle);
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: var(--bg-surface);
        }}
        .mobile-drawer-section {{
            padding: 12px 16px;
            border-bottom: 1px solid var(--border-subtle);
        }}
        .mobile-drawer-title {{
            font-size: 0.68rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            color: var(--text-dim);
            margin-bottom: 8px;
            display: flex;
            align-items: center;
            gap: 6px;
        }}
        .mobile-drawer-nav-list {{
            display: flex;
            flex-direction: column;
            gap: 4px;
        }}
        .mobile-drawer-link {{
            padding: 8px 10px;
            border-radius: var(--radius-sm);
            background: var(--bg-input);
            border: 1px solid var(--border-subtle);
            color: var(--text-main);
            font-size: 0.78rem;
            font-weight: 600;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 8px;
            text-align: left;
            transition: all 0.12s ease;
        }}
        .mobile-drawer-link:hover, .mobile-drawer-link.active {{
            background: var(--primary);
            color: #ffffff;
            border-color: var(--primary);
        }}

        /* ═══════════════════════════════════════════════════════
           SCENARIO PAGINATOR & LIBRARY PAGINATOR
        ═══════════════════════════════════════════════════════ */
        .scenario-paginator {{
            background: var(--bg-surface);
            border: 1px solid var(--border-subtle);
            border-radius: var(--radius-sm);
            padding: 7px 10px;
            margin-bottom: 8px;
            display: flex;
            flex-direction: column;
            gap: 6px;
        }}
        .paginator-top-row {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            font-size: 0.72rem;
            gap: 6px;
        }}
        .paginator-info {{
            font-weight: 700;
            color: #38bdf8;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            display: flex;
            align-items: center;
            gap: 4px;
        }}
        .paginator-controls {{
            display: flex;
            align-items: center;
            gap: 3px;
            flex-shrink: 0;
        }}
        .paginator-strip-wrap {{
            display: flex;
            align-items: center;
            gap: 3px;
            position: relative;
        }}
        .paginator-strip {{
            display: flex;
            align-items: center;
            gap: 3px;
            overflow-x: auto;
            padding-bottom: 2px;
            scrollbar-width: thin;
        }}
        .paginator-strip::-webkit-scrollbar {{
            height: 4px;
        }}
        .page-num-pill {{
            width: 22px;
            height: 22px;
            border-radius: 4px;
            background: var(--bg-input);
            border: 1px solid var(--border-subtle);
            color: var(--text-dim);
            font-size: 0.65rem;
            font-weight: 700;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            flex-shrink: 0;
            transition: all 0.12s ease;
        }}
        .page-num-pill:hover {{
            background: var(--bg-elevated);
            color: var(--text-main);
            border-color: var(--border-strong);
        }}
        .page-num-pill.active {{
            background: var(--primary);
            color: #ffffff;
            border-color: var(--primary);
            box-shadow: 0 0 8px rgba(37, 99, 235, 0.4);
        }}

        /* ═══════════════════════════════════════════════════════
           COLLAPSIBLE ACCORDION SECTION CARDS
        ═══════════════════════════════════════════════════════ */
        .editor-section-card {{
            background: var(--bg-surface);
            border: 1px solid var(--border-subtle);
            border-radius: var(--radius-sm);
            margin-bottom: 8px;
            overflow: hidden;
            transition: border-color 0.15s ease;
        }}
        .editor-section-card:hover {{
            border-color: rgba(255, 255, 255, 0.14);
        }}
        .editor-section-header {{
            padding: 8px 12px;
            background: rgba(255, 255, 255, 0.02);
            display: flex;
            align-items: center;
            justify-content: space-between;
            cursor: pointer;
            user-select: none;
            border-bottom: 1px solid transparent;
            transition: background 0.15s ease;
        }}
        .editor-section-card:not(.is-collapsed) .editor-section-header {{
            border-bottom-color: var(--border-subtle);
            background: rgba(37, 99, 235, 0.04);
        }}
        .editor-section-title {{
            display: flex;
            align-items: center;
            gap: 6px;
            font-size: 0.74rem;
            font-weight: 700;
            color: var(--text-main);
        }}
        .editor-section-badge {{
            font-size: 0.62rem;
            font-weight: 600;
            padding: 1px 6px;
            border-radius: 4px;
            background: rgba(56, 189, 248, 0.12);
            color: #38bdf8;
            border: 1px solid rgba(56, 189, 248, 0.25);
        }}
        .section-toggle-btn {{
            width: 18px;
            height: 18px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.65rem;
            color: var(--text-dim);
            transition: transform 0.2s ease;
        }}
        .editor-section-card.is-collapsed .section-toggle-btn {{
            transform: rotate(-90deg);
        }}
        .editor-section-card.is-collapsed .editor-section-body {{
            display: none !important;
        }}
        .editor-section-body {{
            padding: 10px 12px;
        }}
        .section-helper-text {{
            font-size: 0.67rem;
            color: var(--text-dim);
            margin-bottom: 8px;
            line-height: 1.4;
        }}

        /* Designer Styler Accordion */
        .designer-styler-accordion {{
            background: var(--bg-surface);
            border: 1px solid var(--border-subtle);
            border-radius: var(--radius-sm);
            padding: 8px 10px;
            margin-bottom: 10px;
        }}
        .designer-styler-header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            cursor: pointer;
            user-select: none;
        }}

        /* Dual Viewport Canvas (Desktop + Mobile Side-by-Side) */
        .dual-preview-container {{
            display: flex;
            align-items: flex-start;
            justify-content: center;
            gap: 24px;
            width: 100%;
            overflow-x: auto;
            padding: 10px 0;
        }}

        /* Guided Tutorial Tour Modal */
        .tutorial-overlay {{
            position: fixed;
            inset: 0;
            background: rgba(0, 0, 0, 0.78);
            backdrop-filter: blur(5px);
            z-index: 100000;
            display: none;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }}
        .tutorial-overlay.show {{
            display: flex;
        }}
        .tutorial-card {{
            background: var(--bg-panel);
            border: 1px solid rgba(56, 189, 248, 0.4);
            border-radius: var(--radius-lg);
            width: 100%;
            max-width: 580px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.8), 0 0 30px rgba(37,99,235,0.25);
            overflow: hidden;
            animation: modalPop 0.2s cubic-bezier(0.16, 1, 0.3, 1);
        }}
        .tutorial-header {{
            background: linear-gradient(135deg, rgba(37,99,235,0.25), rgba(16,185,129,0.2));
            border-bottom: 1px solid var(--border-subtle);
            padding: 16px 20px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}
        .tutorial-body {{
            padding: 20px;
        }}
        .tutorial-footer {{
            padding: 14px 20px;
            background: var(--bg-surface);
            border-top: 1px solid var(--border-subtle);
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}

        /* Floating Bottom Action Dock */
        .floating-action-dock {{
            position: absolute;
            bottom: 16px;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(13, 19, 31, 0.88);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.15);
            border-radius: var(--radius-full);
            padding: 5px 12px;
            display: flex;
            align-items: center;
            gap: 6px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.6);
            z-index: 1000;
            transition: all 0.2s ease;
        }}

        /* Zen Mode (Full-Screen Canvas) */
        body.zen-mode .top-nav,
        body.zen-mode .studio-editor-panel {{
            display: none !important;
        }}
        body.zen-mode .stage-toolbar {{
            padding: 0 24px;
        }}

        /* ───── Right Side Live Stage ───── */
        .studio-stage {{
            flex: 1;
            display: flex;
            flex-direction: column;
            background: #04070c;
            overflow: hidden;
            position: relative;
        }}
        .stage-toolbar {{
            min-height: 48px;
            height: auto;
            background: var(--bg-panel);
            border-bottom: 1px solid var(--border-subtle);
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 8px 14px;
            flex-shrink: 0;
            gap: 10px;
            flex-wrap: wrap;
        }}
        .stage-controls-left {{
            display: flex;
            align-items: center;
            gap: 6px;
            flex-wrap: wrap;
        }}
        .utility-btn-group {{
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
            align-items: center;
        }}
        .viewport-segmented {{
            display: flex;
            background: var(--bg-input);
            border: 1px solid var(--border-subtle);
            border-radius: var(--radius-sm);
            padding: 2px;
            gap: 2px;
        }}
        .viewport-btn {{
            background: transparent;
            border: none;
            color: var(--text-secondary);
            padding: 4px 8px;
            border-radius: var(--radius-xs);
            font-size: 0.72rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.12s ease;
        }}
        .viewport-btn.active {{
            background: var(--bg-surface);
            color: #ffffff;
            box-shadow: var(--shadow-sm);
        }}

        .toggle-chip-btn {{
            background: var(--bg-input);
            border: 1px solid var(--border-subtle);
            border-radius: var(--radius-sm);
            padding: 4px 8px;
            font-size: 0.72rem;
            font-weight: 600;
            color: var(--text-secondary);
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 4px;
        }}
        .toggle-chip-btn.active {{
            border-color: var(--primary);
            color: #ffffff;
            background: var(--primary-subtle);
        }}

        /* Action Buttons */
        .btn {{
            padding: 5px 11px;
            border-radius: var(--radius-sm);
            font-family: inherit;
            font-size: 0.76rem;
            font-weight: 600;
            cursor: pointer;
            border: 1px solid transparent;
            display: inline-flex;
            align-items: center;
            gap: 5px;
            transition: all 0.15s ease;
            white-space: nowrap;
        }}
        .btn-outline {{
            background: transparent;
            border-color: var(--border-subtle);
            color: var(--text-main);
        }}
        .btn-outline:hover {{
            background: var(--bg-surface);
            border-color: var(--border-strong);
        }}
        .btn-primary {{
            background: var(--primary);
            color: #ffffff;
        }}
        .btn-primary:hover {{
            background: var(--primary-hover);
        }}
        .btn-success {{
            background: var(--success);
            color: #ffffff;
        }}
        .btn-success:hover {{
            background: var(--success-hover);
        }}

        /* Canvas Stage */
        .stage-canvas {{
            flex: 1;
            overflow: auto;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 16px;
            gap: 14px;
        }}

        /* Lockscreen / Inbox Notification Preview Widget */
        .lockscreen-card {{
            display: none;
            width: 100%;
            max-width: 600px;
            background: rgba(30, 41, 59, 0.75);
            backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.12);
            border-radius: 14px;
            padding: 10px 14px;
            box-shadow: var(--shadow-md);
            margin-bottom: 2px;
        }}
        .lockscreen-card.show {{
            display: block;
        }}
        .ls-header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 4px;
            font-size: 0.68rem;
            color: #94a3b8;
        }}
        .ls-title {{
            font-size: 0.8rem;
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 2px;
        }}
        .ls-body {{
            font-size: 0.74rem;
            color: #cbd5e1;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }}

        /* WhatsApp / SMS Companion Box */
        .omni-companion-card {{
            display: none;
            width: 100%;
            max-width: 600px;
            background: #0f2e24;
            border: 1px solid #10b981;
            border-radius: 10px;
            padding: 10px 14px;
            box-shadow: var(--shadow-md);
        }}
        .omni-companion-card.show {{
            display: block;
        }}
        .omni-header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            font-size: 0.72rem;
            font-weight: 700;
            color: #34d399;
            margin-bottom: 4px;
        }}
        .omni-text {{
            font-size: 0.76rem;
            color: #d1fae5;
            font-family: 'JetBrains Mono', monospace;
            line-height: 1.45;
        }}

        /* Preview Containers */
        .preview-wrapper {{
            width: 100%;
            max-width: 640px;
            transition: all 0.25s ease;
        }}
        .preview-wrapper.tablet-mode {{
            max-width: 480px;
        }}
        .preview-wrapper.mobile-mode {{
            max-width: 375px;
            background: #1e293b;
            padding: 14px 10px 22px;
            border-radius: 36px;
            box-shadow: 0 24px 48px -12px rgba(0, 0, 0, 0.8), 0 0 0 1px rgba(255, 255, 255, 0.1);
        }}
        .mobile-notch {{
            display: none;
            width: 90px;
            height: 12px;
            background: #080d15;
            border-radius: 6px;
            margin: 0 auto 10px;
        }}
        .preview-wrapper.mobile-mode .mobile-notch {{
            display: block;
        }}
        .live-preview-iframe {{
            width: 100%;
            height: 780px;
            border: none;
            background: #ffffff;
            border-radius: var(--radius-md);
            box-shadow: var(--shadow-md);
            transition: filter 0.2s ease;
        }}
        .live-preview-iframe.dark-sim {{
            filter: invert(0.92) hue-rotate(180deg);
        }}
        .preview-wrapper.mobile-mode .live-preview-iframe {{
            height: 600px;
            border-radius: 20px;
        }}

        /* ═══════════════════════════════════════════════════════
           VIEW 2: TEMPLATE LIBRARY
        ═══════════════════════════════════════════════════════ */
        #view-archive {{
            flex-direction: row;
        }}
        .archive-sidebar {{
            width: 340px;
            background: var(--bg-panel);
            border-right: 1px solid var(--border-subtle);
            display: flex;
            flex-direction: column;
            flex-shrink: 0;
        }}
        .archive-search-box {{
            padding: 12px 14px;
            border-bottom: 1px solid var(--border-subtle);
        }}
        .archive-list {{
            flex: 1;
            overflow-y: auto;
            padding: 8px;
        }}
        .archive-card {{
            background: var(--bg-surface);
            border: 1px solid var(--border-subtle);
            border-radius: var(--radius-sm);
            padding: 9px 12px;
            margin-bottom: 5px;
            cursor: pointer;
            transition: all 0.15s ease;
        }}
        .archive-card:hover {{
            border-color: var(--primary);
            transform: translateY(-1px);
        }}
        .archive-card.active {{
            border-color: var(--primary);
            background: rgba(37, 99, 235, 0.15);
        }}
        .archive-card-name {{
            font-size: 0.77rem;
            font-weight: 700;
            color: var(--text-main);
            margin-bottom: 2px;
        }}
        .archive-card-sub {{
            font-size: 0.69rem;
            color: var(--text-dim);
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }}

        /* ═══════════════════════════════════════════════════════
           VIEW 3: BRAND SHELL & SETTINGS
        ═══════════════════════════════════════════════════════ */
        #view-shell {{
            flex-direction: row;
        }}
        .shell-config-panel {{
            width: 440px;
            background: var(--bg-panel);
            border-right: 1px solid var(--border-subtle);
            display: flex;
            flex-direction: column;
            flex-shrink: 0;
            overflow-y: auto;
            padding: 16px;
            gap: 14px;
        }}
        .shell-group-card {{
            background: var(--bg-surface);
            border: 1px solid var(--border-subtle);
            border-radius: var(--radius-md);
            padding: 14px;
        }}
        .shell-group-header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 12px;
            padding-bottom: 8px;
            border-bottom: 1px solid var(--border-subtle);
        }}
        .shell-group-title {{
            font-size: 0.8rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            color: var(--text-primary);
            display: flex;
            align-items: center;
            gap: 6px;
        }}
        .swatch-group {{
            display: flex;
            gap: 6px;
            flex-wrap: wrap;
            margin-top: 6px;
        }}
        .swatch-btn {{
            width: 24px;
            height: 24px;
            border-radius: var(--radius-xs);
            cursor: pointer;
            border: 2px solid transparent;
            transition: transform 0.15s ease, border-color 0.15s ease;
        }}
        .swatch-btn:hover {{ transform: scale(1.15); }}
        .swatch-btn.active {{ border-color: #ffffff; }}
        .contrast-meter-badge {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 4px 10px;
            border-radius: var(--radius-full);
            font-size: 0.72rem;
            font-weight: 700;
            margin-top: 8px;
            border: 1px solid var(--border-subtle);
            background: var(--bg-surface-elevated);
        }}
        .contrast-meter-badge.pass {{
            color: #10b981;
            border-color: rgba(16, 185, 129, 0.35);
            background: rgba(16, 185, 129, 0.1);
        }}
        .contrast-meter-badge.warn {{
            color: #f59e0b;
            border-color: rgba(245, 158, 11, 0.35);
            background: rgba(245, 158, 11, 0.1);
        }}
        .contrast-meter-badge.fail {{
            color: #ef4444;
            border-color: rgba(239, 68, 68, 0.35);
            background: rgba(239, 68, 68, 0.1);
        }}

        /* ═══════════════════════════════════════════════════════
           VIEW 4: AI GENERATOR
        ═══════════════════════════════════════════════════════ */
        #view-ai {{
            flex-direction: row;
        }}
        .ai-sidebar {{
            width: 440px;
            background: var(--bg-panel);
            border-right: 1px solid var(--border-subtle);
            display: flex;
            flex-direction: column;
            flex-shrink: 0;
            overflow-y: auto;
            padding: 16px;
            gap: 14px;
        }}
        .ai-funnel-pills {{
            display: flex;
            flex-direction: column;
            gap: 6px;
            margin-bottom: 4px;
        }}
        .ai-funnel-pill {{
            display: flex;
            align-items: center;
            gap: 8px;
            padding: 7px 10px;
            border-radius: var(--radius-sm);
            background: var(--bg-surface);
            border: 1px solid var(--border-subtle);
            font-size: 0.75rem;
            cursor: pointer;
            color: var(--text-secondary);
            transition: all 0.15s ease;
            text-align: left;
        }}
        .ai-funnel-pill:hover {{
            color: var(--text-primary);
            border-color: var(--border-hover);
            background: var(--bg-surface-elevated);
        }}
        .ai-funnel-pill.active {{
            background: var(--primary-subtle);
            border-color: var(--primary);
            color: #ffffff;
            font-weight: 600;
        }}
        .ai-funnel-num {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 18px;
            height: 18px;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.1);
            font-size: 0.68rem;
            font-weight: 700;
            flex-shrink: 0;
        }}
        .ai-funnel-pill.active .ai-funnel-num {{
            background: var(--primary);
            color: #ffffff;
        }}
        .ai-chips-wrap {{
            display: flex;
            flex-wrap: wrap;
            gap: 5px;
            margin-top: 4px;
        }}
        .ai-preset-chip {{
            padding: 3px 8px;
            border-radius: var(--radius-full);
            background: var(--bg-surface);
            border: 1px solid var(--border-subtle);
            font-size: 0.68rem;
            color: var(--text-secondary);
            cursor: pointer;
            transition: all 0.15s ease;
        }}
        .ai-preset-chip:hover {{
            border-color: var(--primary);
            color: var(--primary);
            background: var(--primary-subtle);
        }}

        /* ═══════════════════════════════════════════════════════
           VIEW 5: HUB OVERVIEW
        ═══════════════════════════════════════════════════════ */
        #view-home {{
            flex-direction: column;
            overflow-y: auto;
            padding: 32px 16px 80px;
            align-items: center;
        }}
        .home-container {{
            width: 100%;
            max-width: 1080px;
            display: flex;
            flex-direction: column;
            gap: 24px;
        }}
        .home-hero {{
            text-align: center;
            margin-bottom: 8px;
        }}
        .home-hero-badge {{
            display: inline-block;
            font-size: 0.72rem;
            font-weight: 700;
            letter-spacing: 0.5px;
            background: var(--primary-subtle);
            color: #60a5fa;
            border: 1px solid rgba(37, 99, 235, 0.3);
            padding: 3px 10px;
            border-radius: var(--radius-full);
            margin-bottom: 10px;
        }}
        .home-hero h1 {{
            font-size: 1.7rem;
            font-weight: 800;
            letter-spacing: -0.5px;
            margin-bottom: 8px;
        }}
        .home-hero p {{
            font-size: 0.85rem;
            color: var(--text-secondary);
            max-width: 620px;
            margin: 0 auto;
            line-height: 1.5;
        }}
        .hub-metrics-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 12px;
        }}
        .hub-metric-card {{
            background: var(--bg-panel);
            border: 1px solid var(--border-subtle);
            border-radius: var(--radius-md);
            padding: 16px;
            display: flex;
            flex-direction: column;
            gap: 6px;
            transition: border-color 0.15s ease;
        }}
        .hub-metric-card:hover {{
            border-color: var(--primary);
        }}
        .hub-metric-num {{
            font-size: 1.8rem;
            font-weight: 800;
            color: var(--text-primary);
            letter-spacing: -0.5px;
            display: flex;
            align-items: baseline;
            gap: 4px;
        }}
        .hub-metric-num span {{
            font-size: 0.85rem;
            color: var(--primary);
            font-weight: 600;
        }}
        .hub-metric-label {{
            font-size: 0.76rem;
            font-weight: 600;
            color: var(--text-primary);
        }}
        .hub-metric-sub {{
            font-size: 0.7rem;
            color: var(--text-dim);
            line-height: 1.4;
        }}
        .hub-section-card {{
            background: var(--bg-panel);
            border: 1px solid var(--border-subtle);
            border-radius: var(--radius-lg);
            padding: 20px;
        }}
        .hub-section-header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 14px;
            padding-bottom: 10px;
            border-bottom: 1px solid var(--border-subtle);
        }}
        .hub-section-title {{
            font-size: 0.92rem;
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .hub-launchpad-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(310px, 1fr));
            gap: 10px;
        }}
        .hub-launch-btn {{
            background: var(--bg-surface);
            border: 1px solid var(--border-subtle);
            border-radius: var(--radius-sm);
            padding: 12px 14px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 12px;
            cursor: pointer;
            transition: all 0.15s ease;
            text-align: left;
        }}
        .hub-launch-btn:hover {{
            border-color: var(--primary);
            background: var(--bg-surface-elevated);
            transform: translateY(-1px);
        }}
        .hub-launch-tag {{
            font-size: 0.68rem;
            font-weight: 700;
            padding: 2px 6px;
            border-radius: 4px;
            background: var(--primary-subtle);
            color: #60a5fa;
            white-space: nowrap;
        }}
        .hub-launch-title {{
            font-size: 0.78rem;
            font-weight: 600;
            color: var(--text-primary);
            line-height: 1.3;
        }}
        .hub-launch-sub {{
            font-size: 0.68rem;
            color: var(--text-secondary);
        }}
        .hub-crm-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 0.74rem;
        }}
        .hub-crm-table th {{
            background: var(--bg-surface);
            padding: 8px 10px;
            text-align: left;
            font-weight: 700;
            color: var(--text-secondary);
            border-bottom: 1px solid var(--border-subtle);
            text-transform: uppercase;
            font-size: 0.66rem;
            letter-spacing: 0.5px;
        }}
        .hub-crm-table td {{
            padding: 8px 10px;
            border-bottom: 1px solid var(--border-subtle);
            color: var(--text-primary);
            vertical-align: middle;
        }}
        .hub-crm-table tr:hover td {{
            background: rgba(255, 255, 255, 0.02);
        }}
        .hub-copy-pill {{
            font-family: monospace;
            background: var(--bg-surface);
            border: 1px solid var(--border-subtle);
            padding: 2px 6px;
            border-radius: 4px;
            font-size: 0.7rem;
            color: #93c5fd;
            cursor: pointer;
            transition: border-color 0.1s ease;
            display: inline-block;
        }}
        .hub-copy-pill:hover {{
            border-color: var(--primary);
            background: var(--primary-subtle);
        }}
        .home-cards-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 12px;
        }}
        .home-card {{
            background: var(--bg-panel);
            border: 1px solid var(--border-subtle);
            border-radius: var(--radius-lg);
            padding: 16px;
            cursor: pointer;
            transition: all 0.2s ease;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }}
        .home-card:hover {{
            border-color: var(--primary);
            transform: translateY(-2px);
            box-shadow: var(--shadow-float);
        }}
        .home-card-title {{
            font-size: 0.92rem;
            font-weight: 700;
            margin: 6px 0 4px;
        }}
        .home-card-desc {{
            font-size: 0.75rem;
            color: var(--text-secondary);
            line-height: 1.45;
            margin-bottom: 12px;
        }}

        /* ───── Modals (Code, Command Palette) ───── */
        .modal-overlay {{
            position: fixed;
            inset: 0;
            background: rgba(0, 0, 0, 0.75);
            backdrop-filter: blur(6px);
            display: none;
            align-items: center;
            justify-content: center;
            z-index: 9999;
            padding: 16px;
        }}
        .modal-overlay.show {{
            display: flex;
        }}
        .modal-box {{
            width: 100%;
            max-width: 760px;
            max-height: 85vh;
            background: var(--bg-panel);
            border: 1px solid var(--border-subtle);
            border-radius: var(--radius-lg);
            display: flex;
            flex-direction: column;
            box-shadow: var(--shadow-float);
            overflow: hidden;
        }}
        .modal-header {{
            height: 48px;
            background: var(--bg-surface);
            border-bottom: 1px solid var(--border-subtle);
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 16px;
        }}
        .modal-body {{
            flex: 1;
            overflow-y: auto;
            padding: 14px;
        }}
        .code-box {{
            background: var(--bg-input);
            border: 1px solid var(--border-subtle);
            border-radius: var(--radius-sm);
            padding: 12px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.72rem;
            color: #e2e8f0;
            white-space: pre-wrap;
            word-break: break-all;
            user-select: all;
        }}

        /* Command Palette Search Box */
        .cmd-search-input {{
            width: 100%;
            background: transparent;
            border: none;
            outline: none;
            font-size: 1rem;
            color: #ffffff;
            padding: 14px 18px;
            border-bottom: 1px solid var(--border-subtle);
        }}
        .cmd-results-list {{
            max-height: 340px;
            overflow-y: auto;
            padding: 8px;
        }}
        .cmd-item {{
            padding: 9px 12px;
            border-radius: var(--radius-sm);
            font-size: 0.78rem;
            color: var(--text-main);
            display: flex;
            align-items: center;
            justify-content: space-between;
            cursor: pointer;
            transition: all 0.1s;
        }}
        .cmd-item:hover, .cmd-item.active {{
            background: var(--primary);
            color: #ffffff;
        }}

        /* Toast Feedback */
        .toast {{
            position: fixed;
            bottom: 24px;
            right: 24px;
            background: var(--success);
            color: #ffffff;
            padding: 9px 18px;
            border-radius: var(--radius-full);
            font-size: 0.8rem;
            font-weight: 700;
            box-shadow: var(--shadow-float);
            transform: translateY(80px);
            opacity: 0;
            transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
            z-index: 10000;
        }}
        .toast.show {{
            transform: translateY(0);
            opacity: 1;
        }}

        /* ═══════════════════════════════════════════════════════
           RICH TOOLTIP & ONBOARDING HELP SYSTEM
        ═══════════════════════════════════════════════════════ */
        [data-tooltip] {{
            position: relative;
        }}
        [data-tooltip]::after {{
            content: attr(data-tooltip);
            position: absolute;
            bottom: calc(100% + 7px);
            left: 50%;
            transform: translateX(-50%) translateY(4px);
            background: rgba(15, 23, 42, 0.96);
            backdrop-filter: blur(8px);
            color: #f1f5f9;
            font-size: 0.68rem;
            font-weight: 500;
            line-height: 1.35;
            padding: 5px 9px;
            border-radius: 6px;
            border: 1px solid rgba(255, 255, 255, 0.12);
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.5);
            white-space: nowrap;
            pointer-events: none;
            opacity: 0;
            transition: opacity 0.18s ease, transform 0.18s ease;
            z-index: 10000;
        }}
        [data-tooltip]::before {{
            content: '';
            position: absolute;
            bottom: calc(100% + 2px);
            left: 50%;
            transform: translateX(-50%) translateY(4px);
            border-width: 5px 5px 0 5px;
            border-style: solid;
            border-color: rgba(15, 23, 42, 0.96) transparent transparent transparent;
            pointer-events: none;
            opacity: 0;
            transition: opacity 0.18s ease, transform 0.18s ease;
            z-index: 10000;
        }}
        [data-tooltip]:hover::after,
        [data-tooltip]:hover::before {{
            opacity: 1;
            transform: translateX(-50%) translateY(0);
        }}
        [data-tooltip-pos="bottom"]::after {{
            bottom: auto;
            top: calc(100% + 7px);
            transform: translateX(-50%) translateY(-4px);
        }}
        [data-tooltip-pos="bottom"]::before {{
            bottom: auto;
            top: calc(100% + 2px);
            border-width: 0 5px 5px 5px;
            border-color: transparent transparent rgba(15, 23, 42, 0.96) transparent;
            transform: translateX(-50%) translateY(-4px);
        }}
        [data-tooltip-pos="bottom"]:hover::after,
        [data-tooltip-pos="bottom"]:hover::before {{
            opacity: 1;
            transform: translateX(-50%) translateY(0);
        }}
        .help-icon {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 14px;
            height: 14px;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.1);
            color: var(--text-dim);
            font-size: 0.62rem;
            font-weight: 700;
            cursor: help;
            margin-left: 4px;
            transition: all 0.15s ease;
        }}
        .help-icon:hover {{
            background: var(--primary);
            color: #ffffff;
        }}

        /* ═══════════════════════════════════════════════════════
           RESPONSIVE BREAKPOINTS
        ═══════════════════════════════════════════════════════ */
        @media (max-width: 1200px) {{
            /* Consolidate secondary header tools into More Actions dropdown */
            .nav-tool-secondary {{
                display: none !important;
            }}
            .top-view-tab#tab-shell,
            .top-view-tab#tab-ai,
            .top-view-tab#tab-home {{
                display: none !important;
            }}
            .more-actions-dropdown-wrap {{
                display: block;
            }}
            .hamburger-btn {{
                display: flex;
            }}
            .campus-pills-bar {{
                max-width: 260px;
                overflow-x: auto;
            }}
            /* Preserve space for critical layout toggles (Desk, Tab, Mob) */
            .stage-controls-left {{
                flex: 1 1 auto;
            }}
            .viewport-segmented {{
                flex-shrink: 0;
            }}
        }}

        @media (max-width: 1024px) {{
            .studio-editor-panel, .shell-config-panel, .ai-sidebar {{
                width: 350px;
                flex: 0 0 350px;
            }}
            .archive-sidebar {{
                width: 280px;
            }}
            .campus-pills-bar {{
                display: none;
            }}
            .hamburger-btn {{
                display: flex;
            }}
        }}

        @media (max-width: 768px) {{
            body {{
                overflow: auto;
            }}
            .top-nav {{
                padding: 0 10px;
                gap: 8px;
            }}
            .hamburger-btn {{
                display: flex;
            }}
            .top-view-tabs {{
                display: none;
            }}
            .nav-brand-title span {{
                display: none;
            }}
            .nav-right-actions button:not(#btn-zen-mode):not(#btn-hamburger) {{
                display: none;
            }}
            #view-studio, #view-shell, #view-ai, #view-archive {{
                flex-direction: column;
            }}
            .mobile-mode-switcher {{
                display: flex;
            }}
            .studio-editor-panel, .shell-config-panel, .ai-sidebar, .archive-sidebar {{
                width: 100%;
                border-right: none;
                border-bottom: 1px solid var(--border-subtle);
            }}
            .stage-toolbar {{
                flex-wrap: wrap;
                height: auto;
                padding: 8px 10px;
                gap: 6px;
            }}
            .stage-canvas {{
                padding: 10px 4px;
            }}
            .preview-wrapper {{
                max-width: 100%;
            }}
            .live-preview-iframe {{
                height: 520px;
            }}
        }}
    </style>
</head>
<body>

    <!-- ───── Top Command Navigation ───── -->
    <header class="top-nav">
        <div class="nav-left">
            <button class="hamburger-btn" id="btn-hamburger" onclick="toggleMobileNav()" data-tooltip="Open Navigation Menu" aria-label="Toggle navigation">
                <span class="hamburger-line"></span>
                <span class="hamburger-line"></span>
                <span class="hamburger-line"></span>
            </button>
            <div class="nav-brand" onclick="switchView('studio')" title="Email Designer">
                <div class="nav-logo-badge">SA</div>
                <div class="nav-brand-title">
                    Simply Admission <span>Designer</span>
                </div>
            </div>

            <!-- Campus Preset Switcher with Horizontal Scroll Controls -->
            <div class="horizontal-scroll-wrap" style="max-width: 480px;">
                <button type="button" class="scroll-arrow-btn" onclick="scrollContainer('campus-pills-container', -120)" data-tooltip="Scroll Campuses Left">◀</button>
                <div class="campus-pills-bar" id="campus-pills-container"></div>
                <button type="button" class="scroll-arrow-btn" onclick="scrollContainer('campus-pills-container', 120)" data-tooltip="Scroll Campuses Right">▶</button>
            </div>
        </div>

        <!-- View Switcher -->
        <div class="top-view-tabs">
            <button class="top-view-tab active" id="tab-studio" onclick="switchView('studio')">
                <span>🎨</span> <span class="tab-text">Studio</span>
            </button>
            <button class="top-view-tab" id="tab-archive" onclick="switchView('archive')">
                <span>📁</span> <span class="tab-text">Library</span>
            </button>
            <button class="top-view-tab" id="tab-shell" onclick="switchView('shell')">
                <span>🏫</span> <span class="tab-text">Brand Kit</span>
            </button>
            <button class="top-view-tab" id="tab-ai" onclick="switchView('ai')">
                <span>✨</span> <span class="tab-text">AI Generator</span>
            </button>
            <button class="top-view-tab" id="tab-home" onclick="switchView('home')">
                <span>🏠</span> <span class="tab-text">Hub</span>
            </button>
        </div>

        <div class="nav-right-actions">
            <span class="autosave-badge" id="autosave-status" data-tooltip="Real-time draft auto-saved to browser storage">
                <span class="autosave-dot"></span> Saved
            </span>
            <button class="btn btn-outline nav-tool-secondary" style="font-size:0.7rem; padding:4px 8px; color:#38bdf8; border-color:rgba(56,189,248,0.4);" onclick="startTutorial()" data-tooltip="Interactive 5-Step Guided Walkthrough">
                🎓 Tour
            </button>
            <button class="btn btn-outline nav-tool-secondary" style="font-size:0.7rem; padding:4px 8px;" onclick="openShortcutsModal()" data-tooltip="Keyboard Shortcuts & Power Tools (?)">
                ⌨️ ?
            </button>
            <button class="btn btn-outline nav-tool-secondary" style="font-size:0.7rem; padding:4px 8px;" id="btn-zen-mode" onclick="toggleZenMode()" data-tooltip="Toggle Fullscreen Focus Canvas (Alt+Z)">
                ⛶ Zen
            </button>
            <button class="btn btn-outline nav-tool-secondary" style="font-size:0.7rem; padding:4px 8px;" onclick="openCommandPalette()" data-tooltip="Command Palette Quick Search (Ctrl+K)">
                ⌘K Palette
            </button>
            <button class="btn btn-outline nav-tool-secondary" style="font-size:0.7rem; padding:4px 8px;" onclick="exportAllAsZip()" data-tooltip="Export All 22 Admission Scenarios as a ZIP">
                📦 ZIP All 22
            </button>
            <button class="btn btn-outline nav-tool-secondary" style="font-size:0.7rem; padding:4px 8px;" onclick="exportCrmCsv()" data-tooltip="Export CRM Scenario Mapping as CSV">
                📊 CSV CRM
            </button>
            <button class="btn btn-outline" style="font-size:0.7rem; padding:4px 8px;" onclick="openCodeModal()" data-tooltip="Inspect and Copy Raw Clean HTML">
                &lt;/&gt; Code
            </button>

            <!-- More Actions Dropdown for responsive screens under 1200px -->
            <div class="more-actions-dropdown-wrap" id="more-actions-dropdown-wrap">
                <button type="button" class="btn btn-outline" id="btn-more-actions" onclick="toggleMoreActionsDropdown(event)" data-tooltip="More Tools &amp; Actions">
                    ⚙️ More ▾
                </button>
                <div class="more-actions-menu" id="more-actions-menu">
                    <button type="button" class="more-action-item" onclick="switchView('shell'); toggleMoreActionsDropdown(false);">🏫 Campus Brand Kit</button>
                    <button type="button" class="more-action-item" onclick="toggleZenMode(); toggleMoreActionsDropdown(false);">⛶ Fullscreen Zen (Alt+Z)</button>
                    <button type="button" class="more-action-item" onclick="openCommandPalette(); toggleMoreActionsDropdown(false);">⌘K Command Palette</button>
                    <button type="button" class="more-action-item" onclick="startTutorial(); toggleMoreActionsDropdown(false);">🎓 Launch Guided Tour</button>
                    <button type="button" class="more-action-item" onclick="openShortcutsModal(); toggleMoreActionsDropdown(false);">⌨️ Keyboard Shortcuts (?)</button>
                    <button type="button" class="more-action-item" onclick="exportAllAsZip(); toggleMoreActionsDropdown(false);">📦 Download 22 Templates (ZIP)</button>
                    <button type="button" class="more-action-item" onclick="exportCrmCsv(); toggleMoreActionsDropdown(false);">📊 Export CRM CSV</button>
                    <button type="button" class="more-action-item" onclick="openAutoFixModal(); toggleMoreActionsDropdown(false);">🟢 Delivery Readiness Audit</button>
                </div>
            </div>
        </div>
    </header>

    <!-- ───── Mobile Navigation Drawer & Backdrop ───── -->
    <div class="drawer-backdrop" id="drawer-backdrop" onclick="toggleMobileNav(false)"></div>
    <aside class="mobile-nav-drawer" id="mobile-nav-drawer">
        <div class="mobile-drawer-header">
            <div style="display:flex; align-items:center; gap:8px;">
                <div class="nav-logo-badge">SA</div>
                <div style="font-size:0.85rem; font-weight:700; color:#f8fafc;">Simply Admission</div>
            </div>
            <button type="button" class="btn btn-outline" style="font-size:0.75rem; padding:3px 8px;" onclick="toggleMobileNav(false)">✕</button>
        </div>
        <div class="mobile-drawer-section">
            <div class="mobile-drawer-title">Navigation Views</div>
            <div class="mobile-drawer-nav-list">
                <button type="button" class="mobile-drawer-link active" onclick="switchView('studio'); toggleMobileNav(false);">🎨 Studio Composer</button>
                <button type="button" class="mobile-drawer-link" onclick="switchView('archive'); toggleMobileNav(false);">📁 Template Library</button>
                <button type="button" class="mobile-drawer-link" onclick="switchView('shell'); toggleMobileNav(false);">🏫 Campus Brand Kit</button>
                <button type="button" class="mobile-drawer-link" onclick="switchView('ai'); toggleMobileNav(false);">✨ AI Campaign Generator</button>
                <button type="button" class="mobile-drawer-link" onclick="switchView('home'); toggleMobileNav(false);">🏠 Hub Overview</button>
            </div>
        </div>
        <div class="mobile-drawer-section">
            <div class="mobile-drawer-title">Quick Actions &amp; Tools</div>
            <div class="mobile-drawer-nav-list">
                <button type="button" class="mobile-drawer-link" onclick="startTutorial(); toggleMobileNav(false);">🎓 Launch Guided Tour</button>
                <button type="button" class="mobile-drawer-link" onclick="openShortcutsModal(); toggleMobileNav(false);">⌨️ Keyboard Shortcuts</button>
                <button type="button" class="mobile-drawer-link" onclick="toggleZenMode(); toggleMobileNav(false);">⛶ Fullscreen Zen Canvas</button>
                <button type="button" class="mobile-drawer-link" onclick="openCommandPalette(); toggleMobileNav(false);">⌘K Command Palette</button>
                <button type="button" class="mobile-drawer-link" onclick="openAutoFixModal(); toggleMobileNav(false);">🟢 Delivery Readiness Audit</button>
                <button type="button" class="mobile-drawer-link" onclick="exportAllAsZip(); toggleMobileNav(false);">📦 Download 22 Templates (ZIP)</button>
                <button type="button" class="mobile-drawer-link" onclick="exportCrmCsv(); toggleMobileNav(false);">📊 Export CRM CSV</button>
                <button type="button" class="mobile-drawer-link" onclick="openCodeModal(); toggleMobileNav(false);">&lt;/&gt; Inspect Raw HTML</button>
            </div>
        </div>
    </aside>

    <!-- ───── App Workspace ───── -->
    <main class="app-body">

        <!-- ═══════════════════════════════════════════════════════
             VIEW 1: TEMPLATE STUDIO
        ═══════════════════════════════════════════════════════ -->
        <section id="view-studio" class="app-view active">
            <!-- Mobile Segmented Switcher -->
            <div class="mobile-mode-switcher" id="mobile-studio-switcher">
                <button type="button" class="mobile-mode-btn active" id="btn-mob-edit" onclick="setMobileStudioMode('edit')">
                    ✏️ Editor
                </button>
                <button type="button" class="mobile-mode-btn" id="btn-mob-preview" onclick="setMobileStudioMode('preview')">
                    👁️ Preview
                </button>
            </div>

            <!-- Left Editor Panel -->
            <div class="studio-editor-panel" id="studio-editor-panel">
                <div class="editor-header">
                    <span class="editor-header-title">
                        <span>Message Composer</span>
                        <span id="read-time-badge" style="font-size:0.68rem; color:var(--text-dim); font-weight:normal;">40s read</span>
                    </span>
                    <div style="display:flex; gap:4px; align-items:center; flex-wrap:wrap;">
                        <button type="button" class="btn btn-outline" style="font-size:0.66rem; padding:2px 6px;" onclick="toggleAllSections(true)" data-tooltip="Expand All Accordion Cards">⤢ Expand All</button>
                        <button type="button" class="btn btn-outline" style="font-size:0.66rem; padding:2px 6px;" onclick="toggleAllSections(false)" data-tooltip="Collapse All Accordion Cards">⤡ Collapse All</button>
                        <button type="button" class="btn btn-outline" style="font-size:0.68rem; padding:2px 6px;" onclick="undo()" data-tooltip="Undo Last Change (Ctrl+Z)">↶</button>
                        <button type="button" class="btn btn-outline" style="font-size:0.68rem; padding:2px 6px;" onclick="redo()" data-tooltip="Redo Change (Ctrl+Y)">↷</button>
                        <div class="mode-pill-toggle">
                            <button type="button" class="mode-pill-btn active" id="btn-mode-form" onclick="setEditorMode('form')" data-tooltip="Visual Form Composer">✨ Visual</button>
                            <button type="button" class="mode-pill-btn" id="btn-mode-raw" onclick="setEditorMode('raw')" data-tooltip="Raw Code Inspector">&lt;/&gt; Code</button>
                        </div>
                        <button type="button" class="btn btn-outline" style="font-size:0.68rem; padding:2px 7px;" onclick="resetTemplate()" data-tooltip="Reset Template to Default Baseline">↺ Reset</button>
                    </div>
                </div>

                <div class="editor-scroll-area">
                    <!-- Section 1: Scenario & Interactive Paginator -->
                    <div class="editor-section-card" id="card-scenario">
                        <div class="editor-section-header" onclick="toggleSection('card-scenario')">
                            <div class="editor-section-title">
                                <span>📋 1. Workflow Scenario &amp; Paginator</span>
                                <span class="editor-section-badge" id="active-scenario-count-badge">22 Alerts</span>
                            </div>
                            <button type="button" class="section-toggle-btn" aria-label="Toggle Scenario Section">▼</button>
                        </div>
                        <div class="editor-section-body">
                            <!-- Scenario Interactive Paginator -->
                            <div class="scenario-paginator" id="scenario-paginator">
                                <div class="paginator-top-row">
                                    <div class="paginator-info" id="paginator-scenario-title">Page 1 of 22: Mobile No Verification OTP</div>
                                    <div class="paginator-controls">
                                        <button type="button" class="btn btn-outline" style="font-size:0.65rem; padding:2px 5px;" onclick="goToScenarioPage(0)" data-tooltip="First Scenario">⏮</button>
                                        <button type="button" class="btn btn-outline" style="font-size:0.65rem; padding:2px 6px;" onclick="stepTemplate(-1)" data-tooltip="Previous Scenario ([)">◀ Prev</button>
                                        <button type="button" class="btn btn-outline" style="font-size:0.65rem; padding:2px 6px;" onclick="stepTemplate(1)" data-tooltip="Next Scenario (])">Next ▶</button>
                                        <button type="button" class="btn btn-outline" style="font-size:0.65rem; padding:2px 5px;" onclick="goToScenarioPage(21)" data-tooltip="Last Scenario">⏭</button>
                                    </div>
                                </div>
                                <div class="horizontal-scroll-wrap" style="margin-top:6px;">
                                    <button type="button" class="scroll-arrow-btn left" onclick="scrollContainer('paginator-strip-container', -120)" aria-label="Scroll Paginator Left">◀</button>
                                    <div class="paginator-strip" id="paginator-strip-container">
                                        <!-- Numbered pills 1..22 rendered here -->
                                    </div>
                                    <button type="button" class="scroll-arrow-btn right" onclick="scrollContainer('paginator-strip-container', 120)" aria-label="Scroll Paginator Right">▶</button>
                                </div>
                            </div>

                            <!-- Category Filter Pills with Horizontal Scroller -->
                            <div style="margin-top:8px;">
                                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
                                    <span style="font-size:0.65rem; color:var(--text-dim); text-transform:uppercase; letter-spacing:0.4px;">Filter Scenarios by Category:</span>
                                </div>
                                <div class="horizontal-scroll-wrap">
                                    <button type="button" class="scroll-arrow-btn left" onclick="scrollContainer('scen-cat-pills-bar', -120)" aria-label="Scroll Categories Left">◀</button>
                                    <div class="scen-category-pills" id="scen-cat-pills-bar">
                                        <button type="button" class="scen-cat-pill active" data-cat="All" onclick="filterScenariosByCategory('All')">All (22)</button>
                                        <button type="button" class="scen-cat-pill" data-cat="Authentication" onclick="filterScenariosByCategory('Authentication')">🔑 Auth (6)</button>
                                        <button type="button" class="scen-cat-pill" data-cat="Enquiry" onclick="filterScenariosByCategory('Enquiry')">📝 Enquiry (5)</button>
                                        <button type="button" class="scen-cat-pill" data-cat="Meeting" onclick="filterScenariosByCategory('Meeting')">📅 Visits (4)</button>
                                        <button type="button" class="scen-cat-pill" data-cat="Payment" onclick="filterScenariosByCategory('Payment')">💳 Fees (3)</button>
                                        <button type="button" class="scen-cat-pill" data-cat="Application" onclick="filterScenariosByCategory('Application')">🎓 Apps (4)</button>
                                    </div>
                                    <button type="button" class="scroll-arrow-btn right" onclick="scrollContainer('scen-cat-pills-bar', 120)" aria-label="Scroll Categories Right">▶</button>
                                </div>
                            </div>

                            <div style="margin-top:8px;">
                                <select class="form-select" id="inp-template-selector" onchange="onTemplateSelect(this.value)">
                                    <option value="custom">✏️ Custom Blank Template</option>
                                </select>
                            </div>
                        </div>
                    </div>

                    <!-- Section 2: Brand Theme Presets -->
                    <div class="editor-section-card" id="card-brand-presets">
                        <div class="editor-section-header" onclick="toggleSection('card-brand-presets')">
                            <div class="editor-section-title">
                                <span>🎨 2. Quick Brand Theme Presets</span>
                                <span class="editor-section-badge">12 Themes</span>
                            </div>
                            <button type="button" class="section-toggle-btn" aria-label="Toggle Brand Presets">▼</button>
                        </div>
                        <div class="editor-section-body">
                            <div style="font-size:0.65rem; color:var(--text-dim); margin-bottom:6px;">Apply 1-click harmonized brand palette to header, buttons, background, fonts, and highlights:</div>
                            <div class="horizontal-scroll-wrap">
                                <button type="button" class="scroll-arrow-btn left" onclick="scrollContainer('brand-presets-container', -180)" aria-label="Scroll Presets Left">◀</button>
                                <div class="brand-presets-bar" id="brand-presets-container">
                                    <button type="button" class="theme-preset-btn active" style="--p-color:#2563eb;" onclick="applyBrandPreset(0)" data-tooltip="Simply Blue (#2563eb)"><span class="dot"></span> Simply Blue</button>
                                    <button type="button" class="theme-preset-btn" style="--p-color:#059669;" onclick="applyBrandPreset(1)" data-tooltip="Emerald Luxe (#059669)"><span class="dot"></span> Emerald</button>
                                    <button type="button" class="theme-preset-btn" style="--p-color:#991b1b;" onclick="applyBrandPreset(2)" data-tooltip="Classic Crimson (#991b1b)"><span class="dot"></span> Crimson</button>
                                    <button type="button" class="theme-preset-btn" style="--p-color:#4f46e5;" onclick="applyBrandPreset(3)" data-tooltip="Royal Indigo (#4f46e5)"><span class="dot"></span> Indigo</button>
                                    <button type="button" class="theme-preset-btn" style="--p-color:#d97706;" onclick="applyBrandPreset(4)" data-tooltip="Sunset Amber (#d97706)"><span class="dot"></span> Amber</button>
                                    <button type="button" class="theme-preset-btn" style="--p-color:#0f172a;" onclick="applyBrandPreset(5)" data-tooltip="Slate Noir (#0f172a)"><span class="dot"></span> Slate</button>
                                    <button type="button" class="theme-preset-btn" style="--p-color:#0d9488;" onclick="applyBrandPreset(6)" data-tooltip="Nordic Teal (#0d9488)"><span class="dot"></span> Teal</button>
                                    <button type="button" class="theme-preset-btn" style="--p-color:#38bdf8;" onclick="applyBrandPreset(7)" data-tooltip="Midnight Obsidian (#38bdf8)"><span class="dot"></span> Midnight</button>
                                    <button type="button" class="theme-preset-btn" style="--p-color:#7c3aed;" onclick="applyBrandPreset(8)" data-tooltip="Amethyst Purple (#7c3aed)"><span class="dot"></span> Amethyst</button>
                                    <button type="button" class="theme-preset-btn" style="--p-color:#e11d48;" onclick="applyBrandPreset(9)" data-tooltip="Coral Blossom (#e11d48)"><span class="dot"></span> Coral</button>
                                    <button type="button" class="theme-preset-btn" style="--p-color:#854d0e;" onclick="applyBrandPreset(10)" data-tooltip="Cyber Bronze (#854d0e)"><span class="dot"></span> Bronze</button>
                                    <button type="button" class="theme-preset-btn" style="--p-color:#475569;" onclick="applyBrandPreset(11)" data-tooltip="Titanium Tech (#475569)"><span class="dot"></span> Titanium</button>
                                </div>
                                <button type="button" class="scroll-arrow-btn right" onclick="scrollContainer('brand-presets-container', 180)" aria-label="Scroll Presets Right">▶</button>
                            </div>
                        </div>
                    </div>

                    <!-- Section 3: Visual Styler & Typography -->
                    <div class="editor-section-card" id="card-visual-styler">
                        <div class="editor-section-header" onclick="toggleSection('card-visual-styler')">
                            <div class="editor-section-title">
                                <span>✨ 3. Visual Styler &amp; Typography</span>
                                <span class="editor-section-badge">Layout &amp; Styling</span>
                            </div>
                            <button type="button" class="section-toggle-btn" aria-label="Toggle Visual Styler">▼</button>
                        </div>
                        <div class="editor-section-body">
                            <!-- Typography & Button Corner Style -->
                            <div style="display:grid; grid-template-columns: 1fr 1fr; gap:6px; margin-bottom:6px;">
                                <div>
                                    <label style="font-size:0.62rem; color:var(--text-dim); display:block; margin-bottom:2px;">Email Typography</label>
                                    <select class="form-select" id="inp-font-family" style="font-size:0.72rem; padding:3px 6px;" onchange="rebuildPreview()">
                                        <option value="Arial, Helvetica, sans-serif">Arial / Clean</option>
                                        <option value="'Helvetica Neue', Helvetica, Arial, sans-serif">Helvetica Modern</option>
                                        <option value="Georgia, 'Times New Roman', serif">Georgia / Classic</option>
                                        <option value="Tahoma, Verdana, sans-serif">Tahoma / Formal</option>
                                        <option value="'Trebuchet MS', sans-serif">Trebuchet MS</option>
                                        <option value="Verdana, Geneva, sans-serif">Verdana / Wide</option>
                                    </select>
                                </div>
                                <div>
                                    <label style="font-size:0.62rem; color:var(--text-dim); display:block; margin-bottom:2px;">Button Corner Style</label>
                                    <select class="form-select" id="inp-btn-radius" style="font-size:0.72rem; padding:3px 6px;" onchange="rebuildPreview()">
                                        <option value="6px">Rounded (6px)</option>
                                        <option value="24px">Full Pill (24px)</option>
                                        <option value="0px">Sharp Square (0px)</option>
                                    </select>
                                </div>
                            </div>
                            <!-- Button Width & Header Banner Style -->
                            <div style="display:grid; grid-template-columns: 1fr 1fr; gap:6px; margin-bottom:6px;">
                                <div>
                                    <label style="font-size:0.62rem; color:var(--text-dim); display:block; margin-bottom:2px;">Button Width</label>
                                    <select class="form-select" id="inp-btn-width" style="font-size:0.72rem; padding:3px 6px;" onchange="rebuildPreview()">
                                        <option value="auto">Auto Centered</option>
                                        <option value="100%">Full Width Mobile CTA</option>
                                    </select>
                                </div>
                                <div>
                                    <label style="font-size:0.62rem; color:var(--text-dim); display:block; margin-bottom:2px;">Header Banner Style</label>
                                    <select class="form-select" id="inp-header-style" style="font-size:0.72rem; padding:3px 6px;" onchange="rebuildPreview()">
                                        <option value="minimal">Minimal Clean Logo</option>
                                        <option value="accent">Top Accent Color Bar</option>
                                        <option value="hero">Branded Header Box</option>
                                    </select>
                                </div>
                            </div>
                            <!-- Logo Size & Alignment -->
                            <div style="display:flex; align-items:center; justify-content:space-between; gap:8px;">
                                <div style="flex:1;">
                                    <label style="font-size:0.62rem; color:var(--text-dim); display:block; margin-bottom:2px;">Logo Height: <span id="lbl-logo-size">48px</span></label>
                                    <input type="range" min="32" max="80" value="48" id="inp-logo-size" style="width:100%; accent-color:var(--primary);" oninput="document.getElementById('lbl-logo-size').textContent=this.value+'px'; rebuildPreview();">
                                </div>
                                <div>
                                    <label style="font-size:0.62rem; color:var(--text-dim); display:block; margin-bottom:2px;">Logo Align</label>
                                    <div class="viewport-segmented" style="padding:1px;">
                                        <button type="button" class="viewport-btn active" id="btn-logo-center" onclick="setLogoAlign('center')">Center</button>
                                        <button type="button" class="viewport-btn" id="btn-logo-left" onclick="setLogoAlign('left')">Left</button>
                                    </div>
                                </div>
                            </div>

                            <!-- Synchronized Color Tuner -->
                            <div style="margin-top:8px; padding-top:8px; border-top:1px solid rgba(255,255,255,0.06);">
                                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
                                    <label style="font-size:0.62rem; color:var(--text-dim); margin:0;">🎨 Synchronized Palette Tuner</label>
                                    <span id="styler-wcag-badge" style="font-size:0.58rem; color:#10b981; font-weight:600;">WCAG AAA (10.4:1)</span>
                                </div>
                                <div style="display:grid; grid-template-columns: 1fr 1fr 1fr; gap:6px;">
                                    <div>
                                        <label style="font-size:0.58rem; color:var(--text-muted); display:block; margin-bottom:2px;">Brand Accent</label>
                                        <input type="color" id="inp-theme-color-mini" value="#2563eb" style="width:100%; height:26px; border:1px solid var(--border-subtle); border-radius:3px; background:none; cursor:pointer;" onchange="setThemeColor(this.value)">
                                    </div>
                                    <div>
                                        <label style="font-size:0.58rem; color:var(--text-muted); display:block; margin-bottom:2px;">Outer Canvas</label>
                                        <input type="color" id="inp-bg-color-mini" value="#f1f5f9" style="width:100%; height:26px; border:1px solid var(--border-subtle); border-radius:3px; background:none; cursor:pointer;" onchange="setOuterBgColor(this.value)">
                                    </div>
                                    <div>
                                        <label style="font-size:0.58rem; color:var(--text-muted); display:block; margin-bottom:2px;">Font Color</label>
                                        <input type="color" id="inp-text-color-mini" value="#334155" style="width:100%; height:26px; border:1px solid var(--border-subtle); border-radius:3px; background:none; cursor:pointer;" onchange="setBodyTextColor(this.value)">
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Section 4: Subject Line & Inbox Snippet -->
                    <div class="editor-section-card" id="card-subject-header">
                        <div class="editor-section-header" onclick="toggleSection('card-subject-header')">
                            <div class="editor-section-title">
                                <span>✉️ 4. Subject Line &amp; Inbox Snippet</span>
                                <span class="editor-section-badge">Inbox Preview</span>
                            </div>
                            <button type="button" class="section-toggle-btn" aria-label="Toggle Subject & Headers">▼</button>
                        </div>
                        <div class="editor-section-body">
                            <!-- Preheader Preview Text -->
                            <div class="form-group">
                                <label class="form-label">
                                    <span>Preheader Preview Text</span>
                                    <span style="font-size:0.66rem; color:var(--text-dim);">Inbox preview snippet</span>
                                </label>
                                <input type="text" class="form-input" id="inp-preheader" placeholder="Brief summary displayed in parent mobile inbox previews..." oninput="rebuildPreview()">
                            </div>

                            <!-- Subject Line with Character Counter -->
                            <div class="form-group">
                                <label class="form-label">
                                    <span>Email Subject</span>
                                    <div class="subj-counter-wrap">
                                        <span class="subj-counter-badge safe" id="subj-char-count">0 / 50</span>
                                        <span style="font-size:0.64rem; color:var(--text-dim);">Mobile limit</span>
                                    </div>
                                </label>
                                <input type="text" class="form-input" id="inp-subject" oninput="onSubjectInput()">
                            </div>

                            <!-- Headline Title -->
                            <div class="form-group">
                                <label class="form-label">Headline / Banner Title</label>
                                <input type="text" class="form-input" id="inp-headline" oninput="rebuildPreview()">
                            </div>

                            <!-- Greeting Line & Quick Switchers -->
                            <div class="form-group" style="margin-bottom:0;">
                                <label class="form-label">
                                    <span>Greeting Line</span>
                                    <span style="font-size:0.66rem; color:var(--text-dim);">1-click presets below</span>
                                </label>
                                <input type="text" class="form-input" id="inp-greeting" oninput="rebuildPreview()">
                                <div class="greeting-pills">
                                    <button type="button" class="greeting-pill-btn" onclick="setGreeting('Dear Parents,')">Dear Parents,</button>
                                    <button type="button" class="greeting-pill-btn" onclick="setGreeting('Dear {{{{student_name}}}} & Parents,')">Dear {{{{student_name}}}} &amp; Parents,</button>
                                    <button type="button" class="greeting-pill-btn" onclick="setGreeting('Dear Candidate,')">Dear Candidate,</button>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Section 5: Message Body & CRM Variables -->
                    <div class="editor-section-card" id="card-body-crm">
                        <div class="editor-section-header" onclick="toggleSection('card-body-crm')">
                            <div class="editor-section-title">
                                <span>📝 5. Message Body &amp; CRM Variables</span>
                                <span class="editor-section-badge">68 Variables</span>
                            </div>
                            <button type="button" class="section-toggle-btn" aria-label="Toggle Message Body">▼</button>
                        </div>
                        <div class="editor-section-body">
                            <!-- Body Content with Toolbar & Variables -->
                            <div class="form-group" style="margin-bottom:6px;">
                                <label class="form-label">
                                    <span>Body Content</span>
                                    <span style="font-size:0.66rem; color:var(--text-dim);">Type @ or / to search 68 keys</span>
                                </label>

                                <!-- Formatting Toolbar & Quick Component Inserters -->
                                <div class="editor-toolbar" style="flex-wrap:wrap; gap:3px;">
                                    <button type="button" class="tool-btn" onclick="wrapSelection('<strong>', '</strong>')" title="Bold"><b>B</b></button>
                                    <button type="button" class="tool-btn" onclick="wrapSelection('<em>', '</em>')" title="Italic"><i>I</i></button>
                                    <button type="button" class="tool-btn" onclick="insertCalloutBlock()" title="Insert Callout Card">📦 Box</button>
                                    <button type="button" class="tool-btn" onclick="insertFeeTable()" title="Insert Fee Breakdown Table">+ 💳 Fee Table</button>
                                    <button type="button" class="tool-btn" onclick="insertScheduleCard()" title="Insert Date/Time Schedule Card">+ 📅 Schedule</button>
                                    <button type="button" class="tool-btn" onclick="insertChecklist()" title="Insert Document Checklist">+ 📋 Checklist</button>
                                    <button type="button" class="tool-btn" onclick="insertSupportHelpdesk()" title="Insert Admissions Helpdesk Bar">+ 📞 Helpdesk</button>
                                    <button type="button" class="tool-btn" onclick="toggleCrmDrawer()" title="Variable Explorer">🏷️ Tag</button>
                                </div>

                                <textarea class="form-textarea" id="inp-body" rows="6" oninput="onBodyInput()" placeholder="Enter message copy here..."></textarea>

                                <!-- Tag Lint Warning -->
                                <div class="lint-alert-box" id="lint-alert-box"></div>
                            </div>

                            <!-- Top 8 Quick Variable Chips with Horizontal Scroller -->
                            <div style="margin-top: 8px;">
                                <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:4px;">
                                    <span style="font-size:0.67rem; font-weight:700; color:var(--text-secondary); letter-spacing:0.4px;">CRM VARIABLES (68 KEYS):</span>
                                    <button type="button" class="btn btn-outline" style="font-size:0.65rem; padding:2px 6px;" onclick="toggleCrmDrawer()">
                                        🔍 <span id="crm-drawer-toggle-text">Explore All 68 Keys</span>
                                    </button>
                                </div>

                                <div class="horizontal-scroll-wrap">
                                    <button type="button" class="scroll-arrow-btn left" onclick="scrollContainer('quick-chips-container', -140)" aria-label="Scroll Variables Left">◀</button>
                                    <div class="quick-chips-bar" id="quick-chips-container">
                                        <button type="button" class="quick-chip-btn" onclick="insertTag('{{{{student_name}}}}')">+ Student Name</button>
                                        <button type="button" class="quick-chip-btn" onclick="insertTag('{{{{student_class}}}}')">+ Class</button>
                                        <button type="button" class="quick-chip-btn" onclick="insertTag('{{{{enquiry_auto_id}}}}')">+ Enquiry ID</button>
                                        <button type="button" class="quick-chip-btn" onclick="insertTag('{{{{application_no}}}}')">+ App No</button>
                                        <button type="button" class="quick-chip-btn" onclick="insertTag('{{{{username}}}}')">+ Username</button>
                                        <button type="button" class="quick-chip-btn" onclick="insertTag('{{{{passwords}}}}')">+ Password</button>
                                        <button type="button" class="quick-chip-btn" onclick="insertTag('{{{{current_fee_receipt_amount}}}}')">+ Fee Amount</button>
                                        <button type="button" class="quick-chip-btn" onclick="insertTag('{{{{payment_link}}}}')">+ Payment Link</button>
                                    </div>
                                    <button type="button" class="scroll-arrow-btn right" onclick="scrollContainer('quick-chips-container', 140)" aria-label="Scroll Variables Right">▶</button>
                                </div>

                                <!-- Collapsible 68 Keys Drawer -->
                                <div id="crm-vars-drawer" class="drawer-box" style="display: none; margin-top:8px;">
                                    <input type="text" class="drawer-search-inp" id="crm-search-inp" placeholder="Search 68 variables (e.g. father, tour, fee, receipt, otp)..." oninput="onCrmSearchChange(this.value)">
                                    <div class="drawer-pills" id="crm-category-pills"></div>
                                    <div class="drawer-chips-grid" id="crm-tags-chips-container"></div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Section 6: Modular Content Blocks -->
                    <div class="editor-section-card" id="card-modular-blocks">
                        <div class="editor-section-header" onclick="toggleSection('card-modular-blocks')">
                            <div class="editor-section-title">
                                <span>🧩 6. Modular Content Blocks</span>
                                <span class="editor-section-badge">Interactive Components</span>
                            </div>
                            <button type="button" class="section-toggle-btn" aria-label="Toggle Modular Blocks">▼</button>
                        </div>
                        <div class="editor-section-body">
                            <!-- Block 1: Urgent Notice Strip -->
                            <div class="modular-block-card">
                                <label class="checkbox-label">
                                    <input type="checkbox" id="inp-include-notice" onchange="rebuildPreview()">
                                    <span>Include High-Visibility Notice Banner</span>
                                </label>
                                <div id="notice-inputs-wrap" style="display:none; margin-top:6px;">
                                    <input type="text" class="form-input" id="inp-notice-text" value="Please note: The deadline for document verification is fast approaching." oninput="rebuildPreview()" placeholder="Notice text...">
                                </div>
                            </div>

                            <!-- Block 2: 3-Step Milestone Roadmap -->
                            <div class="modular-block-card">
                                <label class="checkbox-label">
                                    <input type="checkbox" id="inp-include-roadmap" onchange="rebuildPreview()">
                                    <span>Include 3-Step Admission Roadmap</span>
                                </label>
                            </div>

                            <!-- Block 3: Pure CSS Credentials Card -->
                            <div class="modular-block-card">
                                <label class="checkbox-label">
                                    <input type="checkbox" id="inp-include-login" checked onchange="rebuildPreview()">
                                    <span>Include Candidate Portal Login Box (CSS Styled)</span>
                                </label>
                                <div id="login-inputs-wrap" style="margin-top:6px;">
                                    <input type="text" class="form-input" id="inp-login-prompt" value="Complete your Application Form using your Candidate Portal credentials below:" oninput="rebuildPreview()" placeholder="Login Prompt Text" style="margin-bottom:5px;">
                                    <input type="text" class="form-input" id="inp-button-text" value="ADMISSION PORTAL LOGIN" oninput="rebuildPreview()" placeholder="Button Text">
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Section 7: Sign-off & Team -->
                    <div class="editor-section-card" id="card-signoff">
                        <div class="editor-section-header" onclick="toggleSection('card-signoff')">
                            <div class="editor-section-title">
                                <span>✍️ 7. Sign-off &amp; Team Closing</span>
                                <span class="editor-section-badge">Sign-off</span>
                            </div>
                            <button type="button" class="section-toggle-btn" aria-label="Toggle Sign-off">▼</button>
                        </div>
                        <div class="editor-section-body">
                            <div class="form-group" style="margin-bottom:0;">
                                <label class="form-label">Sign-off Team</label>
                                <input type="text" class="form-input" id="inp-signoff-team" value="Team Admissions" oninput="rebuildPreview()">
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Right Live Preview Stage -->
            <div class="studio-stage" id="studio-stage-panel">
                <div class="stage-toolbar">
                    <div class="stage-controls-left">
                        <div class="viewport-segmented">
                            <button class="viewport-btn active" id="btn-vp-desktop" onclick="setViewportMode('desktop')" title="Desktop View (640px)">🖥️ Desk</button>
                            <button class="viewport-btn" id="btn-vp-tablet" onclick="setViewportMode('tablet')" title="Tablet View (480px)">📱 Tab</button>
                            <button class="viewport-btn" id="btn-vp-mobile" onclick="setViewportMode('mobile')" title="Mobile Mockup (375px)">📱 Mob</button>
                            <button class="viewport-btn" id="btn-vp-dual" onclick="setViewportMode('dual')" title="Side-by-Side Dual View (Desktop + Mobile simultaneous)">🖥️+📱 Dual</button>
                        </div>

                        <!-- Zoom Controls -->
                        <div class="viewport-segmented">
                            <button class="viewport-btn" onclick="setZoom(0.8)">80%</button>
                            <button class="viewport-btn" onclick="setZoom(0.9)">90%</button>
                            <button class="viewport-btn active" id="btn-zoom-100" onclick="setZoom(1)">100%</button>
                        </div>

                        <!-- Dark Mode Email Simulation -->
                        <button type="button" class="toggle-chip-btn" id="btn-dark-sim" onclick="toggleDarkSimulation()" title="Preview how email looks in Parent Dark Mode">
                            🌙 Dark Sim
                        </button>

                        <!-- Click-to-Edit WYSIWYG Mode in Preview -->
                        <button type="button" class="toggle-chip-btn" id="btn-inpreview-edit" onclick="toggleInPreviewEdit()" title="Click directly on text in preview to edit in place">
                            ✏️ Live Edit
                        </button>

                        <!-- Lock Screen Notification Mockup Toggle -->
                        <button type="button" class="toggle-chip-btn" id="btn-lockscreen-toggle" onclick="toggleLockscreenMockup()" title="Preview mobile inbox notification">
                            📱 Lockscreen
                        </button>

                        <!-- SMS / WhatsApp Companion Toggle -->
                        <button type="button" class="toggle-chip-btn" id="btn-omni-toggle" onclick="toggleOmniCompanion()" title="SMS & WhatsApp companion text">
                            💬 WA / SMS
                        </button>

                        <!-- Template Delivery Readiness Score -->
                        <div class="readiness-meter" id="readiness-meter-badge" onclick="openAutoFixModal()" title="Click to view 1-Click Delivery Readiness Fixes">
                            🟢 100% Ready
                        </div>

                        <!-- Test Data Customizer Toggle -->
                        <button type="button" class="toggle-chip-btn" id="btn-custom-sample-toggle" onclick="toggleSampleCustomizer()" title="Customize Test Data Values">
                            🧪 Test Data
                        </button>

                        <!-- Sample Data Toggle -->
                        <div style="display:flex; align-items:center; gap:5px; margin-left:4px;">
                            <label style="display:flex; align-items:center; gap:5px; cursor:pointer; font-size:0.73rem;">
                                <input type="checkbox" id="inp-sample-toggle" checked onchange="rebuildPreview()">
                                <span id="lbl-sample-mode" style="color:#34d399; font-weight:600;">Sample Data</span>
                            </label>
                        </div>
                    </div>

                    <!-- Utility Button Group (Grouped Flex Container) -->
                    <div class="utility-btn-group" id="utility-btn-group">
                        <button class="btn btn-outline" onclick="copySubject()" title="Copy Subject Line">Copy Subject</button>
                        <button class="btn btn-outline" style="background:rgba(37,99,235,0.15); color:#60a5fa; border-color:#3b82f6;" onclick="copyFormattedForGmail()" title="Copy Formatted Email to Paste directly into Gmail or Outlook (Ctrl+V)">📋 Paste to Gmail</button>
                        <button class="btn btn-success" onclick="copyHTML()" title="Copy Clean Production HTML">Copy HTML</button>
                        <button class="btn btn-outline" onclick="printTemplate()" title="Print or Save as PDF Proof">🖨️ Print</button>
                        <button class="btn btn-primary" onclick="downloadHTML()" title="Download .html file">Download</button>
                    </div>
                </div>

                <div class="stage-canvas">
                    <!-- Interactive Test Data Customizer Widget -->
                    <div class="sample-customizer-card" id="sample-customizer-card" style="display:none;">
                        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                            <span style="font-size:0.75rem; font-weight:700; color:#38bdf8;">🧪 TEST DATA CUSTOMIZER (UPDATES PREVIEW IN REAL TIME)</span>
                            <button type="button" class="btn btn-outline" style="font-size:0.65rem; padding:1px 6px;" onclick="resetCustomTestData()">Reset Defaults</button>
                        </div>
                        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap:6px;">
                            <div>
                                <label style="font-size:0.62rem; color:var(--text-dim); display:block; margin-bottom:2px;">Student Name</label>
                                <input type="text" class="drawer-search-inp" style="margin-bottom:0;" id="cust-student-name" value="Aarav Sharma" oninput="onCustomTestDataChange()">
                            </div>
                            <div>
                                <label style="font-size:0.62rem; color:var(--text-dim); display:block; margin-bottom:2px;">Student Class</label>
                                <input type="text" class="drawer-search-inp" style="margin-bottom:0;" id="cust-student-class" value="Grade 1" oninput="onCustomTestDataChange()">
                            </div>
                            <div>
                                <label style="font-size:0.62rem; color:var(--text-dim); display:block; margin-bottom:2px;">Father / Parent</label>
                                <input type="text" class="drawer-search-inp" style="margin-bottom:0;" id="cust-parent-name" value="Mr. Vikram Sharma" oninput="onCustomTestDataChange()">
                            </div>
                            <div>
                                <label style="font-size:0.62rem; color:var(--text-dim); display:block; margin-bottom:2px;">Fee Amount</label>
                                <input type="text" class="drawer-search-inp" style="margin-bottom:0;" id="cust-fee-amount" value="₹ 2,500" oninput="onCustomTestDataChange()">
                            </div>
                            <div>
                                <label style="font-size:0.62rem; color:var(--text-dim); display:block; margin-bottom:2px;">OTP Code</label>
                                <input type="text" class="drawer-search-inp" style="margin-bottom:0;" id="cust-otp-code" value="482910" oninput="onCustomTestDataChange()">
                            </div>
                            <div>
                                <label style="font-size:0.62rem; color:var(--text-dim); display:block; margin-bottom:2px;">Application ID</label>
                                <input type="text" class="drawer-search-inp" style="margin-bottom:0;" id="cust-app-no" value="APP-2026-8941" oninput="onCustomTestDataChange()">
                            </div>
                        </div>
                    </div>
                    <!-- Lockscreen Notification Mockup Widget -->
                    <div class="lockscreen-card" id="lockscreen-mockup-card">
                        <div class="ls-header">
                            <span id="ls-sender-name">SIMPLY ADMISSION</span>
                            <span>now</span>
                        </div>
                        <div class="ls-title" id="ls-subject-text">Your Admission Enquiry - Simply Admission</div>
                        <div class="ls-body" id="ls-snippet-text">Thank you for your interest in Grade 1 admission...</div>
                    </div>

                    <!-- WhatsApp / SMS Companion Widget -->
                    <div class="omni-companion-card" id="omni-companion-card">
                        <div class="omni-header">
                            <span>💬 OMNICHANNEL SMS &amp; WHATSAPP COMPANION</span>
                            <button type="button" class="btn btn-outline" style="font-size:0.65rem; padding:1px 6px; color:#34d399; border-color:#34d399;" onclick="copyOmniText()">Copy Text</button>
                        </div>
                        <div class="omni-text" id="omni-text-content"></div>
                    </div>

                    <!-- Standard Single Email Preview Container -->
                    <div class="preview-wrapper" id="preview-wrapper">
                        <div class="mobile-notch"></div>
                        <iframe id="live-iframe" class="live-preview-iframe"></iframe>
                    </div>

                    <!-- Dual Viewport Container (Desktop + Mobile Side-by-Side) -->
                    <div class="dual-preview-container" id="dual-preview-container" style="display:none;">
                        <div style="flex:0 0 640px; max-width:640px;">
                            <div style="font-size:0.72rem; font-weight:700; color:#38bdf8; margin-bottom:6px; text-align:center;">🖥️ DESKTOP VIEW (640px)</div>
                            <div class="preview-wrapper desktop" style="max-width:640px; margin:0 auto;">
                                <iframe id="live-iframe-desktop" class="live-preview-iframe" title="Desktop Preview"></iframe>
                            </div>
                        </div>
                        <div style="flex:0 0 380px; max-width:380px;">
                            <div style="font-size:0.72rem; font-weight:700; color:#34d399; margin-bottom:6px; text-align:center;">📱 MOBILE VIEW (375px)</div>
                            <div class="phone-chassis" style="margin:0 auto;">
                                <div class="phone-notch"></div>
                                <iframe id="live-iframe-mobile" class="live-preview-iframe" style="height:580px;" title="Mobile Preview"></iframe>
                            </div>
                        </div>
                    </div>

                    <!-- Floating Bottom Action Dock -->
                    <div class="floating-action-dock" id="floating-action-dock">
                        <button class="btn btn-outline" style="font-size:0.68rem; padding:3px 9px; border-radius:12px; background:rgba(37,99,235,0.25); color:#60a5fa; border-color:#3b82f6;" onclick="copyFormattedForGmail()" title="Paste directly into Gmail / Outlook (Ctrl+V)">📋 Paste to Gmail</button>
                        <button class="btn btn-success" style="font-size:0.68rem; padding:3px 9px; border-radius:12px;" onclick="copyHTML()" title="Copy Production HTML">Copy HTML</button>
                        <button class="btn btn-outline" style="font-size:0.68rem; padding:3px 8px; border-radius:12px;" onclick="toggleDarkSimulation()" title="Simulate Parent Dark Mode">🌙</button>
                        <button class="btn btn-outline" style="font-size:0.68rem; padding:3px 8px; border-radius:12px;" onclick="toggleInPreviewEdit()" id="btn-dock-wysiwyg" title="Click-to-Edit in Preview">✏️ Edit</button>
                        <button class="btn btn-outline" style="font-size:0.68rem; padding:3px 8px; border-radius:12px;" onclick="openCommandPalette()" title="Ctrl+K Command Palette">⌘K</button>
                    </div>
                </div>
            </div>
        </section>

        <!-- ═══════════════════════════════════════════════════════
             VIEW 2: TEMPLATE LIBRARY
        ═══════════════════════════════════════════════════════ -->
        <section id="view-archive" class="app-view">
            <div class="archive-sidebar">
                <div class="archive-search-box">
                    <input type="text" class="form-input" id="archive-search-inp" placeholder="Search templates..." oninput="filterArchiveList(this.value)">
                </div>
                <div class="archive-list" id="archive-items-container"></div>
                <!-- Template Library Paginator Strip -->
                <div class="archive-paginator-strip" id="archive-paginator" style="display:flex; justify-content:space-between; align-items:center; padding:10px 14px; border-top:1px solid var(--border-subtle); background:var(--bg-panel); font-size:0.7rem;">
                    <button type="button" class="btn btn-outline" id="btn-archive-prev" onclick="stepArchivePage(-1)" style="font-size:0.67rem; padding:3px 8px;">◀ Prev</button>
                    <span id="archive-page-info" style="color:var(--text-dim); font-weight:600;">Page 1 of 1</span>
                    <button type="button" class="btn btn-outline" id="btn-archive-next" onclick="stepArchivePage(1)" style="font-size:0.67rem; padding:3px 8px;">Next ▶</button>
                </div>
            </div>
            <div class="studio-stage">
                <div class="stage-toolbar">
                    <span id="archive-current-title" style="font-size:0.8rem; font-weight:700;">Template Preview</span>
                    <div style="display:flex; gap:6px;">
                        <button class="btn btn-primary" onclick="loadArchiveIntoStudio()">✏️ Edit in Studio</button>
                        <button class="btn btn-outline" onclick="copyArchiveSubject()">Copy Subject</button>
                        <button class="btn btn-success" onclick="copyArchiveHTML()">Copy HTML</button>
                    </div>
                </div>
                <div class="stage-canvas">
                    <div class="preview-wrapper" style="max-width:640px;">
                        <iframe id="archive-live-iframe" class="live-preview-iframe"></iframe>
                    </div>
                </div>
            </div>
        </section>

        <!-- ═══════════════════════════════════════════════════════
             VIEW 3: CAMPUS BRAND SHELL
        ═══════════════════════════════════════════════════════ -->
        <section id="view-shell" class="app-view">
            <div class="shell-config-panel">
                <div class="shell-group-card">
                    <div class="shell-group-header">
                        <div class="shell-group-title">
                            <span>🏫</span> Campus Brand Profile &amp; Sync
                        </div>
                        <div style="display:flex; gap:6px;">
                            <button type="button" class="btn btn-outline" style="font-size:0.67rem; padding:2px 8px;" onclick="exportBrandKitJson()" title="Export brand settings as JSON">💾 Export</button>
                            <label class="btn btn-outline" style="font-size:0.67rem; padding:2px 8px; cursor:pointer; margin:0;" title="Import brand settings from JSON">
                                📂 Import
                                <input type="file" id="inp-brand-file" accept=".json" style="display:none;" onchange="importBrandKitJson(event)">
                            </label>
                        </div>
                    </div>
                    <div class="form-group" style="margin-bottom:8px;">
                        <label class="form-label">Active Brand Profile</label>
                        <select class="form-select" id="shell-campus-select" onchange="applyCampusPreset(this.value)">
                            <option value="Simply Admission">Simply Admission (Default)</option>
                        </select>
                    </div>
                    <div style="font-size:0.68rem; color:var(--text-dim); line-height:1.4;">
                        Brand styles apply globally across all 22 admission alert scenarios and Studio previews.
                    </div>
                </div>

                <div class="shell-group-card">
                    <div class="shell-group-header">
                        <div class="shell-group-title">
                            <span>🎨</span> Visual Identity &amp; Logo
                        </div>
                    </div>
                    <div class="form-group">
                        <label class="form-label">School / Institution Name</label>
                        <input type="text" class="form-input" id="inp-campus-name" value="Simply Admission" oninput="rebuildPreview(); updateShellPreview();">
                    </div>
                    <div class="form-group">
                        <label class="form-label">Logo Image URL (Direct PNG/SVG)</label>
                        <input type="text" class="form-input" id="inp-logo-link" value="https://resources.edunexttechnologies.com/web-data/simplyadmission/img/Simpli_Admission-logo.png" oninput="rebuildPreview(); updateShellPreview();">
                    </div>
                    <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">
                        <div class="form-group">
                            <label class="form-label">Logo Max Height (<span id="shell-logo-size-val">48px</span>)</label>
                            <input type="range" min="28" max="80" step="2" value="48" id="inp-logo-size" oninput="document.getElementById('shell-logo-size-val').textContent = this.value + 'px'; rebuildPreview(); updateShellPreview();" style="width:100%; accent-color:var(--primary);">
                        </div>
                        <div class="form-group">
                            <label class="form-label">Logo Alignment</label>
                            <select class="form-select" id="inp-logo-align" onchange="currentLogoAlign = this.value; rebuildPreview(); updateShellPreview();">
                                <option value="center">Center Aligned</option>
                                <option value="left">Left Aligned</option>
                            </select>
                        </div>
                    </div>
                </div>

                <div class="shell-group-card">
                    <div class="shell-group-header">
                        <div class="shell-group-title">
                            <span>🌈</span> Synchronized Color Palette &amp; WCAG Meter
                        </div>
                    </div>
                    <div class="form-group">
                        <div style="display:flex; justify-content:space-between; align-items:center;">
                            <label class="form-label">12 Coordinated Brand Themes</label>
                            <div class="contrast-meter-badge pass" id="wcag-contrast-badge">WCAG AAA (10.4:1)</div>
                        </div>
                        <div class="swatch-group" style="display:grid; grid-template-columns: repeat(6, 1fr); gap:6px; margin: 6px 0 10px;">
                            <button type="button" class="swatch-btn" style="background:#2563eb; width:100%; height:26px; border-radius:4px;" title="Simply Blue" onclick="applyBrandPreset(0)"></button>
                            <button type="button" class="swatch-btn" style="background:#059669; width:100%; height:26px; border-radius:4px;" title="Emerald Luxe" onclick="applyBrandPreset(1)"></button>
                            <button type="button" class="swatch-btn" style="background:#991b1b; width:100%; height:26px; border-radius:4px;" title="Classic Crimson" onclick="applyBrandPreset(2)"></button>
                            <button type="button" class="swatch-btn" style="background:#4f46e5; width:100%; height:26px; border-radius:4px;" title="Royal Indigo" onclick="applyBrandPreset(3)"></button>
                            <button type="button" class="swatch-btn" style="background:#d97706; width:100%; height:26px; border-radius:4px;" title="Sunset Amber" onclick="applyBrandPreset(4)"></button>
                            <button type="button" class="swatch-btn" style="background:#0f172a; width:100%; height:26px; border-radius:4px;" title="Slate Noir" onclick="applyBrandPreset(5)"></button>
                            <button type="button" class="swatch-btn" style="background:#0d9488; width:100%; height:26px; border-radius:4px;" title="Nordic Teal" onclick="applyBrandPreset(6)"></button>
                            <button type="button" class="swatch-btn" style="background:#38bdf8; width:100%; height:26px; border-radius:4px;" title="Midnight Obsidian" onclick="applyBrandPreset(7)"></button>
                            <button type="button" class="swatch-btn" style="background:#7c3aed; width:100%; height:26px; border-radius:4px;" title="Amethyst Purple" onclick="applyBrandPreset(8)"></button>
                            <button type="button" class="swatch-btn" style="background:#e11d48; width:100%; height:26px; border-radius:4px;" title="Coral Blossom" onclick="applyBrandPreset(9)"></button>
                            <button type="button" class="swatch-btn" style="background:#854d0e; width:100%; height:26px; border-radius:4px;" title="Cyber Bronze" onclick="applyBrandPreset(10)"></button>
                            <button type="button" class="swatch-btn" style="background:#475569; width:100%; height:26px; border-radius:4px;" title="Titanium Tech" onclick="applyBrandPreset(11)"></button>
                        </div>
                    </div>
                    <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">
                        <div class="form-group">
                            <label class="form-label">Primary Brand Accent</label>
                            <input type="color" id="inp-theme-color" value="#2563eb" onchange="onThemeColorChange(this.value)" style="width:100%; height:32px; border-radius:4px; border:1px solid var(--border-subtle); background:none; cursor:pointer;">
                        </div>
                        <div class="form-group">
                            <label class="form-label">Secondary Accent</label>
                            <input type="color" id="inp-secondary-color" value="#3b82f6" onchange="rebuildPreview(); updateShellPreview();" style="width:100%; height:32px; border-radius:4px; border:1px solid var(--border-subtle); background:none; cursor:pointer;">
                        </div>
                    </div>
                    <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">
                        <div class="form-group">
                            <label class="form-label">Outer Canvas Tint</label>
                            <input type="text" class="form-input" id="inp-bg-color" value="#f1f5f9" oninput="rebuildPreview(); updateShellPreview();">
                        </div>
                        <div class="form-group">
                            <label class="form-label">Email Card Background</label>
                            <input type="text" class="form-input" id="inp-card-bg-color" value="#ffffff" oninput="rebuildPreview(); updateShellPreview();">
                        </div>
                    </div>
                    <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">
                        <div class="form-group">
                            <label class="form-label">Headline Font Color</label>
                            <input type="color" id="inp-headline-color" value="#1e3a8a" onchange="rebuildPreview(); updateShellPreview();" style="width:100%; height:32px; border-radius:4px; border:1px solid var(--border-subtle); background:none; cursor:pointer;">
                        </div>
                        <div class="form-group">
                            <label class="form-label">Body Text Font Color</label>
                            <input type="color" id="inp-text-color" value="#334155" onchange="rebuildPreview(); updateShellPreview();" style="width:100%; height:32px; border-radius:4px; border:1px solid var(--border-subtle); background:none; cursor:pointer;">
                        </div>
                    </div>
                    <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">
                        <div class="form-group">
                            <label class="form-label">Highlight &amp; Badge Tint</label>
                            <input type="text" class="form-input" id="inp-highlight-color" value="#eff6ff" oninput="rebuildPreview(); updateShellPreview();">
                        </div>
                        <div class="form-group">
                            <label class="form-label">Button Text Color</label>
                            <input type="color" id="inp-btn-text-color" value="#ffffff" onchange="rebuildPreview(); updateShellPreview(); updateWcagContrast();" style="width:100%; height:32px; border-radius:4px; border:1px solid var(--border-subtle); background:none; cursor:pointer;">
                        </div>
                    </div>
                    <div class="form-group" style="margin-top:6px;">
                        <label class="form-label">Button Curvature</label>
                        <div style="display:flex; gap:6px;">
                            <button type="button" class="btn btn-outline" style="flex:1; font-size:0.68rem; padding:4px;" onclick="setBtnRadiusPreset('0px')">Sharp (0px)</button>
                            <button type="button" class="btn btn-outline" style="flex:1; font-size:0.68rem; padding:4px;" onclick="setBtnRadiusPreset('4px')">Subtle (4px)</button>
                            <button type="button" class="btn btn-outline" style="flex:1; font-size:0.68rem; padding:4px;" onclick="setBtnRadiusPreset('8px')">Soft (8px)</button>
                            <button type="button" class="btn btn-outline" style="flex:1; font-size:0.68rem; padding:4px;" onclick="setBtnRadiusPreset('9999px')">Pill</button>
                        </div>
                        <input type="hidden" id="inp-btn-radius" value="6px">
                    </div>
                </div>

                <div class="shell-group-card">
                    <div class="shell-group-header">
                        <div class="shell-group-title">
                            <span>📞</span> Admissions Helpline &amp; Campus Office
                        </div>
                    </div>
                    <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">
                        <div class="form-group">
                            <label class="form-label">Admissions Phone</label>
                            <input type="text" class="form-input" id="inp-campus-phone" value="+91 98765 43210" placeholder="+91..." oninput="rebuildPreview(); updateShellPreview();">
                        </div>
                        <div class="form-group">
                            <label class="form-label">Admissions Email</label>
                            <input type="text" class="form-input" id="inp-campus-email" value="admissions@simplyadmission.com" placeholder="admissions@..." oninput="rebuildPreview(); updateShellPreview();">
                        </div>
                    </div>
                    <div class="form-group">
                        <label class="form-label">Campus Physical Address</label>
                        <input type="text" class="form-input" id="inp-campus-address" value="Sector 68, Noida, Uttar Pradesh 201301" placeholder="Campus location..." oninput="rebuildPreview(); updateShellPreview();">
                    </div>
                    <div class="form-group">
                        <label class="form-label">Office Working Hours</label>
                        <input type="text" class="form-input" id="inp-campus-timings" value="Mon - Sat: 9:00 AM - 4:30 PM" placeholder="Office timings..." oninput="rebuildPreview(); updateShellPreview();">
                    </div>
                </div>

                <div class="shell-group-card">
                    <div class="shell-group-header">
                        <div class="shell-group-title">
                            <span>🌐</span> Verified Public Channels &amp; CDN Icons
                        </div>
                    </div>
                    <div class="form-group">
                        <label class="form-label">Official Website URL</label>
                        <input type="text" class="form-input" id="inp-website-url" value="http://simplyadmission.com" oninput="rebuildPreview(); updateShellPreview();">
                    </div>
                    <div class="form-group">
                        <label class="form-label">Google Maps Location Link</label>
                        <input type="text" class="form-input" id="inp-location-link" value="https://www.google.com/maps/search/Simply+Admission,+Noida+Sector+68" oninput="rebuildPreview(); updateShellPreview();">
                    </div>
                    <div class="form-group">
                        <label class="form-label">Candidate Portal Login URL</label>
                        <input type="text" class="form-input" id="inp-portal-url" value="{{{{school_url}}}}" oninput="rebuildPreview(); updateShellPreview();">
                    </div>
                    <div class="form-group">
                        <label class="form-label">WhatsApp Admissions Helpline Link</label>
                        <input type="text" class="form-input" id="inp-soc-wa" value="https://wa.me/919876543210" placeholder="https://wa.me/..." oninput="rebuildPreview(); updateShellPreview();">
                    </div>
                    <div style="font-size:0.72rem; font-weight:700; color:var(--text-secondary); margin:10px 0 6px;">Social Channels (Verified CDN Icons in Footer)</div>
                    <input type="text" class="form-input" id="inp-soc-fb" value="https://www.facebook.com/simplyadmission" placeholder="Facebook URL" oninput="rebuildPreview(); updateShellPreview();" style="margin-bottom:6px;">
                    <input type="text" class="form-input" id="inp-soc-insta" value="https://www.instagram.com/simply_admission/" placeholder="Instagram URL" oninput="rebuildPreview(); updateShellPreview();" style="margin-bottom:6px;">
                    <input type="text" class="form-input" id="inp-soc-twitter" value="https://twitter.com/AdmissionSimply" placeholder="Twitter URL" oninput="rebuildPreview(); updateShellPreview();" style="margin-bottom:6px;">
                    <input type="text" class="form-input" id="inp-soc-linkedin" value="https://www.linkedin.com/company/simplyadmission/?viewAsMember=true" placeholder="LinkedIn URL" oninput="rebuildPreview(); updateShellPreview();" style="margin-bottom:6px;">
                    <input type="text" class="form-input" id="inp-soc-yt" value="" placeholder="YouTube URL" oninput="rebuildPreview(); updateShellPreview();">
                </div>
            </div>

            <div class="studio-stage">
                <div class="stage-toolbar">
                    <span style="font-size:0.8rem; font-weight:700;">Campus Brand Shell Live Preview</span>
                    <button class="btn btn-primary" onclick="switchView('studio')">Open in Studio &rarr;</button>
                </div>
                <div class="stage-canvas">
                    <div class="preview-wrapper" style="max-width:640px;">
                        <iframe id="shell-live-iframe" class="live-preview-iframe" title="Brand Shell Preview"></iframe>
                    </div>
                </div>
            </div>
        </section>

        <!-- ═══════════════════════════════════════════════════════
             VIEW 4: AI ADMISSION CAMPAIGN BUILDER
        ═══════════════════════════════════════════════════════ -->
        <section id="view-ai" class="app-view">
            <div class="ai-sidebar">
                <div>
                    <h3 style="font-size:0.92rem; font-weight:700; margin-bottom:4px;">✨ AI Admission Campaign Generator</h3>
                    <div style="font-size:0.72rem; color:var(--text-secondary);">Synthesizes conversion-focused, client-proof copy across 7 canonical admission stages.</div>
                </div>

                <div class="shell-group-card">
                    <div class="shell-group-header">
                        <div class="shell-group-title">
                            <span>🎯</span> 1. Select Admission Funnel Stage
                        </div>
                    </div>
                    <div class="ai-funnel-pills">
                        <button type="button" class="ai-funnel-pill" id="ai-stage-open_house" onclick="selectAiFunnelStage('open_house')">
                            <span class="ai-funnel-num">1</span>
                            <div>
                                <div style="font-weight:600;">Open House &amp; Campus Tour</div>
                                <div style="font-size:0.66rem; color:var(--text-dim);">Early prospect engagement &amp; visit booking</div>
                            </div>
                        </button>
                        <button type="button" class="ai-funnel-pill active" id="ai-stage-incomplete_form" onclick="selectAiFunnelStage('incomplete_form')">
                            <span class="ai-funnel-num">2</span>
                            <div>
                                <div style="font-weight:600;">Incomplete Form Reminder</div>
                                <div style="font-size:0.66rem; color:var(--text-dim);">Nudge registered parents to submit details</div>
                            </div>
                        </button>
                        <button type="button" class="ai-funnel-pill" id="ai-stage-slot_booking" onclick="selectAiFunnelStage('slot_booking')">
                            <span class="ai-funnel-num">3</span>
                            <div>
                                <div style="font-weight:600;">Entrance Assessment / Slot Booking</div>
                                <div style="font-size:0.66rem; color:var(--text-dim);">Interaction schedule &amp; slot selection</div>
                            </div>
                        </button>
                        <button type="button" class="ai-funnel-pill" id="ai-stage-provisional_offer" onclick="selectAiFunnelStage('provisional_offer')">
                            <span class="ai-funnel-num">4</span>
                            <div>
                                <div style="font-weight:600;">Provisional Offer of Admission</div>
                                <div style="font-size:0.66rem; color:var(--text-dim);">Congratulatory selection letter</div>
                            </div>
                        </button>
                        <button type="button" class="ai-funnel-pill" id="ai-stage-fee_deadline" onclick="selectAiFunnelStage('fee_deadline')">
                            <span class="ai-funnel-num">5</span>
                            <div>
                                <div style="font-weight:600;">Admission Fee Deadline Reminder</div>
                                <div style="font-size:0.66rem; color:var(--text-dim);">Seat reservation fee expiry alert</div>
                            </div>
                        </button>
                        <button type="button" class="ai-funnel-pill" id="ai-stage-doc_verification" onclick="selectAiFunnelStage('doc_verification')">
                            <span class="ai-funnel-num">6</span>
                            <div>
                                <div style="font-weight:600;">Mandatory Document Verification</div>
                                <div style="font-size:0.66rem; color:var(--text-dim);">TC, Birth Certificate, Immunisation checklist</div>
                            </div>
                        </button>
                        <button type="button" class="ai-funnel-pill" id="ai-stage-orientation" onclick="selectAiFunnelStage('orientation')">
                            <span class="ai-funnel-num">7</span>
                            <div>
                                <div style="font-weight:600;">Student Induction &amp; Orientation Day</div>
                                <div style="font-size:0.66rem; color:var(--text-dim);">Welcome event schedule &amp; student onboarding</div>
                            </div>
                        </button>
                    </div>

                    <div style="margin-top:10px;">
                        <span style="font-size:0.68rem; font-weight:700; color:var(--text-secondary); display:block; margin-bottom:4px;">1-Click Inspiration Presets:</span>
                        <div class="ai-chips-wrap">
                            <span class="ai-preset-chip" onclick="applyAiInspirationChip('Open House Walkthrough Invitation', 'open_house')">🏫 Open House Walkthrough</span>
                            <span class="ai-preset-chip" onclick="applyAiInspirationChip('Incomplete Registration Due in 48 Hours', 'incomplete_form')">⏳ Form Due in 48h</span>
                            <span class="ai-preset-chip" onclick="applyAiInspirationChip('Select Interaction Slot for Grade 1', 'slot_booking')">📅 Interaction Slot</span>
                            <span class="ai-preset-chip" onclick="applyAiInspirationChip('Official Admission Offer Letter Issued', 'provisional_offer')">🎉 Offer Letter</span>
                            <span class="ai-preset-chip" onclick="applyAiInspirationChip('Final Seat Confirmation Fee Due Tomorrow', 'fee_deadline')">⚠️ Fee Expiry</span>
                            <span class="ai-preset-chip" onclick="applyAiInspirationChip('Missing Birth Certificate & Transfer Certificate', 'doc_verification')">📄 Pending Docs</span>
                        </div>
                    </div>
                </div>

                <div class="shell-group-card">
                    <div class="shell-group-header">
                        <div class="shell-group-title">
                            <span>⚙️</span> 2. Audience &amp; Delivery Modifiers
                        </div>
                    </div>
                    <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">
                        <div class="form-group">
                            <label class="form-label">Target Audience</label>
                            <select class="form-select" id="ai-audience">
                                <option value="parents">Prospective Parents</option>
                                <option value="candidate">Candidate Direct</option>
                                <option value="siblings">Sibling Parents</option>
                                <option value="referral">Referral / Alumni</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <label class="form-label">Communication Tone</label>
                            <select class="form-select" id="ai-tone">
                                <option value="warm">Warm &amp; Reassuring</option>
                                <option value="formal">Formal &amp; Institutional</option>
                                <option value="urgent">Urgent &amp; Time-Sensitive</option>
                                <option value="celebratory">Celebratory &amp; Welcoming</option>
                            </select>
                        </div>
                    </div>

                    <div style="margin-top:8px;">
                        <label class="form-label">Modular Structural Blocks</label>
                        <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px; font-size:0.72rem;">
                            <label style="display:flex; align-items:center; gap:6px; cursor:pointer;">
                                <input type="checkbox" id="ai-chk-notice" checked> Notice Banner
                            </label>
                            <label style="display:flex; align-items:center; gap:6px; cursor:pointer;">
                                <input type="checkbox" id="ai-chk-roadmap" checked> 3-Step Roadmap
                            </label>
                            <label style="display:flex; align-items:center; gap:6px; cursor:pointer;">
                                <input type="checkbox" id="ai-chk-login" checked> Portal Login Card
                            </label>
                            <label style="display:flex; align-items:center; gap:6px; cursor:pointer;">
                                <input type="checkbox" id="ai-chk-cta" checked> Primary CTA Button
                            </label>
                        </div>
                    </div>

                    <div class="form-group" style="margin-top:10px;">
                        <label class="form-label">Custom Campaign Directive / Notes (Optional)</label>
                        <textarea class="form-textarea" id="ai-prompt" rows="2" placeholder="e.g. Highlight that only 12 seats remain for Grade 1 and the assessment portal closes Friday at 5 PM."></textarea>
                    </div>

                    <button type="button" class="btn btn-primary" style="width:100%; justify-content:center; padding:10px; font-weight:700; margin-top:8px;" onclick="runAiGenerator()">
                        ✨ Synthesize Campaign Template
                    </button>
                </div>
            </div>

            <div class="studio-stage">
                <div class="stage-toolbar">
                    <div style="display:flex; align-items:center; gap:8px;">
                        <span style="font-size:0.8rem; font-weight:700;">Generated Output:</span>
                        <span id="ai-stage-badge" class="hub-launch-tag">Incomplete Form Reminder</span>
                    </div>
                    <div style="display:flex; gap:8px;">
                        <button class="btn btn-primary" onclick="loadAiIntoStudio()">✏️ Edit in Studio</button>
                        <button class="btn btn-success" onclick="copyAiHTML()">Copy HTML</button>
                    </div>
                </div>
                <div class="stage-canvas">
                    <div class="preview-wrapper" style="max-width:640px;">
                        <iframe id="ai-live-iframe" class="live-preview-iframe" title="AI Generated Preview"></iframe>
                    </div>
                </div>
            </div>
        </section>

        <!-- ═══════════════════════════════════════════════════════
             VIEW 5: HUB OVERVIEW & DELIVERY METRICS
        ═══════════════════════════════════════════════════════ -->
        <section id="view-home" class="app-view">
            <div class="home-container">
                <div class="home-hero">
                    <span class="home-hero-badge">ENTERPRISE ADMISSION COMMUNICATIONS</span>
                    <h1>Admission Campaign &amp; Delivery Hub</h1>
                    <p>Production-grade email infrastructure engineered for school admissions. Tested across 50+ email clients with zero-dependency rendering, ghost tables, and verified CDN iconography.</p>
                </div>

                <!-- 4 High-Impact Delivery Health Metrics -->
                <div class="hub-metrics-grid">
                    <div class="hub-metric-card">
                        <div class="hub-metric-num">22 <span>Scenarios</span></div>
                        <div class="hub-metric-label">Canonical Admission Alerts</div>
                        <div class="hub-metric-sub">Complete lifecycle coverage from initial enquiry to induction.</div>
                    </div>
                    <div class="hub-metric-card">
                        <div class="hub-metric-num">68 <span>Variables</span></div>
                        <div class="hub-metric-label">Enterprise CRM Merge Tags</div>
                        <div class="hub-metric-sub">Full mapping for LeadSquared, Meritto, SFDC EDA &amp; HubSpot.</div>
                    </div>
                    <div class="hub-metric-card">
                        <div class="hub-metric-num">99.8% <span>Proofed</span></div>
                        <div class="hub-metric-label">Cross-Client Compatibility</div>
                        <div class="hub-metric-sub">Outlook 2016-365 Ghost Tables, iOS Mail, Gmail, &amp; Yahoo.</div>
                    </div>
                    <div class="hub-metric-card">
                        <div class="hub-metric-num">0 <span>Latency</span></div>
                        <div class="hub-metric-label">External Image Dependencies</div>
                        <div class="hub-metric-sub">Pure CSS layouts with 100% verified CDN iconography.</div>
                    </div>
                </div>

                <!-- Quick Launchpad for Top 6 Alert Scenarios -->
                <div class="hub-section-card">
                    <div class="hub-section-header">
                        <div class="hub-section-title">
                            <span>🚀</span> High-Frequency Alert Quick Launchpad
                        </div>
                        <span style="font-size:0.72rem; color:var(--text-dim);">Jump directly into Studio Composer</span>
                    </div>
                    <div class="hub-launchpad-grid">
                        <div class="hub-launch-btn" onclick="launchHubScenario('01_mobile_no_verification_otp')">
                            <div>
                                <div class="hub-launch-title">01. Mobile Verification OTP</div>
                                <div class="hub-launch-sub">Two-factor auth &amp; registration validation</div>
                            </div>
                            <span class="hub-launch-tag">Instant Auth</span>
                        </div>
                        <div class="hub-launch-btn" onclick="launchHubScenario('02_enquiry_acknowledgement')">
                            <div>
                                <div class="hub-launch-title">02. Enquiry Acknowledgement</div>
                                <div class="hub-launch-sub">First-touch prospect engagement &amp; brochure</div>
                            </div>
                            <span class="hub-launch-tag">Lead Intake</span>
                        </div>
                        <div class="hub-launch-btn" onclick="launchHubScenario('06_registration_fee_payment_reminder')">
                            <div>
                                <div class="hub-launch-title">06. Registration Fee Reminder</div>
                                <div class="hub-launch-sub">Application fee nudge with portal credentials</div>
                            </div>
                            <span class="hub-launch-tag">Conversion</span>
                        </div>
                        <div class="hub-launch-btn" onclick="launchHubScenario('09_campus_tour_invitation_confirmation')">
                            <div>
                                <div class="hub-launch-title">09. Campus Tour Confirmation</div>
                                <div class="hub-launch-sub">Open house booking &amp; navigation directions</div>
                            </div>
                            <span class="hub-launch-tag">Experience</span>
                        </div>
                        <div class="hub-launch-btn" onclick="launchHubScenario('12_fee_payment_successful')">
                            <div>
                                <div class="hub-launch-title">12. Fee Payment Receipt</div>
                                <div class="hub-launch-sub">Official payment confirmation &amp; receipt head</div>
                            </div>
                            <span class="hub-launch-tag">Finance</span>
                        </div>
                        <div class="hub-launch-btn" onclick="launchHubScenario('14_admission_offer_letter')">
                            <div>
                                <div class="hub-launch-title">14. Admission Offer Letter</div>
                                <div class="hub-launch-sub">Provisional seat grant &amp; enrollment deadline</div>
                            </div>
                            <span class="hub-launch-tag">Offer Granted</span>
                        </div>
                    </div>
                </div>

                <!-- Cross-Platform CRM Field Mapping Reference -->
                <div class="hub-section-card">
                    <div class="hub-section-header">
                        <div class="hub-section-title">
                            <span>🔄</span> Cross-Platform CRM Merge Field Reference
                        </div>
                        <span style="font-size:0.72rem; color:var(--text-dim);">Click any tag to copy to clipboard</span>
                    </div>
                    <div style="overflow-x:auto;">
                        <table class="hub-crm-table">
                            <thead>
                                <tr>
                                    <th>Standard Variable</th>
                                    <th>LeadSquared</th>
                                    <th>Meritto / NoPaperForms</th>
                                    <th>Salesforce EDA</th>
                                    <th>HubSpot</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td><span class="hub-copy-pill" onclick="copyText('{{{{student_name}}}}')">{{{{student_name}}}}</span></td>
                                    <td><code>{{{{Lead.FirstName}}}}</code></td>
                                    <td><code>[STUDENT_NAME]</code></td>
                                    <td><code>{{!Contact.FirstName}}</code></td>
                                    <td><code>{{{{ contact.firstname }}}}</code></td>
                                </tr>
                                <tr>
                                    <td><span class="hub-copy-pill" onclick="copyText('{{{{student_class}}}}')">{{{{student_class}}}}</span></td>
                                    <td><code>{{{{Lead.mx_Grade_Applying}}}}</code></td>
                                    <td><code>[COURSE_APPLIED]</code></td>
                                    <td><code>{{!Opportunity.Grade__c}}</code></td>
                                    <td><code>{{{{ contact.grade_applying }}}}</code></td>
                                </tr>
                                <tr>
                                    <td><span class="hub-copy-pill" onclick="copyText('{{{{father_name}}}}')">{{{{father_name}}}}</span></td>
                                    <td><code>{{{{Lead.mx_Father_Name}}}}</code></td>
                                    <td><code>[FATHER_NAME]</code></td>
                                    <td><code>{{!Account.Parent_Name__c}}</code></td>
                                    <td><code>{{{{ contact.parent_name }}}}</code></td>
                                </tr>
                                <tr>
                                    <td><span class="hub-copy-pill" onclick="copyText('{{{{application_no}}}}')">{{{{application_no}}}}</span></td>
                                    <td><code>{{{{Lead.mx_Application_No}}}}</code></td>
                                    <td><code>[APPLICATION_NUMBER]</code></td>
                                    <td><code>{{!Lead.App_Number__c}}</code></td>
                                    <td><code>{{{{ contact.application_number }}}}</code></td>
                                </tr>
                                <tr>
                                    <td><span class="hub-copy-pill" onclick="copyText('{{{{current_fee_receipt_amount}}}}')">{{{{current_fee_receipt_amount}}}}</span></td>
                                    <td><code>{{{{Lead.mx_Fee_Paid}}}}</code></td>
                                    <td><code>[FEE_AMOUNT]</code></td>
                                    <td><code>{{!Opportunity.Amount}}</code></td>
                                    <td><code>{{{{ deal.amount }}}}</code></td>
                                </tr>
                                <tr>
                                    <td><span class="hub-copy-pill" onclick="copyText('{{{{school_url}}}}')">{{{{school_url}}}}</span></td>
                                    <td><code>{{{{Lead.mx_Portal_URL}}}}</code></td>
                                    <td><code>[PORTAL_URL]</code></td>
                                    <td><code>{{!Account.Website}}</code></td>
                                    <td><code>{{{{ company.domain }}}}</code></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- Institutional Delivery Standards Card -->
                <div class="hub-section-card">
                    <div class="hub-section-header">
                        <div class="hub-section-title">
                            <span>🛡️</span> Institutional Delivery Standards &amp; Architecture
                        </div>
                    </div>
                    <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr)); gap:12px; font-size:0.75rem; color:var(--text-secondary); line-height:1.5;">
                        <div style="background:var(--bg-surface); padding:12px; border-radius:6px; border:1px solid var(--border-subtle);">
                            <div style="font-weight:700; color:var(--text-primary); margin-bottom:4px;">Strict Zero Marketing Fluff</div>
                            Zero legal disclaimers, promotional footer bloat, or irrelevant institutional history. Pure transactional focus.
                        </div>
                        <div style="background:var(--bg-surface); padding:12px; border-radius:6px; border:1px solid var(--border-subtle);">
                            <div style="font-weight:700; color:var(--text-primary); margin-bottom:4px;">Verified CDN Iconography</div>
                            Social channels, Google Maps, and Website icons rendered exclusively via reliable CDN endpoints with alt tags.
                        </div>
                        <div style="background:var(--bg-surface); padding:12px; border-radius:6px; border:1px solid var(--border-subtle);">
                            <div style="font-weight:700; color:var(--text-primary); margin-bottom:4px;">MSO Ghost Table Engine</div>
                            Pure table nesting with fixed widths and Outlook conditional statements ensuring pixel-perfect desktop alignment.
                        </div>
                        <div style="background:var(--bg-surface); padding:12px; border-radius:6px; border:1px solid var(--border-subtle);">
                            <div style="font-weight:700; color:var(--text-primary); margin-bottom:4px;">WCAG 2.1 AA Contrast Ratio</div>
                            Color hierarchy dynamically checked for 4.5:1+ contrast against white backgrounds for optimal parent readability.
                        </div>
                    </div>
                </div>

                <!-- Core Navigation Cards -->
                <div class="home-cards-grid">
                    <div class="home-card" onclick="switchView('studio')">
                        <div>
                            <span style="font-size:1.4rem;">🎨</span>
                            <div class="home-card-title">Template Studio</div>
                            <div class="home-card-desc">Compose and customize all 22 admission alert scenarios with 68 CRM merge tags and dual-mode live preview.</div>
                        </div>
                        <button class="btn btn-primary">Open Studio &rarr;</button>
                    </div>
                    <div class="home-card" onclick="switchView('archive')">
                        <div>
                            <span style="font-size:1.4rem;">📁</span>
                            <div class="home-card-title">Template Library</div>
                            <div class="home-card-desc">Browse pre-approved production templates across all connected school campuses and sample suites.</div>
                        </div>
                        <button class="btn btn-outline">Explore Library &rarr;</button>
                    </div>
                    <div class="home-card" onclick="switchView('shell')">
                        <div>
                            <span style="font-size:1.4rem;">🏫</span>
                            <div class="home-card-title">Campus Brand Kit</div>
                            <div class="home-card-desc">Set school logo, color hierarchy, WCAG contrast, admissions helpline, and verified CDN icons.</div>
                        </div>
                        <button class="btn btn-outline">Configure Brand &rarr;</button>
                    </div>
                    <div class="home-card" onclick="switchView('ai')">
                        <div>
                            <span style="font-size:1.4rem;">✨</span>
                            <div class="home-card-title">AI Campaign Generator</div>
                            <div class="home-card-desc">Generate tailored email alerts dynamically matching your campus styling, funnel stage, and tone.</div>
                        </div>
                        <button class="btn btn-outline">Launch AI &rarr;</button>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <!-- ───── Code Viewer Modal ───── -->
    <div class="modal-overlay" id="code-modal">
        <div class="modal-box">
            <div class="modal-header">
                <span style="font-size:0.84rem; font-weight:700;">Generated Email HTML (Email-Client Proof)</span>
                <button type="button" style="background:none; border:none; color:var(--text-secondary); cursor:pointer; font-size:1rem;" onclick="closeCodeModal()">✕</button>
            </div>
            <div class="modal-body">
                <div class="code-box" id="modal-code-content"></div>
            </div>
            <div style="padding:10px 18px; border-top:1px solid var(--border-subtle); background:var(--bg-surface); display:flex; justify-content:flex-end; gap:8px;">
                <button class="btn btn-outline" onclick="closeCodeModal()">Close</button>
                <button class="btn btn-success" onclick="copyHTML(); closeCodeModal();">Copy Code</button>
            </div>
        </div>
    </div>

    <!-- ───── Command Palette Modal (Ctrl+K) ───── -->
    <div class="modal-overlay" id="cmd-modal">
        <div class="modal-box" style="max-width:540px;">
            <input type="text" class="cmd-search-input" id="cmd-search-inp" placeholder="Type a scenario, action, or variable..." oninput="onCmdSearch(this.value)">
            <div class="cmd-results-list" id="cmd-results-list"></div>
        </div>
    </div>

    <!-- ───── Interactive Guided Tutorial / Tour Modal ───── -->
    <div class="tutorial-overlay" id="tutorial-modal">
        <div class="tutorial-card">
            <div class="tutorial-header">
                <span style="font-weight:700; font-size:0.92rem; color:#f8fafc;" id="tut-title">🎓 Welcome to Email Template Designer</span>
                <button type="button" style="background:none; border:none; color:var(--text-secondary); cursor:pointer; font-size:1.1rem;" onclick="closeTutorial()">✕</button>
            </div>
            <div class="tutorial-body" id="tut-content">
                <!-- Dynamically rendered step -->
            </div>
            <div class="tutorial-footer">
                <div style="font-size:0.75rem; color:var(--text-dim);" id="tut-step-counter">Step 1 of 5</div>
                <div style="display:flex; gap:6px;">
                    <button type="button" class="btn btn-outline" id="tut-btn-prev" onclick="prevTutorialStep()">Back</button>
                    <button type="button" class="btn btn-primary" id="tut-btn-next" onclick="nextTutorialStep()">Next →</button>
                </div>
            </div>
        </div>
    </div>

    <!-- ───── Keyboard Shortcuts Modal (?) ───── -->
    <div class="modal-overlay" id="shortcuts-modal">
        <div class="modal-box" style="max-width:500px;">
            <div class="modal-header">
                <span>⌨️ Keyboard Shortcuts &amp; Power Tools</span>
                <button type="button" style="background:none; border:none; color:var(--text-secondary); cursor:pointer; font-size:1rem;" onclick="closeShortcutsModal()">✕</button>
            </div>
            <div class="modal-body" style="padding:16px;">
                <div style="display:grid; grid-template-columns: 1fr 1fr; gap:8px;">
                    <div style="background:var(--bg-input); padding:8px 10px; border-radius:6px; border:1px solid var(--border-subtle);">
                        <div style="font-size:0.68rem; color:var(--text-dim);">Command Palette</div>
                        <div style="font-size:0.8rem; font-weight:700; color:#38bdf8; font-family:monospace;">Ctrl + K / ⌘K</div>
                    </div>
                    <div style="background:var(--bg-input); padding:8px 10px; border-radius:6px; border:1px solid var(--border-subtle);">
                        <div style="font-size:0.68rem; color:var(--text-dim);">Paste to Gmail (Rich Text)</div>
                        <div style="font-size:0.8rem; font-weight:700; color:#38bdf8; font-family:monospace;">Ctrl + Shift + G</div>
                    </div>
                    <div style="background:var(--bg-input); padding:8px 10px; border-radius:6px; border:1px solid var(--border-subtle);">
                        <div style="font-size:0.68rem; color:var(--text-dim);">Cycle Scenarios (Prev / Next)</div>
                        <div style="font-size:0.8rem; font-weight:700; color:#38bdf8; font-family:monospace;">[ and ] keys</div>
                    </div>
                    <div style="background:var(--bg-input); padding:8px 10px; border-radius:6px; border:1px solid var(--border-subtle);">
                        <div style="font-size:0.68rem; color:var(--text-dim);">Copy Production HTML</div>
                        <div style="font-size:0.8rem; font-weight:700; color:#38bdf8; font-family:monospace;">Ctrl + S / ⌘S</div>
                    </div>
                    <div style="background:var(--bg-input); padding:8px 10px; border-radius:6px; border:1px solid var(--border-subtle);">
                        <div style="font-size:0.68rem; color:var(--text-dim);">Undo / Redo Edits</div>
                        <div style="font-size:0.8rem; font-weight:700; color:#38bdf8; font-family:monospace;">Ctrl + Z / Ctrl + Y</div>
                    </div>
                    <div style="background:var(--bg-input); padding:8px 10px; border-radius:6px; border:1px solid var(--border-subtle);">
                        <div style="font-size:0.68rem; color:var(--text-dim);">Fullscreen Zen Canvas</div>
                        <div style="font-size:0.8rem; font-weight:700; color:#38bdf8; font-family:monospace;">Alt + Z</div>
                    </div>
                </div>
            </div>
            <div style="padding:10px 18px; border-top:1px solid var(--border-subtle); background:var(--bg-surface); display:flex; justify-content:flex-end;">
                <button class="btn btn-outline" onclick="closeShortcutsModal()">Close</button>
            </div>
        </div>
    </div>

    <!-- ───── 1-Click Auto-Fix Readiness Modal ───── -->
    <div class="modal-overlay" id="autofix-modal">
        <div class="modal-box" style="max-width:480px;">
            <div class="modal-header">
                <span>🟢 Delivery Readiness Audit &amp; 1-Click Fixes</span>
                <button type="button" style="background:none; border:none; color:var(--text-secondary); cursor:pointer; font-size:1rem;" onclick="closeAutoFixModal()">✕</button>
            </div>
            <div class="modal-body" style="padding:16px;" id="autofix-modal-content">
                <!-- Dynamically populated auto-fix items -->
            </div>
            <div style="padding:10px 18px; border-top:1px solid var(--border-subtle); background:var(--bg-surface); display:flex; justify-content:flex-end;">
                <button class="btn btn-outline" onclick="closeAutoFixModal()">Close</button>
            </div>
        </div>
    </div>

    <!-- Toast Notification -->
    <div class="toast" id="toast">Copied to clipboard</div>

    <!-- ═══════════════════════════════════════════════════════════
         APPLICATION LOGIC (VANILLA JS)
    ═══════════════════════════════════════════════════════════════ -->
    <script>
        const CLIENTS_DATA = {clients_json};
        const CANONICAL_TEMPLATES = {templates_json};
        const CLIENT_CAMPUSES = {campuses_json};
        const CRM_VARIABLES_CATALOG = {crm_vars_json};

        let currentActiveCampus = "Simply Admission";
        let activeArchiveItem = null;
        let crmDrawerOpen = false;
        let currentViewport = "desktop";
        let currentView = "studio";
        let mobileStudioMode = "edit";
        let isDarkSim = false;
        let isLockscreenOpen = false;
        let isOmniOpen = false;
        let currentZoom = 1;
        let currentLogoAlign = 'center';
        let isLiveEditActive = false;
        let currentEditorMode = 'form';
        let designerAccordionOpen = false;
        let undoHistory = [];
        let redoHistory = [];
        let isUndoAction = false;

        // Initialize App
        window.addEventListener('DOMContentLoaded', () => {{
            populateCampusPills();
            populateTemplateDropdown();
            populateCrmDrawer();
            populateArchiveList();
            applyCampusPreset(currentActiveCampus);
            rebuildPreview();

            // Autosave timer (every 3 seconds)
            setInterval(saveToLocalStorage, 3000);
            renderScenarioPaginator();

            // Keyboard Shortcuts
            window.addEventListener('keydown', (e) => {{
                const isInput = ['INPUT', 'TEXTAREA', 'SELECT'].includes(document.activeElement.tagName);
                if ((e.ctrlKey || e.metaKey) && e.key === 's') {{
                    e.preventDefault();
                    copyHTML();
                }}
                if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {{
                    e.preventDefault();
                    openCommandPalette();
                }}
                if ((e.ctrlKey || e.metaKey) && e.shiftKey && e.key.toLowerCase() === 'g') {{
                    e.preventDefault();
                    copyFormattedForGmail();
                }}
                if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'z') {{
                    e.preventDefault();
                    undo();
                }}
                if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'y') {{
                    e.preventDefault();
                    redo();
                }}
                if (!isInput && e.key === '[') {{
                    e.preventDefault();
                    stepTemplate(-1);
                }}
                if (!isInput && e.key === ']') {{
                    e.preventDefault();
                    stepTemplate(1);
                }}
                if (!isInput && e.key === '?') {{
                    e.preventDefault();
                    openShortcutsModal();
                }}
                if (!isInput && (e.altKey && e.key.toLowerCase() === 'z')) {{
                    e.preventDefault();
                    toggleZenMode();
                }}
                if (e.key === 'Escape') {{
                    closeCodeModal();
                    closeCommandPalette();
                    closeShortcutsModal();
                    closeAutoFixModal();
                    closeTutorial();
                    toggleMobileNav(false);
                    toggleMoreActionsDropdown(false);
                    document.body.classList.remove('zen-mode');
                }}
            }});
        }});

        // ───── Horizontal & Vertical Scroll Helpers ─────
        function scrollContainer(containerId, offset) {{
            const el = document.getElementById(containerId);
            if (el) {{
                el.scrollBy({{ left: offset, behavior: 'smooth' }});
            }}
        }}

        // ───── Mobile Navigation Drawer ─────
        function toggleMobileNav(forceState) {{
            const drawer = document.getElementById('mobile-nav-drawer');
            const backdrop = document.getElementById('drawer-backdrop');
            const btn = document.getElementById('btn-hamburger');
            if (!drawer) return;
            const isOpen = (typeof forceState === 'boolean') ? forceState : !drawer.classList.contains('open');
            if (isOpen) {{
                drawer.classList.add('open');
                if (backdrop) backdrop.classList.add('show');
                if (btn) btn.classList.add('active');
            }} else {{
                drawer.classList.remove('open');
                if (backdrop) backdrop.classList.remove('show');
                if (btn) btn.classList.remove('active');
            }}
        }}

        // ───── More Actions Responsive Dropdown ─────
        function toggleMoreActionsDropdown(forceState) {{
            const menu = document.getElementById('more-actions-menu');
            const btn = document.getElementById('btn-more-actions');
            if (!menu) return;
            const isShow = (typeof forceState === 'boolean') ? forceState : !menu.classList.contains('show');
            menu.classList.toggle('show', isShow);
            if (btn) btn.classList.toggle('active', isShow);
        }}

        window.addEventListener('click', (e) => {{
            const wrap = document.getElementById('more-actions-dropdown-wrap');
            if (wrap && !wrap.contains(e.target)) {{
                toggleMoreActionsDropdown(false);
            }}
        }});

        // ───── Collapsible Accordion Sections ─────
        function toggleSection(cardId) {{
            const card = document.getElementById(cardId);
            if (card) {{
                card.classList.toggle('is-collapsed');
            }}
        }}

        function toggleAllSections(expandAll) {{
            document.querySelectorAll('.editor-section-card').forEach(card => {{
                if (expandAll) {{
                    card.classList.remove('is-collapsed');
                }} else {{
                    card.classList.add('is-collapsed');
                }}
            }});
        }}

        // ───── Scenario Paginator Logic ─────
        function renderScenarioPaginator() {{
            const strip = document.getElementById('paginator-strip-container');
            const titleEl = document.getElementById('paginator-scenario-title');
            if (!strip) return;
            strip.innerHTML = '';
            const select = document.getElementById('inp-template-selector');
            const curVal = select ? select.value : (CANONICAL_TEMPLATES[0] ? CANONICAL_TEMPLATES[0].id : '');
            
            let curIdx = CANONICAL_TEMPLATES.findIndex(t => t.id === curVal);
            if (curIdx === -1) curIdx = 0;
            const currentTpl = CANONICAL_TEMPLATES[curIdx] || CANONICAL_TEMPLATES[0];

            if (titleEl && currentTpl) {{
                titleEl.textContent = `Page ${{curIdx + 1}} of ${{CANONICAL_TEMPLATES.length}}: ${{currentTpl.name}}`;
            }}

            CANONICAL_TEMPLATES.forEach((tpl, idx) => {{
                const pill = document.createElement('button');
                pill.type = 'button';
                pill.className = `page-num-pill ${{idx === curIdx ? 'active' : ''}}`;
                pill.textContent = idx + 1;
                pill.title = `${{idx + 1}}. ${{tpl.name}} (${{tpl.category}})`;
                pill.onclick = () => goToScenarioPage(idx);
                strip.appendChild(pill);
            }});

            const activePill = strip.querySelector('.page-num-pill.active');
            if (activePill) {{
                activePill.scrollIntoView({{ behavior: 'smooth', inline: 'nearest', block: 'nearest' }});
            }}
        }}

        function goToScenarioPage(idx) {{
            if (idx < 0 || idx >= CANONICAL_TEMPLATES.length) return;
            const target = CANONICAL_TEMPLATES[idx];
            const select = document.getElementById('inp-template-selector');
            if (select) {{
                select.value = target.id;
                onTemplateSelect(target.id);
            }}
            renderScenarioPaginator();
        }}

        function switchView(viewName) {{
            currentView = viewName;
            document.querySelectorAll('.app-view').forEach(v => v.classList.remove('active'));
            document.querySelectorAll('.top-view-tab').forEach(t => t.classList.remove('active'));

            const targetView = document.getElementById(`view-${{viewName}}`);
            if (targetView) targetView.classList.add('active');

            const targetTab = document.getElementById(`tab-${{viewName}}`);
            if (targetTab) targetTab.classList.add('active');

            if (viewName === 'archive' && !activeArchiveItem) {{
                selectFirstArchiveItem();
            }} else if (viewName === 'shell') {{
                updateShellPreview();
            }} else if (viewName === 'studio') {{
                rebuildPreview();
            }}
        }}

        function setMobileStudioMode(mode) {{
            mobileStudioMode = mode;
            const editPanel = document.getElementById('studio-editor-panel');
            const stagePanel = document.getElementById('studio-stage-panel');
            const btnEdit = document.getElementById('btn-mob-edit');
            const btnPrev = document.getElementById('btn-mob-preview');

            if (mode === 'preview') {{
                editPanel.style.display = 'none';
                stagePanel.style.display = 'flex';
                btnPrev.classList.add('active');
                btnEdit.classList.remove('active');
            }} else {{
                editPanel.style.display = 'flex';
                stagePanel.style.display = 'none';
                btnEdit.classList.add('active');
                btnPrev.classList.remove('active');
            }}
        }}

        function populateCampusPills() {{
            const container = document.getElementById('campus-pills-container');
            if (!container) return;
            const wrap = container.closest('.horizontal-scroll-wrap');
            container.innerHTML = '';
            const keys = Object.keys(CLIENT_CAMPUSES);
            if (keys.length <= 1) {{
                if (wrap) wrap.style.display = 'none';
                return;
            }}
            if (wrap) wrap.style.display = 'flex';
            for (const cName of keys) {{
                const btn = document.createElement('button');
                btn.type = 'button';
                btn.className = `campus-pill-btn ${{cName === currentActiveCampus ? 'active' : ''}}`;
                btn.textContent = cName;
                btn.onclick = () => applyCampusPreset(cName);
                container.appendChild(btn);
            }}
        }}

        function applyCampusPreset(campusKey) {{
            const c = CLIENT_CAMPUSES[campusKey];
            if (!c) return;
            currentActiveCampus = campusKey;
            populateCampusPills();

            const shellSelect = document.getElementById('shell-campus-select');
            if (shellSelect) shellSelect.value = campusKey;

            document.getElementById('inp-campus-name').value = c.campus_name || '';
            document.getElementById('inp-logo-link').value = c.campus_logo_link || '';
            document.getElementById('inp-portal-url').value = c.candidate_login_url || '{{{{school_url}}}}';
            document.getElementById('inp-location-link').value = c.campus_location_link || '';
            document.getElementById('inp-website-url').value = c.website || '';
            document.getElementById('inp-theme-color').value = c.theme_color || '#11a14a';
            document.getElementById('inp-bg-color').value = c.bg_color || '#f4f5f7';

            document.getElementById('inp-soc-fb').value = c.facebook || '';
            document.getElementById('inp-soc-insta').value = c.instagram || '';
            document.getElementById('inp-soc-twitter').value = c.twitter || '';
            document.getElementById('inp-soc-linkedin').value = c.linkedin || '';
            document.getElementById('inp-soc-yt').value = c.youtube || '';

            rebuildPreview();
            updateShellPreview();
            updateWcagContrast();
            showToast(`Preset: ${{campusKey}} applied!`);
        }}

        function setThemeColor(hex) {{
            const el = document.getElementById('inp-theme-color');
            if (el) el.value = hex;
            const mini = document.getElementById('inp-theme-color-mini');
            if (mini) mini.value = hex;
            rebuildPreview();
            updateShellPreview();
            updateWcagContrast();
        }}

        function setOuterBgColor(hex) {{
            const el = document.getElementById('inp-bg-color');
            if (el) el.value = hex;
            const mini = document.getElementById('inp-bg-color-mini');
            if (mini) mini.value = hex;
            rebuildPreview();
            updateShellPreview();
        }}

        function setBodyTextColor(hex) {{
            const el = document.getElementById('inp-text-color');
            if (el) el.value = hex;
            const mini = document.getElementById('inp-text-color-mini');
            if (mini) mini.value = hex;
            rebuildPreview();
            updateShellPreview();
        }}

        function onThemeColorChange(hex) {{
            const mini = document.getElementById('inp-theme-color-mini');
            if (mini) mini.value = hex;
            rebuildPreview();
            updateShellPreview();
            updateWcagContrast();
        }}

        function setBtnRadiusPreset(rad) {{
            const inp = document.getElementById('inp-btn-radius');
            if (inp) inp.value = rad;
            rebuildPreview();
            updateShellPreview();
            showToast(`Button curvature set to ${{rad}}`);
        }}

        // WCAG 2.1 Contrast Calculation Engine
        function getLuminance(hex) {{
            hex = (hex || '#000000').replace('#', '');
            if (hex.length === 3) hex = hex.split('').map(c => c + c).join('');
            const r = parseInt(hex.substring(0, 2), 16) / 255;
            const g = parseInt(hex.substring(2, 4), 16) / 255;
            const b = parseInt(hex.substring(4, 6), 16) / 255;
            const a = [r, g, b].map(v => v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4));
            return 0.2126 * a[0] + 0.7152 * a[1] + 0.0722 * a[2];
        }}

        function getContrastRatio(hex1, hex2) {{
            const lum1 = getLuminance(hex1);
            const lum2 = getLuminance(hex2);
            const brightest = Math.max(lum1, lum2);
            const darkest = Math.min(lum1, lum2);
            return (brightest + 0.05) / (darkest + 0.05);
        }}

        function updateWcagContrast() {{
            const theme = document.getElementById('inp-theme-color') ? document.getElementById('inp-theme-color').value : '#2563eb';
            const btnText = document.getElementById('inp-btn-text-color') ? document.getElementById('inp-btn-text-color').value : '#ffffff';
            const ratio = getContrastRatio(theme, btnText);
            const formatted = ratio.toFixed(1) + ':1';
            
            const badge = document.getElementById('wcag-contrast-badge');
            if (badge) {{
                if (ratio >= 7.0) {{
                    badge.className = 'contrast-meter-badge pass';
                    badge.textContent = `WCAG AAA (${{formatted}})`;
                }} else if (ratio >= 4.5) {{
                    badge.className = 'contrast-meter-badge pass';
                    badge.textContent = `WCAG AA (${{formatted}})`;
                }} else if (ratio >= 3.0) {{
                    badge.className = 'contrast-meter-badge warn';
                    badge.textContent = `Large Text (${{formatted}})`;
                }} else {{
                    badge.className = 'contrast-meter-badge fail';
                    badge.textContent = `Low Contrast (${{formatted}})`;
                }}
            }}

            const stylerBadge = document.getElementById('styler-wcag-badge');
            if (stylerBadge) {{
                if (ratio >= 7.0) {{
                    stylerBadge.style.color = '#10b981';
                    stylerBadge.textContent = `WCAG AAA (${{formatted}})`;
                }} else if (ratio >= 4.5) {{
                    stylerBadge.style.color = '#38bdf8';
                    stylerBadge.textContent = `WCAG AA (${{formatted}})`;
                }} else {{
                    stylerBadge.style.color = '#f59e0b';
                    stylerBadge.textContent = `WCAG (${{formatted}})`;
                }}
            }}
        }}

        // Brand Profile JSON Export & Import
        function exportBrandKitJson() {{
            const brand = {{
                campusName: document.getElementById('inp-campus-name').value,
                logoLink: document.getElementById('inp-logo-link').value,
                logoSize: document.getElementById('inp-logo-size') ? document.getElementById('inp-logo-size').value : '48',
                logoAlign: currentLogoAlign,
                themeColor: document.getElementById('inp-theme-color').value,
                secondaryColor: document.getElementById('inp-secondary-color') ? document.getElementById('inp-secondary-color').value : '#059669',
                bgColor: document.getElementById('inp-bg-color').value,
                btnRadius: document.getElementById('inp-btn-radius') ? document.getElementById('inp-btn-radius').value : '6px',
                phone: document.getElementById('inp-campus-phone') ? document.getElementById('inp-campus-phone').value : '',
                email: document.getElementById('inp-campus-email') ? document.getElementById('inp-campus-email').value : '',
                address: document.getElementById('inp-campus-address') ? document.getElementById('inp-campus-address').value : '',
                timings: document.getElementById('inp-campus-timings') ? document.getElementById('inp-campus-timings').value : '',
                websiteUrl: document.getElementById('inp-website-url').value,
                locationLink: document.getElementById('inp-location-link').value,
                portalUrl: document.getElementById('inp-portal-url').value,
                wa: document.getElementById('inp-soc-wa') ? document.getElementById('inp-soc-wa').value : '',
                fb: document.getElementById('inp-soc-fb').value,
                insta: document.getElementById('inp-soc-insta').value,
                twitter: document.getElementById('inp-soc-twitter').value,
                li: document.getElementById('inp-soc-linkedin').value,
                yt: document.getElementById('inp-soc-yt').value
            }};
            const str = JSON.stringify(brand, null, 2);
            const blob = new Blob([str], {{ type: 'application/json;charset=utf-8' }});
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = `${{(brand.campusName || 'Brand').replace(/\\s+/g, '_')}}_brand_profile.json`;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);
            showToast('Brand profile exported!');
        }}

        function importBrandKitJson(e) {{
            const file = e.target.files[0];
            if (!file) return;
            const reader = new FileReader();
            reader.onload = (evt) => {{
                try {{
                    const b = JSON.parse(evt.target.result);
                    if (b.campusName) document.getElementById('inp-campus-name').value = b.campusName;
                    if (b.logoLink) document.getElementById('inp-logo-link').value = b.logoLink;
                    if (b.logoSize) {{
                        document.getElementById('inp-logo-size').value = b.logoSize;
                        const valSpan = document.getElementById('shell-logo-size-val');
                        if (valSpan) valSpan.textContent = b.logoSize + 'px';
                    }}
                    if (b.logoAlign) {{
                        currentLogoAlign = b.logoAlign;
                        const alignSel = document.getElementById('inp-logo-align');
                        if (alignSel) alignSel.value = b.logoAlign;
                    }}
                    if (b.themeColor) document.getElementById('inp-theme-color').value = b.themeColor;
                    if (b.secondaryColor && document.getElementById('inp-secondary-color')) document.getElementById('inp-secondary-color').value = b.secondaryColor;
                    if (b.bgColor) document.getElementById('inp-bg-color').value = b.bgColor;
                    if (b.btnRadius && document.getElementById('inp-btn-radius')) document.getElementById('inp-btn-radius').value = b.btnRadius;
                    if (b.phone && document.getElementById('inp-campus-phone')) document.getElementById('inp-campus-phone').value = b.phone;
                    if (b.email && document.getElementById('inp-campus-email')) document.getElementById('inp-campus-email').value = b.email;
                    if (b.address && document.getElementById('inp-campus-address')) document.getElementById('inp-campus-address').value = b.address;
                    if (b.timings && document.getElementById('inp-campus-timings')) document.getElementById('inp-campus-timings').value = b.timings;
                    if (b.websiteUrl) document.getElementById('inp-website-url').value = b.websiteUrl;
                    if (b.locationLink) document.getElementById('inp-location-link').value = b.locationLink;
                    if (b.portalUrl) document.getElementById('inp-portal-url').value = b.portalUrl;
                    if (b.wa && document.getElementById('inp-soc-wa')) document.getElementById('inp-soc-wa').value = b.wa;
                    if (b.fb) document.getElementById('inp-soc-fb').value = b.fb;
                    if (b.insta) document.getElementById('inp-soc-insta').value = b.insta;
                    if (b.twitter) document.getElementById('inp-soc-twitter').value = b.twitter;
                    if (b.li) document.getElementById('inp-soc-linkedin').value = b.li;
                    if (b.yt) document.getElementById('inp-soc-yt').value = b.yt;

                    rebuildPreview();
                    updateShellPreview();
                    updateWcagContrast();
                    showToast('Brand Profile imported successfully!');
                }} catch (err) {{
                    showToast('Invalid JSON file');
                }}
            }};
            reader.readAsText(file);
        }}

        // ═══════════════════════════════════════════════════════
        // AI ADMISSION CAMPAIGN GENERATOR ENGINE
        // ═══════════════════════════════════════════════════════
        let selectedAiStage = 'incomplete_form';
        let currentAiGeneratedState = null;

        const AI_FUNNEL_KNOWLEDGE = {{
            'open_house': {{
                title: 'Open House & Campus Tour',
                badge: 'Open House Walkthrough',
                subject: 'Experience {{{{school_name}}}}: Open House & Campus Tour Invitation',
                preheader: 'Join our interactive campus walkthrough and meet academic leadership.',
                headline: 'DISCOVER THE ACADEMIC JOURNEY AT {{{{school_name}}}}',
                greeting: 'Dear Prospective Parents,',
                body: 'We are pleased to invite your family to our upcoming Campus Open House. This immersive session is designed to provide comprehensive insight into our curriculum, state-of-the-art learning laboratories, athletics facilities, and academic ethos.\\n\\nDuring your walkthrough, you will have the opportunity to engage directly with our Academic Leadership, tour active learning spaces, and understand how our holistic pedagogical model nurtures curiosity and excellence in every student.\\n\\nPlease reserve your family interaction slot using your Candidate Portal credentials below.',
                notice: 'Limited Walkthrough Slots: Registration for the upcoming Saturday session closes 48 hours prior.',
                buttonText: 'RESERVE TOUR SLOT'
            }},
            'incomplete_form': {{
                title: 'Incomplete Form Reminder',
                badge: 'Incomplete Form Reminder',
                subject: 'Action Required: Complete Your Application for {{{{student_name}}}} - {{{{school_name}}}}',
                preheader: 'Application No: {{{{application_no}}}} is pending mandatory details.',
                headline: 'CONTINUE YOUR ADMISSION APPLICATION',
                greeting: 'Dear {{{{father_name}}}},',
                body: 'Thank you for initiating the admission process for {{{{student_name}}}} for {{{{student_class}}}} at {{{{school_name}}}}.\\n\\nOur admissions records indicate that Application No: {{{{application_no}}}} is currently incomplete. Crucial academic records and parent contact details are awaiting submission to enable our committee to review your file.\\n\\nTo ensure your application is considered within the current evaluation cohort, please log in to the Candidate Portal and finalize the pending sections.',
                notice: 'Cohort Evaluation Window: Unsubmitted forms will be moved to the waitlist cycle after 3 business days.',
                buttonText: 'COMPLETE APPLICATION FORM'
            }},
            'slot_booking': {{
                title: 'Entrance Assessment / Slot Booking',
                badge: 'Interaction Slot Booking',
                subject: 'Schedule Assessment & Family Interaction: Application {{{{application_no}}}}',
                preheader: 'Select your preferred date and time slot for {{{{student_name}}}}.',
                headline: 'ADMISSION ASSESSMENT & INTERACTION SCHEDULING',
                greeting: 'Dear Parents,',
                body: 'We are delighted to inform you that Application No: {{{{application_no}}}} for {{{{student_name}}}} ({{{{student_class}}}}) has successfully passed preliminary document screening.\\n\\nYou are now invited to choose a convenient time slot for the candidate assessment and parent interaction with our academic panel.\\n\\nPlease log in to your Candidate Portal below, navigate to the Assessment Schedule tab, and reserve your preferred appointment.',
                notice: 'Interaction Guidelines: Punctuality is required. The interaction process requires approximately 45 minutes.',
                buttonText: 'BOOK INTERACTION SLOT'
            }},
            'provisional_offer': {{
                title: 'Provisional Offer of Admission',
                badge: 'Provisional Offer Letter',
                subject: 'Congratulations: Provisional Offer of Admission for {{{{student_name}}}} - {{{{school_name}}}}',
                preheader: 'Provisional seat allocation confirmed for Academic Session 2026-27.',
                headline: 'PROVISIONAL OFFER OF ADMISSION',
                greeting: 'Dear {{{{father_name}}}},',
                body: 'On behalf of the Admissions Committee and Academic Leadership of {{{{school_name}}}}, we take immense pleasure in offering {{{{student_name}}}} provisional admission to {{{{student_class}}}} for Academic Session 2026-27.\\n\\nOur evaluation committee was deeply impressed by {{{{student_name}}}} interaction and potential. We look forward to partnering with your family to nurture excellence, character, and lifelong curiosity.\\n\\nTo review your official Provisional Offer Letter and proceed with seat confirmation, please access your Candidate Portal credentials below.',
                notice: 'Offer Acceptance Window: This provisional offer remains valid for 7 calendar days from the date of issue.',
                buttonText: 'VIEW PROVISIONAL OFFER'
            }},
            'fee_deadline': {{
                title: 'Admission Fee Deadline Reminder',
                badge: 'Seat Confirmation Fee Due',
                subject: 'Urgent: Admission Fee Payment Deadline for {{{{student_name}}}} (App: {{{{application_no}}}})',
                preheader: 'Seat confirmation fee of {{{{current_fee_receipt_amount}}}} is due.',
                headline: 'SEAT CONFIRMATION FEE PAYMENT REMINDER',
                greeting: 'Dear {{{{father_name}}}},',
                body: 'This is an important reminder regarding the admission offer extended to {{{{student_name}}}} for {{{{student_class}}}} at {{{{school_name}}}} under Application No: {{{{application_no}}}}.\\n\\nTo secure and lock the allocated seat, the admission confirmation fee of {{{{current_fee_receipt_amount}}}} must be remitted before the deadline.\\n\\nUnconfirmed seats will be released to waitlisted candidates immediately upon deadline expiry. Please make the secure payment online via your Candidate Portal.',
                notice: 'Final Fee Deadline: Remit payment before deadline expiry to guarantee confirmed seat allocation.',
                buttonText: 'PAY ADMISSION FEE'
            }},
            'doc_verification': {{
                title: 'Mandatory Document Verification',
                badge: 'Document Verification',
                subject: 'Mandatory Document Submission Required: Application {{{{application_no}}}}',
                preheader: 'Upload birth certificate, transfer certificate & medical records.',
                headline: 'VERIFICATION OF MANDATORY ADMISSION DOCUMENTS',
                greeting: 'Dear Parents,',
                body: 'Following the provisional admission confirmation for {{{{student_name}}}} ({{{{student_class}}}}), our compliance department requires mandatory documentation to complete formal enrollment with the education board.\\n\\nPlease upload self-attested digital copies of the candidate Birth Certificate, Transfer Certificate (TC) from the previous institution, Report Cards, and immunization history.\\n\\nAll documents must be uploaded directly via the Candidate Portal for digital verification.',
                notice: 'Mandatory Board Compliance: Document verification must be concluded prior to commencement of classes.',
                buttonText: 'UPLOAD VERIFICATION DOCUMENTS'
            }},
            'orientation': {{
                title: 'Student Induction & Orientation Day',
                badge: 'Orientation Day Schedule',
                subject: 'Welcome to {{{{school_name}}}}: Student Induction & Orientation Day Schedule',
                preheader: 'Important details for Orientation Day and student onboarding.',
                headline: 'WELCOME TO THE {{{{school_name}}}} FAMILY',
                greeting: 'Dear Parents & Students,',
                body: 'We are thrilled to welcome {{{{student_name}}}} to {{{{school_name}}}} for Academic Session 2026-27! We look forward to an inspiring academic journey filled with discovery, innovation, and growth.\\n\\nOur mandatory Student Induction and Parent Orientation Day is scheduled shortly. The session will cover academic guidelines, uniform and books distribution, transport routes, and classroom allocation.\\n\\nPlease log in to your Candidate Portal below to download the comprehensive Orientation Schedule and Campus Guide.',
                notice: 'Orientation Check-in: Please arrive 15 minutes prior to the scheduled start time at the Main Campus Auditorium.',
                buttonText: 'DOWNLOAD ORIENTATION GUIDE'
            }}
        }};

        function selectAiFunnelStage(stageKey) {{
            selectedAiStage = stageKey;
            document.querySelectorAll('.ai-funnel-pill').forEach(btn => btn.classList.remove('active'));
            const activeBtn = document.getElementById(`ai-stage-${{stageKey}}`);
            if (activeBtn) activeBtn.classList.add('active');

            const badge = document.getElementById('ai-stage-badge');
            if (badge && AI_FUNNEL_KNOWLEDGE[stageKey]) {{
                badge.textContent = AI_FUNNEL_KNOWLEDGE[stageKey].title;
            }}
            runAiGenerator();
        }}

        function applyAiInspirationChip(chipText, stageKey) {{
            const promptBox = document.getElementById('ai-prompt');
            if (promptBox) promptBox.value = chipText;
            selectAiFunnelStage(stageKey);
            showToast(`Applied preset: ${{chipText}}`);
        }}

        function runAiGenerator() {{
            const stage = AI_FUNNEL_KNOWLEDGE[selectedAiStage] || AI_FUNNEL_KNOWLEDGE['incomplete_form'];
            const audience = document.getElementById('ai-audience') ? document.getElementById('ai-audience').value : 'parents';
            const tone = document.getElementById('ai-tone') ? document.getElementById('ai-tone').value : 'warm';
            const userPrompt = (document.getElementById('ai-prompt') ? document.getElementById('ai-prompt').value : '').trim();

            const incNotice = document.getElementById('ai-chk-notice') ? document.getElementById('ai-chk-notice').checked : true;
            const incRoadmap = document.getElementById('ai-chk-roadmap') ? document.getElementById('ai-chk-roadmap').checked : true;
            const incLogin = document.getElementById('ai-chk-login') ? document.getElementById('ai-chk-login').checked : true;

            let subject = stage.subject;
            let preheader = stage.preheader;
            let headline = stage.headline;
            let greeting = stage.greeting;
            let body = stage.body;
            let notice = stage.notice;
            let buttonText = stage.buttonText;

            // Apply Tone Modifiers
            if (tone === 'urgent') {{
                subject = 'Immediate Action Required: ' + subject.replace('Action Required: ', '');
                headline = 'URGENT NOTICE: ' + headline;
                notice = 'TIME-SENSITIVE: ' + notice;
            }} else if (tone === 'formal') {{
                greeting = 'Dear Sir / Madam,';
            }} else if (tone === 'celebratory') {{
                subject = 'Welcome to Our Community: ' + subject.replace('Congratulations: ', '');
            }}

            // Incorporate Custom Prompt directive if provided
            if (userPrompt) {{
                body = body + '\\n\\nSpecial Advisory: ' + userPrompt;
            }}

            // Store state
            currentAiGeneratedState = {{
                subject: subject,
                preheader: preheader,
                headline: headline,
                greeting: greeting,
                body: body,
                noticeText: notice,
                includeNotice: incNotice,
                includeRoadmap: incRoadmap,
                includeLogin: incLogin,
                buttonText: buttonText
            }};

            renderAiPreview();
        }}

        function renderAiPreview() {{
            if (!currentAiGeneratedState) runAiGenerator();
            const s = currentAiGeneratedState;

            const origSubj = document.getElementById('inp-subject').value;
            const origPre = document.getElementById('inp-preheader').value;
            const origHead = document.getElementById('inp-headline').value;
            const origGreet = document.getElementById('inp-greeting').value;
            const origBody = document.getElementById('inp-body').value;
            const origBtn = document.getElementById('inp-button-text').value;
            const origNotice = document.getElementById('inp-notice-text') ? document.getElementById('inp-notice-text').value : '';
            const origIncNotice = document.getElementById('inp-include-notice') ? document.getElementById('inp-include-notice').checked : false;
            const origIncRoad = document.getElementById('inp-include-roadmap') ? document.getElementById('inp-include-roadmap').checked : false;
            const origIncLog = document.getElementById('inp-include-login') ? document.getElementById('inp-include-login').checked : true;

            document.getElementById('inp-subject').value = s.subject;
            document.getElementById('inp-preheader').value = s.preheader;
            document.getElementById('inp-headline').value = s.headline;
            document.getElementById('inp-greeting').value = s.greeting;
            document.getElementById('inp-body').value = s.body;
            document.getElementById('inp-button-text').value = s.buttonText;
            if (document.getElementById('inp-notice-text')) document.getElementById('inp-notice-text').value = s.noticeText;
            if (document.getElementById('inp-include-notice')) document.getElementById('inp-include-notice').checked = s.includeNotice;
            if (document.getElementById('inp-include-roadmap')) document.getElementById('inp-include-roadmap').checked = s.includeRoadmap;
            if (document.getElementById('inp-include-login')) document.getElementById('inp-include-login').checked = s.includeLogin;

            const html = generateEmailHTML(true);

            document.getElementById('inp-subject').value = origSubj;
            document.getElementById('inp-preheader').value = origPre;
            document.getElementById('inp-headline').value = origHead;
            document.getElementById('inp-greeting').value = origGreet;
            document.getElementById('inp-body').value = origBody;
            document.getElementById('inp-button-text').value = origBtn;
            if (document.getElementById('inp-notice-text')) document.getElementById('inp-notice-text').value = origNotice;
            if (document.getElementById('inp-include-notice')) document.getElementById('inp-include-notice').checked = origIncNotice;
            if (document.getElementById('inp-include-roadmap')) document.getElementById('inp-include-roadmap').checked = origIncRoad;
            if (document.getElementById('inp-include-login')) document.getElementById('inp-include-login').checked = origIncLog;

            const frame = document.getElementById('ai-live-iframe');
            if (frame) frame.srcdoc = html;
        }}

        function loadAiIntoStudio() {{
            if (!currentAiGeneratedState) runAiGenerator();
            const s = currentAiGeneratedState;

            document.getElementById('inp-subject').value = s.subject;
            document.getElementById('inp-preheader').value = s.preheader;
            document.getElementById('inp-headline').value = s.headline;
            document.getElementById('inp-greeting').value = s.greeting;
            document.getElementById('inp-body').value = s.body;
            document.getElementById('inp-button-text').value = s.buttonText;
            if (document.getElementById('inp-notice-text')) document.getElementById('inp-notice-text').value = s.noticeText;
            if (document.getElementById('inp-include-notice')) document.getElementById('inp-include-notice').checked = s.includeNotice;
            if (document.getElementById('inp-include-roadmap')) document.getElementById('inp-include-roadmap').checked = s.includeRoadmap;
            if (document.getElementById('inp-include-login')) document.getElementById('inp-include-login').checked = s.includeLogin;

            document.getElementById('inp-template-selector').value = 'custom';
            onSubjectInput();
            onBodyInput();
            switchView('studio');
            rebuildPreview();
            showToast('AI Campaign loaded into Studio Composer!');
        }}

        function copyAiHTML() {{
            const frame = document.getElementById('ai-live-iframe');
            if (frame && frame.srcdoc) {{
                navigator.clipboard.writeText(frame.srcdoc).then(() => showToast('AI Generated HTML copied!'));
            }} else {{
                showToast('Please generate template first');
            }}
        }}

        // ═══════════════════════════════════════════════════════
        // HUB QUICK ACTIONS
        // ═══════════════════════════════════════════════════════
        function launchHubScenario(templateId) {{
            switchView('studio');
            const selector = document.getElementById('inp-template-selector');
            if (selector) {{
                selector.value = templateId;
                onTemplateSelect(templateId);
            }}
            showToast(`Loaded scenario ${{templateId}} in Studio!`);
        }}

        function copyText(str) {{
            navigator.clipboard.writeText(str).then(() => showToast(`Copied ${{str}} to clipboard!`));
        }}

        const BRAND_PRESETS = [
            {{
                name: 'Simply Blue',
                primary: '#2563eb',
                secondary: '#3b82f6',
                bg: '#f1f5f9',
                cardBg: '#ffffff',
                textPrimary: '#1e3a8a',
                textBody: '#334155',
                textMuted: '#64748b',
                highlightBg: '#eff6ff',
                highlightBorder: '#bfdbfe',
                highlightText: '#1e40af',
                btnText: '#ffffff',
                cardBorder: '#e2e8f0'
            }},
            {{
                name: 'Emerald Luxe',
                primary: '#059669',
                secondary: '#10b981',
                bg: '#f0fdf4',
                cardBg: '#ffffff',
                textPrimary: '#064e3b',
                textBody: '#1f2937',
                textMuted: '#6b7280',
                highlightBg: '#ecfdf5',
                highlightBorder: '#a7f3d0',
                highlightText: '#065f46',
                btnText: '#ffffff',
                cardBorder: '#d1fae5'
            }},
            {{
                name: 'Classic Crimson',
                primary: '#991b1b',
                secondary: '#dc2626',
                bg: '#fef2f2',
                cardBg: '#ffffff',
                textPrimary: '#7f1d1d',
                textBody: '#292524',
                textMuted: '#78716c',
                highlightBg: '#fff1f2',
                highlightBorder: '#fecdd3',
                highlightText: '#9f1239',
                btnText: '#ffffff',
                cardBorder: '#fee2e2'
            }},
            {{
                name: 'Royal Indigo',
                primary: '#4f46e5',
                secondary: '#6366f1',
                bg: '#f5f3ff',
                cardBg: '#ffffff',
                textPrimary: '#312e81',
                textBody: '#1e1b4b',
                textMuted: '#6b7280',
                highlightBg: '#e0e7ff',
                highlightBorder: '#c7d2fe',
                highlightText: '#3730a3',
                btnText: '#ffffff',
                cardBorder: '#ede9fe'
            }},
            {{
                name: 'Sunset Amber',
                primary: '#d97706',
                secondary: '#f59e0b',
                bg: '#fffbeb',
                cardBg: '#ffffff',
                textPrimary: '#78350f',
                textBody: '#292524',
                textMuted: '#78716c',
                highlightBg: '#fef3c7',
                highlightBorder: '#fde68a',
                highlightText: '#92400e',
                btnText: '#ffffff',
                cardBorder: '#fef3c7'
            }},
            {{
                name: 'Slate Noir',
                primary: '#0f172a',
                secondary: '#334155',
                bg: '#f8fafc',
                cardBg: '#ffffff',
                textPrimary: '#0f172a',
                textBody: '#334155',
                textMuted: '#64748b',
                highlightBg: '#f1f5f9',
                highlightBorder: '#cbd5e1',
                highlightText: '#0f172a',
                btnText: '#ffffff',
                cardBorder: '#e2e8f0'
            }},
            {{
                name: 'Nordic Teal',
                primary: '#0d9488',
                secondary: '#14b8a6',
                bg: '#f0fdfa',
                cardBg: '#ffffff',
                textPrimary: '#134e4a',
                textBody: '#1e293b',
                textMuted: '#64748b',
                highlightBg: '#ccfbf1',
                highlightBorder: '#99f6e4',
                highlightText: '#115e59',
                btnText: '#ffffff',
                cardBorder: '#ccfbf1'
            }},
            {{
                name: 'Midnight Obsidian',
                primary: '#38bdf8',
                secondary: '#0284c7',
                bg: '#090d16',
                cardBg: '#131b2e',
                textPrimary: '#f8fafc',
                textBody: '#cbd5e1',
                textMuted: '#94a3b8',
                highlightBg: '#1e293b',
                highlightBorder: '#334155',
                highlightText: '#38bdf8',
                btnText: '#0f172a',
                cardBorder: '#1e293b'
            }},
            {{
                name: 'Amethyst Purple',
                primary: '#7c3aed',
                secondary: '#8b5cf6',
                bg: '#faf5ff',
                cardBg: '#ffffff',
                textPrimary: '#4c1d95',
                textBody: '#2e1065',
                textMuted: '#6b7280',
                highlightBg: '#f3e8ff',
                highlightBorder: '#ddd6fe',
                highlightText: '#5b21b6',
                btnText: '#ffffff',
                cardBorder: '#f3e8ff'
            }},
            {{
                name: 'Coral Blossom',
                primary: '#e11d48',
                secondary: '#f43f5e',
                bg: '#fff1f2',
                cardBg: '#ffffff',
                textPrimary: '#881337',
                textBody: '#27272a',
                textMuted: '#71717a',
                highlightBg: '#ffe4e6',
                highlightBorder: '#fecdd3',
                highlightText: '#9f1239',
                btnText: '#ffffff',
                cardBorder: '#ffe4e6'
            }},
            {{
                name: 'Cyber Bronze',
                primary: '#854d0e',
                secondary: '#a16207',
                bg: '#faf8f5',
                cardBg: '#ffffff',
                textPrimary: '#451a03',
                textBody: '#292524',
                textMuted: '#78716c',
                highlightBg: '#fef9c3',
                highlightBorder: '#fef08a',
                highlightText: '#713f12',
                btnText: '#ffffff',
                cardBorder: '#fef08a'
            }},
            {{
                name: 'Titanium Tech',
                primary: '#475569',
                secondary: '#64748b',
                bg: '#f1f5f9',
                cardBg: '#ffffff',
                textPrimary: '#0f172a',
                textBody: '#1e293b',
                textMuted: '#64748b',
                highlightBg: '#e2e8f0',
                highlightBorder: '#cbd5e1',
                highlightText: '#1e293b',
                btnText: '#ffffff',
                cardBorder: '#cbd5e1'
            }}
        ];

        let activeBrandPresetIndex = 0;

        function applyBrandPreset(index) {{
            const p = BRAND_PRESETS[index];
            if (!p) return;
            activeBrandPresetIndex = index;

            const setVal = (id, val) => {{
                const el = document.getElementById(id);
                if (el) el.value = val;
            }};

            setVal('inp-theme-color', p.primary);
            setVal('inp-theme-color-mini', p.primary);
            setVal('inp-secondary-color', p.secondary);
            setVal('inp-bg-color', p.bg);
            setVal('inp-bg-color-mini', p.bg);
            setVal('inp-card-bg-color', p.cardBg);
            setVal('inp-headline-color', p.textPrimary);
            setVal('inp-text-color', p.textBody);
            setVal('inp-text-color-mini', p.textBody);
            setVal('inp-highlight-color', p.highlightBg);
            setVal('inp-btn-text-color', p.btnText);

            document.querySelectorAll('.theme-preset-btn').forEach((btn, idx) => {{
                btn.classList.toggle('active', idx === index);
            }});

            rebuildPreview();
            updateShellPreview();
            updateWcagContrast();
            showToast(`Theme applied: ${{p.name}} (Fonts, Bg & Highlights synchronized)`);
        }}

        function stepTemplate(direction) {{
            const select = document.getElementById('inp-template-selector');
            const options = Array.from(select.options).filter(o => o.value !== 'custom');
            if (options.length === 0) return;
            let currentIndex = options.findIndex(o => o.value === select.value);
            if (currentIndex === -1) currentIndex = 0;
            let nextIndex = currentIndex + direction;
            if (nextIndex < 0) nextIndex = options.length - 1;
            if (nextIndex >= options.length) nextIndex = 0;
            select.value = options[nextIndex].value;
            onTemplateSelect(select.value);
            showToast(`Loaded: ${{options[nextIndex].textContent}}`);
        }}

        let activeScenarioCategory = 'All';

        function filterScenariosByCategory(catName) {{
            activeScenarioCategory = catName;
            const select = document.getElementById('inp-template-selector');
            select.innerHTML = '<option value="custom">✏️ Custom Blank Template</option>';
            
            let filtered = CANONICAL_TEMPLATES;
            if (catName !== 'All') {{
                filtered = CANONICAL_TEMPLATES.filter(t => (t.category || '').toLowerCase().includes(catName.toLowerCase()));
            }}

            filtered.forEach(t => {{
                const opt = document.createElement('option');
                opt.value = t.id;
                opt.textContent = t.name;
                select.appendChild(opt);
            }});

            document.querySelectorAll('.scen-cat-pill').forEach(btn => {{
                btn.classList.toggle('active', btn.getAttribute('data-cat') === catName);
            }});

            const countBadge = document.getElementById('active-scenario-count-badge');
            if (countBadge) countBadge.textContent = `${{filtered.length}} Alerts`;

            if (filtered.length > 0) {{
                select.value = filtered[0].id;
                onTemplateSelect(filtered[0].id);
            }}
        }}

        function populateTemplateDropdown() {{
            const select = document.getElementById('inp-template-selector');
            select.innerHTML = '<option value="custom">✏️ Custom Blank Template</option>';

            const categories = {{}};
            CANONICAL_TEMPLATES.forEach(t => {{
                const cat = t.category || "General Alerts";
                if (!categories[cat]) categories[cat] = [];
                categories[cat].push(t);
            }});

            for (const [cat, tmpls] of Object.entries(categories)) {{
                const group = document.createElement('optgroup');
                group.label = cat;
                tmpls.forEach(t => {{
                    const opt = document.createElement('option');
                    opt.value = t.id;
                    opt.textContent = t.name;
                    group.appendChild(opt);
                }});
                select.appendChild(group);
            }}

            if (CANONICAL_TEMPLATES.length > 0) {{
                select.value = CANONICAL_TEMPLATES[0].id;
                loadCanonicalTemplate(CANONICAL_TEMPLATES[0]);
            }}
        }}

        function onTemplateSelect(templateId) {{
            if (templateId === 'custom') return;
            const t = CANONICAL_TEMPLATES.find(x => x.id === templateId);
            if (t) loadCanonicalTemplate(t);
        }}

        function loadCanonicalTemplate(t) {{
            const campusName = document.getElementById('inp-campus-name').value || 'Simply Admission';
            document.getElementById('inp-subject').value = (t.subject || '').replace(/{{{{school_name}}}}/g, campusName);
            document.getElementById('inp-headline').value = t.headline || '';
            document.getElementById('inp-greeting').value = t.greeting || 'Dear Parents,';
            document.getElementById('inp-body').value = t.body || '';
            document.getElementById('inp-include-login').checked = t.include_login !== false;
            document.getElementById('inp-login-prompt').value = t.login_prompt || 'Complete your Application Form using your Candidate Portal credentials below:';
            document.getElementById('inp-button-text').value = t.button_text || 'CANDIDATE LOGIN';
            onSubjectInput();
            onBodyInput();
            rebuildPreview();
            renderScenarioPaginator();
        }}

        function resetTemplate() {{
            const val = document.getElementById('inp-template-selector').value;
            onTemplateSelect(val);
            showToast('Template reset to default copy');
        }}

        function setGreeting(val) {{
            document.getElementById('inp-greeting').value = val;
            rebuildPreview();
            showToast('Greeting updated');
        }}

        // CRM Variables Explorer
        function populateCrmDrawer() {{
            const pillsContainer = document.getElementById('crm-category-pills');
            pillsContainer.innerHTML = '';

            const allBtn = document.createElement('button');
            allBtn.type = 'button';
            allBtn.className = 'drawer-cat-pill active';
            allBtn.textContent = 'All (68)';
            allBtn.onclick = () => filterCrmCategory('all', allBtn);
            pillsContainer.appendChild(allBtn);

            for (const catName of Object.keys(CRM_VARIABLES_CATALOG)) {{
                const btn = document.createElement('button');
                btn.type = 'button';
                btn.className = 'drawer-cat-pill';
                btn.textContent = catName;
                btn.onclick = () => filterCrmCategory(catName, btn);
                pillsContainer.appendChild(btn);
            }}

            renderCrmChips('all', '');
        }}

        function filterCrmCategory(catName, btnEl) {{
            document.querySelectorAll('.drawer-cat-pill').forEach(b => b.classList.remove('active'));
            if (btnEl) btnEl.classList.add('active');
            const query = (document.getElementById('crm-search-inp').value || '').trim();
            renderCrmChips(catName, query);
        }}

        function onCrmSearchChange(query) {{
            const activeBtn = document.querySelector('.drawer-cat-pill.active');
            const cat = activeBtn ? activeBtn.textContent.replace(/\\s*\\(\\d+\\)/, '').trim() : 'all';
            renderCrmChips(cat, query);
        }}

        function renderCrmChips(activeCat, query) {{
            const container = document.getElementById('crm-tags-chips-container');
            container.innerHTML = '';
            const q = query.toLowerCase();

            for (const [catName, vars] of Object.entries(CRM_VARIABLES_CATALOG)) {{
                if (activeCat !== 'all' && activeCat !== catName) continue;
                for (const v of vars) {{
                    if (q && !v.key.toLowerCase().includes(q) && !v.label.toLowerCase().includes(q)) continue;
                    const chip = document.createElement('button');
                    chip.type = 'button';
                    chip.className = 'drawer-chip';
                    chip.innerHTML = `<span>+ ${{v.label}}</span> <code>{{{{${{v.key}}}}}}</code>`;
                    chip.onclick = () => insertTag(`{{{{${{v.key}}}}}}`);
                    container.appendChild(chip);
                }}
            }}
        }}

        function toggleCrmDrawer() {{
            crmDrawerOpen = !crmDrawerOpen;
            const drawer = document.getElementById('crm-vars-drawer');
            const label = document.getElementById('crm-drawer-toggle-text');
            drawer.style.display = crmDrawerOpen ? 'block' : 'none';
            label.textContent = crmDrawerOpen ? 'Close Explorer' : 'Explore All 68 Keys';
        }}

        function insertTag(tag) {{
            const textarea = document.getElementById('inp-body');
            const start = textarea.selectionStart;
            const end = textarea.selectionEnd;
            const text = textarea.value;
            textarea.value = text.substring(0, start) + tag + text.substring(end);
            textarea.selectionStart = textarea.selectionEnd = start + tag.length;
            textarea.focus();
            onBodyInput();
            rebuildPreview();
            showToast(`Inserted ${{tag}}`);
        }}

        function wrapSelection(openTag, closeTag) {{
            const textarea = document.getElementById('inp-body');
            const start = textarea.selectionStart;
            const end = textarea.selectionEnd;
            const selected = textarea.value.substring(start, end) || 'Sample text';
            const rep = openTag + selected + closeTag;
            textarea.value = textarea.value.substring(0, start) + rep + textarea.value.substring(end);
            textarea.focus();
            onBodyInput();
            rebuildPreview();
        }}

        function insertCalloutBlock() {{
            const block = `\\n<div style="background-color:#f8fafc; border:1px solid #e2e8f0; border-radius:6px; padding:14px; margin:16px 0;"><strong>Important Notice:</strong> Add your key details here.</div>\\n`;
            insertTag(block);
        }}

        function insertFeeTable() {{
            const snippet = `\\n<table cellpadding="0" cellspacing="0" border="0" width="100%" style="margin:16px 0; background:#f8fafc; border:1px solid #e2e8f0; border-radius:6px; overflow:hidden;">
  <tr style="background:#f1f5f9;">
    <td style="padding:8px 12px; font-weight:bold; color:#334155; font-size:13px;">Fee Description</td>
    <td align="right" style="padding:8px 12px; font-weight:bold; color:#334155; font-size:13px;">Amount</td>
  </tr>
  <tr>
    <td style="padding:8px 12px; color:#475569; font-size:13px; border-top:1px solid #e2e8f0;">{{{{current_fee_receipt_head}}}}</td>
    <td align="right" style="padding:8px 12px; font-weight:bold; color:#0f172a; font-size:13px; border-top:1px solid #e2e8f0;">{{{{current_fee_receipt_amount}}}}</td>
  </tr>
</table>\\n`;
            insertTag(snippet);
        }}

        function insertScheduleCard() {{
            const snippet = `\\n<table cellpadding="0" cellspacing="0" border="0" width="100%" style="margin:16px 0; background:#f0fdf4; border:1px solid #bbf7d0; border-radius:6px;">
  <tr>
    <td style="padding:12px;">
      <div style="font-size:11px; font-weight:bold; color:#15803d; text-transform:uppercase; margin-bottom:4px;">Scheduled Interaction Details</div>
      <div style="font-size:13px; color:#1e293b; margin-bottom:3px;"><strong>Date:</strong> {{{{meeting_date}}}}</div>
      <div style="font-size:13px; color:#1e293b; margin-bottom:3px;"><strong>Time:</strong> {{{{meeting_time}}}}</div>
      <div style="font-size:13px; color:#1e293b;"><strong>Venue / Campus:</strong> {{{{school_address}}}}</div>
    </td>
  </tr>
</table>\\n`;
            insertTag(snippet);
        }}

        function insertChecklist() {{
            const snippet = `\\n<div style="margin:16px 0; padding:12px; background:#f8fafc; border:1px solid #e2e8f0; border-radius:6px;">
  <div style="font-weight:bold; font-size:13px; color:#334155; margin-bottom:6px;">Required Verification Documents:</div>
  <ul style="margin:0; padding-left:18px; font-size:13px; color:#475569; line-height:1.6;">
    <li>Student Birth Certificate (Original + Copy)</li>
    <li>Previous Class Academic Report Card</li>
    <li>Parent Residential Address Proof (Aadhaar / Passport)</li>
  </ul>
</div>\\n`;
            insertTag(snippet);
        }}

        function insertSupportHelpdesk() {{
            const snippet = `\\n<table cellpadding="0" cellspacing="0" border="0" width="100%" style="margin:16px 0; background:#f1f5f9; border-radius:6px;">
  <tr>
    <td style="padding:10px 14px; font-size:12px; color:#475569;">
      <strong>Need assistance?</strong> Contact our Admissions Desk at <strong>{{{{school_mobile_no}}}}</strong> or email <strong>{{{{school_email_id}}}}</strong>.
    </td>
  </tr>
</table>\\n`;
            insertTag(snippet);
        }}

        // Real-Time Linter & Character Counters
        function onSubjectInput() {{
            const val = document.getElementById('inp-subject').value || '';
            const len = val.length;
            const badge = document.getElementById('subj-char-count');
            badge.textContent = `${{len}} / 50`;
            badge.className = 'subj-counter-badge ' + (len <= 50 ? 'safe' : len <= 65 ? 'warn' : 'danger');
            updateLockscreenPreview();
            rebuildPreview();
        }}

        function onBodyInput() {{
            const val = document.getElementById('inp-body').value || '';
            const wordCount = val.trim().split(/\\s+/).filter(Boolean).length;
            const seconds = Math.max(10, Math.round((wordCount / 200) * 60));
            document.getElementById('read-time-badge').textContent = `${{seconds}}s read (${{wordCount}} words)`;

            // Check for broken merge tags (unclosed braces)
            const lintBox = document.getElementById('lint-alert-box');
            const brokenRegex = /{{{{[^}}]*$/m;
            if (brokenRegex.test(val)) {{
                lintBox.style.display = 'block';
                lintBox.textContent = '⚠️ Warning: Detected unclosed variable brace "{{...". Please check your merge tags.';
            }} else {{
                lintBox.style.display = 'none';
            }}

            updateLockscreenPreview();
            updateOmniCompanionText();
            rebuildPreview();
        }}

        // Viewport & Zoom Controls
        function setViewportMode(mode) {{
            currentViewport = mode;
            const wrapper = document.getElementById('preview-wrapper');
            const dualWrapper = document.getElementById('dual-preview-container');
            const btns = {{
                desktop: document.getElementById('btn-vp-desktop'),
                tablet: document.getElementById('btn-vp-tablet'),
                mobile: document.getElementById('btn-vp-mobile'),
                dual: document.getElementById('btn-vp-dual')
            }};

            Object.values(btns).forEach(b => b && b.classList.remove('active'));

            if (mode === 'dual') {{
                wrapper.style.display = 'none';
                dualWrapper.style.display = 'flex';
                if (btns.dual) btns.dual.classList.add('active');
                rebuildPreview();
                return;
            }}

            wrapper.style.display = 'block';
            dualWrapper.style.display = 'none';
            wrapper.classList.remove('mobile-mode', 'tablet-mode');

            if (mode === 'mobile') {{
                wrapper.classList.add('mobile-mode');
                if (btns.mobile) btns.mobile.classList.add('active');
            }} else if (mode === 'tablet') {{
                wrapper.classList.add('tablet-mode');
                if (btns.tablet) btns.tablet.classList.add('active');
            }} else {{
                if (btns.desktop) btns.desktop.classList.add('active');
            }}
        }}

        function setZoom(scale) {{
            currentZoom = scale;
            const frame = document.getElementById('live-iframe');
            frame.style.transform = scale === 1 ? 'none' : `scale(${{scale}})`;
            frame.style.transformOrigin = 'top center';
            showToast(`Preview scale: ${{Math.round(scale * 100)}}%`);
        }}

        function toggleDarkSimulation() {{
            isDarkSim = !isDarkSim;
            const frame = document.getElementById('live-iframe');
            const btn = document.getElementById('btn-dark-sim');
            frame.classList.toggle('dark-sim', isDarkSim);
            btn.classList.toggle('active', isDarkSim);
            showToast(isDarkSim ? 'Simulating Parent Dark Mode' : 'Standard Light Mode');
        }}

        function toggleLockscreenMockup() {{
            isLockscreenOpen = !isLockscreenOpen;
            const card = document.getElementById('lockscreen-mockup-card');
            const btn = document.getElementById('btn-lockscreen-toggle');
            card.classList.toggle('show', isLockscreenOpen);
            btn.classList.toggle('active', isLockscreenOpen);
            if (isLockscreenOpen) updateLockscreenPreview();
        }}

        function updateLockscreenPreview() {{
            const campusName = document.getElementById('inp-campus-name').value || 'SIMPLY ADMISSION';
            const subj = document.getElementById('inp-subject').value || 'Admission Notification';
            const preheader = document.getElementById('inp-preheader').value;
            const rawBody = document.getElementById('inp-body').value || '';
            const snippet = preheader || rawBody.replace(/<[^>]+>/g, '').substring(0, 100) + '...';

            document.getElementById('ls-sender-name').textContent = campusName.toUpperCase();
            document.getElementById('ls-subject-text').textContent = subj;
            document.getElementById('ls-snippet-text').textContent = snippet;
        }}

        function toggleOmniCompanion() {{
            isOmniOpen = !isOmniOpen;
            const card = document.getElementById('omni-companion-card');
            const btn = document.getElementById('btn-omni-toggle');
            card.classList.toggle('show', isOmniOpen);
            btn.classList.toggle('active', isOmniOpen);
            if (isOmniOpen) updateOmniCompanionText();
        }}

        function updateOmniCompanionText() {{
            const campusName = document.getElementById('inp-campus-name').value || 'Simply Admission';
            const headline = document.getElementById('inp-headline').value || 'Admission Update';
            const rawBody = (document.getElementById('inp-body').value || '').replace(/<[^>]+>/g, '').replace(/\\s+/g, ' ').substring(0, 220);
            const companion = `[${{campusName}}] ${{headline}}: ${{rawBody}}... Log in to your portal: {{{{school_url}}}}`;
            document.getElementById('omni-text-content').textContent = companion;
        }}

        function copyOmniText() {{
            const txt = document.getElementById('omni-text-content').textContent;
            navigator.clipboard.writeText(txt).then(() => showToast('SMS / WhatsApp copy copied!'));
        }}

        // HTML Generator Core (Strict: Zero-emoticons, only CDN icons in footer)
        function generateEmailHTML(useSampleData = false) {{
            const campusName = (document.getElementById('inp-campus-name').value || '').trim() || 'Simply Admission';
            const logoLink = (document.getElementById('inp-logo-link').value || '').trim();
            const portalUrl = (document.getElementById('inp-portal-url').value || '').trim() || '{{{{school_url}}}}';
            const locationLink = (document.getElementById('inp-location-link').value || '').trim() || 'https://maps.google.com';
            const websiteUrl = (document.getElementById('inp-website-url').value || '').trim() || 'http://simplyadmission.com';
            const themeColor = document.getElementById('inp-theme-color').value || '#2563eb';
            const bgColor = (document.getElementById('inp-bg-color') ? document.getElementById('inp-bg-color').value : '') || '#f1f5f9';
            const cardBgColor = (document.getElementById('inp-card-bg-color') ? document.getElementById('inp-card-bg-color').value : '') || '#ffffff';
            const headlineColor = (document.getElementById('inp-headline-color') ? document.getElementById('inp-headline-color').value : '') || themeColor;
            const textBodyColor = (document.getElementById('inp-text-color') ? document.getElementById('inp-text-color').value : '') || '#334155';
            const highlightBg = (document.getElementById('inp-highlight-color') ? document.getElementById('inp-highlight-color').value : '') || '#eff6ff';
            const btnTextColor = (document.getElementById('inp-btn-text-color') ? document.getElementById('inp-btn-text-color').value : '') || '#ffffff';

            const activePreset = BRAND_PRESETS.find(p => p.primary.toLowerCase() === themeColor.toLowerCase()) || BRAND_PRESETS[activeBrandPresetIndex] || BRAND_PRESETS[0];
            const highlightBorder = activePreset.highlightBorder || '#cbd5e1';
            const highlightText = activePreset.highlightText || '#1e40af';
            const textMuted = activePreset.textMuted || '#64748b';
            const cardBorder = activePreset.cardBorder || '#e2e8f0';

            // Visual Design & Layout Styler Controls
            const fontFamily = (document.getElementById('inp-font-family') ? document.getElementById('inp-font-family').value : '') || 'Arial, Helvetica, sans-serif';
            const btnRadius = (document.getElementById('inp-btn-radius') ? document.getElementById('inp-btn-radius').value : '') || '6px';
            const btnWidth = (document.getElementById('inp-btn-width') ? document.getElementById('inp-btn-width').value : '') || 'auto';
            const headerStyle = (document.getElementById('inp-header-style') ? document.getElementById('inp-header-style').value : '') || 'minimal';
            const logoSize = (document.getElementById('inp-logo-size') ? document.getElementById('inp-logo-size').value : '') || '48';
            const logoAlign = currentLogoAlign || 'center';

            let preheader = (document.getElementById('inp-preheader').value || '').trim();
            let subject = document.getElementById('inp-subject').value || '';
            let headline = document.getElementById('inp-headline').value || '';
            let greeting = document.getElementById('inp-greeting').value || 'Dear Parents,';
            let rawBody = document.getElementById('inp-body').value || '';

            let includeNotice = document.getElementById('inp-include-notice') ? document.getElementById('inp-include-notice').checked : false;
            let noticeText = document.getElementById('inp-notice-text') ? document.getElementById('inp-notice-text').value : '';
            let includeRoadmap = document.getElementById('inp-include-roadmap') ? document.getElementById('inp-include-roadmap').checked : false;
            let includeLogin = document.getElementById('inp-include-login').checked;
            let loginPrompt = document.getElementById('inp-login-prompt').value || 'Complete your Application Form using your Candidate Portal credentials below:';
            let buttonText = document.getElementById('inp-button-text').value || 'ADMISSION PORTAL LOGIN';
            let signoffTeam = document.getElementById('inp-signoff-team').value || 'Team Admissions';

            const fb = (document.getElementById('inp-soc-fb').value || '').trim();
            const insta = (document.getElementById('inp-soc-insta').value || '').trim();
            const twitter = (document.getElementById('inp-soc-twitter').value || '').trim();
            const li = (document.getElementById('inp-soc-linkedin').value || '').trim();
            const yt = (document.getElementById('inp-soc-yt').value || '').trim();
            const wa = (document.getElementById('inp-soc-wa') ? document.getElementById('inp-soc-wa').value : '').trim();
            const phone = (document.getElementById('inp-campus-phone') ? document.getElementById('inp-campus-phone').value : '').trim();
            const email = (document.getElementById('inp-campus-email') ? document.getElementById('inp-campus-email').value : '').trim();
            const timings = (document.getElementById('inp-campus-timings') ? document.getElementById('inp-campus-timings').value : '').trim();

            // Zero-emoticon sanitizer
            const stripEmojis = (str) => (str || '').replace(/[\\u{{1F300}}-\\u{{1F9FF}}\\u{{2600}}-\\u{{26FF}}\\u{{2700}}-\\u{{27BF}}\\u{{1F1E6}}-\\u{{1F1FF}}\\u{{1FA00}}-\\u{{1FAFF}}]/gu, '').trim();
            subject = stripEmojis(subject);
            headline = stripEmojis(headline);
            greeting = stripEmojis(greeting);
            buttonText = stripEmojis(buttonText);

            // Preheader snippet
            let preheaderHTML = '';
            if (preheader) {{
                preheaderHTML = `<span style="display:none; font-size:1px; color:#ffffff; line-height:1px; max-height:0px; max-width:0px; opacity:0; overflow:hidden;">${{preheader}}</span>`;
            }}

            // Top Notice Strip
            let noticeHTML = '';
            if (includeNotice && noticeText) {{
                noticeHTML = `
        <tr>
          <td bgcolor="${{highlightBg}}" style="padding: 10px 20px; background-color: ${{highlightBg}}; border-bottom: 1px solid ${{highlightBorder}}; font-family: ${{fontFamily}}; font-size: 12px; color: ${{headlineColor}}; text-align: center; font-weight: bold;">
            ${{noticeText}}
          </td>
        </tr>`;
            }}

            // Top Header Logo & Styler Layout
            const logoAlignTd = logoAlign === 'left' ? 'left' : 'center';
            const logoImgMargin = logoAlign === 'left' ? '0' : '0 auto';
            const headerBgColor = headerStyle === 'hero' ? themeColor : cardBgColor;
            const headerTextColor = headerStyle === 'hero' ? btnTextColor : headlineColor;
            const headerBorderBottom = headerStyle === 'hero' ? 'none' : `1px solid ${{highlightBorder}}`;

            let headerLogoHTML = '';
            if (logoLink) {{
                headerLogoHTML = `
        <tr>
          <td align="${{logoAlignTd}}" style="padding: 24px 24px 20px; background-color: ${{headerBgColor}}; border-bottom: ${{headerBorderBottom}};">
            <a href="${{websiteUrl}}" target="_blank" style="text-decoration: none;">
              <img src="${{logoLink}}" alt="${{campusName}}" border="0" style="display: block; max-height: ${{logoSize}}px; max-width: 240px; width: auto; height: auto; margin: ${{logoImgMargin}}; outline: none; border: none; text-decoration: none;" />
            </a>
          </td>
        </tr>`;
            }} else {{
                headerLogoHTML = `
        <tr>
          <td align="${{logoAlignTd}}" style="padding: 22px 24px 18px; background-color: ${{headerBgColor}}; border-bottom: ${{headerBorderBottom}};">
            <h2 style="margin: 0; font-family: ${{fontFamily}}; font-size: 20px; font-weight: bold; color: ${{headerTextColor}};">
              ${{campusName}}
            </h2>
          </td>
        </tr>`;
            }}

            // 3-Step Milestone Roadmap
            let roadmapHTML = '';
            if (includeRoadmap) {{
                roadmapHTML = `
                <table width="100%" border="0" cellpadding="0" cellspacing="0" style="margin: 20px 0; background-color: ${{highlightBg}}; border: 1px solid ${{highlightBorder}}; border-radius: ${{btnRadius}};">
                  <tr>
                    <td align="center" style="padding: 14px 10px; font-family: ${{fontFamily}};">
                      <table border="0" cellpadding="0" cellspacing="0" width="100%">
                        <tr>
                          <td align="center" width="33%" style="font-size: 11px; font-weight: bold; color: ${{themeColor}};">
                            <div style="display:inline-block; width:22px; height:22px; line-height:22px; background:${{themeColor}}; color:${{btnTextColor}}; border-radius:50%; margin-bottom:4px;">1</div><br/>Registration
                          </td>
                          <td align="center" width="33%" style="font-size: 11px; font-weight: bold; color: ${{textMuted}};">
                            <div style="display:inline-block; width:22px; height:22px; line-height:22px; background:${{highlightBorder}}; color:${{textMuted}}; border-radius:50%; margin-bottom:4px;">2</div><br/>Verification
                          </td>
                          <td align="center" width="33%" style="font-size: 11px; font-weight: bold; color: ${{textMuted}};">
                            <div style="display:inline-block; width:22px; height:22px; line-height:22px; background:${{highlightBorder}}; color:${{textMuted}}; border-radius:50%; margin-bottom:4px;">3</div><br/>Admission Offer
                          </td>
                        </tr>
                      </table>
                    </td>
                  </tr>
                </table>`;
            }}

            // Body Paragraphs
            const paragraphs = rawBody.split('\\n\\n').filter(p => p.trim().length > 0);
            let bodyHTML = paragraphs.map(p => {{
                const formatted = p.replace(/\\n/g, '<br/>');
                return `<p style="margin: 0 0 16px 0; font-family: ${{fontFamily}}; font-size: 14px; line-height: 1.65; color: ${{textBodyColor}};">${{formatted}}</p>`;
            }}).join('\\n');

            // Synchronize highlight blocks, OTP pill, and buttons in body
            bodyHTML = bodyHTML
                .replace(/background-color:\s*#[a-fA-F0-9]+;\s*color:\s*#[a-fA-F0-9]+;/g, `background-color: ${{highlightBg}}; color: ${{highlightText}};`)
                .replace(/border:\s*1px solid #[a-fA-F0-9]+;/g, `border: 1px solid ${{highlightBorder}};`)
                .replace(/background-color:\s*#11a14a;\s*color:\s*#ffffff;/g, `background-color: ${{themeColor}}; color: ${{btnTextColor}};`)
                .replace(/color:\s*#11a14a;/g, `color: ${{themeColor}};`);

            // Button styling helper
            const btnDisplay = btnWidth === '100%' ? 'display: block; width: 100%; text-align: center; box-sizing: border-box;' : 'display: inline-block;';

            // Pure CSS Credentials Box
            let loginBoxHTML = '';
            if (includeLogin) {{
                loginBoxHTML = `
                <table width="100%" border="0" cellpadding="0" cellspacing="0" style="margin: 20px 0; background-color: ${{highlightBg}}; border: 1px solid ${{highlightBorder}}; border-left: 4px solid ${{themeColor}}; border-radius: ${{btnRadius}};">
                  <tr>
                    <td style="padding: 16px 20px; font-family: ${{fontFamily}}; font-size: 13px; color: ${{textBodyColor}}; line-height: 1.6;">
                      <div style="font-weight: bold; color: ${{headlineColor}}; margin-bottom: 6px; text-transform: uppercase; letter-spacing: 0.5px; font-size: 12px;">ADMISSION PORTAL LOGIN</div>
                      <div style="margin-bottom: 10px; color: ${{textMuted}}; font-size: 13px;">${{loginPrompt}}</div>
                      <table border="0" cellpadding="4" cellspacing="0" style="font-family: ${{fontFamily}}; font-size: 13px; color: ${{textBodyColor}};">
                        <tr>
                          <td style="font-weight: bold; width: 110px; color: ${{textMuted}};">Portal URL:</td>
                          <td><a href="${{portalUrl}}" target="_blank" style="color: ${{themeColor}}; font-weight: bold; text-decoration: underline;">${{portalUrl}}</a></td>
                        </tr>
                        <tr>
                          <td style="font-weight: bold; color: ${{textMuted}};">Username:</td>
                          <td><span style="font-family: monospace; background-color: ${{highlightBorder}}; padding: 2px 7px; border-radius: 4px; font-size: 12px; color: ${{highlightText}};">{{{{username}}}}</span></td>
                        </tr>
                        <tr>
                          <td style="font-weight: bold; color: ${{textMuted}};">Password:</td>
                          <td><span style="font-family: monospace; background-color: ${{highlightBorder}}; padding: 2px 7px; border-radius: 4px; font-size: 12px; color: ${{highlightText}};">{{{{passwords}}}}</span></td>
                        </tr>
                      </table>
                      <div style="margin-top: 14px;">
                        <a href="${{portalUrl}}" target="_blank" style="${{btnDisplay}} padding: 11px 24px; background-color: ${{themeColor}}; color: ${{btnTextColor}}; text-decoration: none; border-radius: ${{btnRadius}}; font-weight: bold; font-size: 13px; letter-spacing: 0.5px; font-family: ${{fontFamily}};">
                          ${{buttonText}} &rarr;
                        </a>
                      </div>
                    </td>
                  </tr>
                </table>`;
            }}

            // Footer: ONLY social links, Google Maps link, and Website link (CDN icons)
            const footerIcons = [];
            if (wa) footerIcons.push(`<td align="center" style="padding: 0 8px;"><a href="${{wa}}" target="_blank" title="WhatsApp Admissions Helpline"><img src="https://img.icons8.com/color/48/whatsapp--v1.png" alt="WhatsApp" width="28" height="28" border="0" style="display:block; width:28px; height:28px;" /></a></td>`);
            if (fb) footerIcons.push(`<td align="center" style="padding: 0 8px;"><a href="${{fb}}" target="_blank" title="Facebook"><img src="https://img.icons8.com/color/48/facebook-new.png" alt="Facebook" width="28" height="28" border="0" style="display:block; width:28px; height:28px;" /></a></td>`);
            if (insta) footerIcons.push(`<td align="center" style="padding: 0 8px;"><a href="${{insta}}" target="_blank" title="Instagram"><img src="https://img.icons8.com/color/48/instagram-new--v1.png" alt="Instagram" width="28" height="28" border="0" style="display:block; width:28px; height:28px;" /></a></td>`);
            if (twitter) footerIcons.push(`<td align="center" style="padding: 0 8px;"><a href="${{twitter}}" target="_blank" title="Twitter"><img src="https://img.icons8.com/color/48/twitter--v1.png" alt="Twitter" width="28" height="28" border="0" style="display:block; width:28px; height:28px;" /></a></td>`);
            if (li) footerIcons.push(`<td align="center" style="padding: 0 8px;"><a href="${{li}}" target="_blank" title="LinkedIn"><img src="https://img.icons8.com/color/48/linkedin.png" alt="LinkedIn" width="28" height="28" border="0" style="display:block; width:28px; height:28px;" /></a></td>`);
            if (yt) footerIcons.push(`<td align="center" style="padding: 0 8px;"><a href="${{yt}}" target="_blank" title="YouTube"><img src="https://img.icons8.com/color/48/youtube-play.png" alt="YouTube" width="28" height="28" border="0" style="display:block; width:28px; height:28px;" /></a></td>`);

            footerIcons.push(`<td align="center" style="padding: 0 8px;"><a href="${{locationLink}}" target="_blank" title="Google Map"><img src="https://img.icons8.com/color/48/google-maps-new.png" alt="Google Map" width="28" height="28" border="0" style="display:block; width:28px; height:28px;" /></a></td>`);
            footerIcons.push(`<td align="center" style="padding: 0 8px;"><a href="${{websiteUrl}}" target="_blank" title="Website"><img src="https://img.icons8.com/color/48/domain--v1.png" alt="Website" width="28" height="28" border="0" style="display:block; width:28px; height:28px;" /></a></td>`);

            const footerIconsHTML = `
            <table border="0" cellpadding="0" cellspacing="0" align="center" style="margin: 0 auto;">
              <tr>
                ${{footerIcons.join('\\n                ')}}
              </tr>
            </table>`;

            let helplineInfoHTML = '';
            if (phone || email) {{
                const contactParts = [];
                if (phone) contactParts.push(`Tel: ${{phone}}`);
                if (email) contactParts.push(`Email: ${{email}}`);
                if (timings) contactParts.push(`Hours: ${{timings}}`);
                helplineInfoHTML = `<div style="margin-top: 8px; font-size: 12px; color: ${{textMuted}}; font-family: ${{fontFamily}};">${{contactParts.join(' &bull; ')}}</div>`;
            }}

            let templateHTML = `<!--
================================================================================
EMAIL SUBJECT: ${{subject}}
================================================================================
-->
${{preheaderHTML}}
<table width="100%" border="0" cellpadding="0" cellspacing="0" bgcolor="${{bgColor}}" style="background-color: ${{bgColor}}; margin: 0; padding: 25px 0; font-family: ${{fontFamily}};">
  <tr>
    <td align="center" valign="top">
      <table width="600" border="0" cellpadding="0" cellspacing="0" bgcolor="${{cardBgColor}}" style="width: 100%; max-width: 600px; background-color: ${{cardBgColor}}; border-radius: ${{btnRadius}}; overflow: hidden; border: 1px solid ${{cardBorder}};">
        <tr>
          <td height="4" bgcolor="${{themeColor}}" style="height: 4px; background-color: ${{themeColor}}; font-size: 1px; line-height: 1px;">&nbsp;</td>
        </tr>
        ${{noticeHTML}}
        ${{headerLogoHTML}}
        <tr>
          <td align="left" style="padding: 30px 30px 24px; font-family: ${{fontFamily}}; font-size: 14px; line-height: 1.65; color: ${{textBodyColor}};">
            <p style="margin: 0 0 16px 0; font-size: 16px; font-weight: bold; color: ${{headlineColor}};">
              ${{headline}}
            </p>
            <p style="margin: 0 0 16px 0; font-size: 14px; line-height: 1.6; color: ${{textBodyColor}};">
              ${{greeting}}
            </p>
            ${{roadmapHTML}}
            ${{bodyHTML}}
            ${{loginBoxHTML}}
            <p style="margin: 22px 0 0 0; font-size: 14px; line-height: 1.6; color: ${{textBodyColor}};">
              Warm regards,<br />
              <strong>${{signoffTeam}}</strong><br />
              <span style="color: ${{textMuted}}; font-size: 13px;">${{campusName}}</span>
              ${{helplineInfoHTML}}
            </p>
          </td>
        </tr>
        <tr>
          <td style="padding: 0 30px;">
            <table width="100%" border="0" cellpadding="0" cellspacing="0">
              <tr>
                <td height="1" bgcolor="${{highlightBorder}}" style="height: 1px; background-color: ${{highlightBorder}}; font-size: 1px; line-height: 1px;">&nbsp;</td>
              </tr>
            </table>
          </td>
        </tr>
        <tr>
          <td align="center" style="padding: 20px 20px 22px; background-color: ${{highlightBg}};">
            ${{footerIconsHTML}}
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>`;

            // Replace Sample Data if enabled
            if (useSampleData) {{
                for (const [cat, vars] of Object.entries(CRM_VARIABLES_CATALOG)) {{
                    for (const v of vars) {{
                        const regex = new RegExp(`{{{{${{v.key}}}}}}`, 'g');
                        let sampleVal = (customSampleOverrides && customSampleOverrides[v.key]) ? customSampleOverrides[v.key] : v.sample;
                        if (v.key === 'school_name') sampleVal = campusName;
                        if (v.key === 'school_url') sampleVal = websiteUrl;
                        templateHTML = templateHTML.replace(regex, sampleVal);
                    }}
                }}
            }}

            return templateHTML;
        }}

        function rebuildPreview() {{
            pushUndoState();
            const isSample = document.getElementById('inp-sample-toggle').checked;
            const html = generateEmailHTML(isSample);
            const frame = document.getElementById('live-iframe');
            if (frame) frame.srcdoc = html;

            // Dual View sync
            if (currentViewport === 'dual') {{
                const deskFrame = document.getElementById('live-iframe-desktop');
                const mobFrame = document.getElementById('live-iframe-mobile');
                if (deskFrame) deskFrame.srcdoc = html;
                if (mobFrame) mobFrame.srcdoc = html;
            }}

            if (isLiveEditActive) {{
                setTimeout(attachLiveEditListeners, 150);
            }}

            updateReadinessScore();
            setAutosaveStatus('Saving...');
            setTimeout(() => setAutosaveStatus('Saved'), 350);
        }}

        function updateShellPreview() {{
            const html = generateEmailHTML(true);
            const frame = document.getElementById('shell-live-iframe');
            if (frame) frame.srcdoc = html;
        }}

        // Copy & Download Actions
        function copySubject() {{
            const subj = document.getElementById('inp-subject').value || '';
            navigator.clipboard.writeText(subj).then(() => showToast('Subject line copied!'));
        }}

        async function copyFormattedForGmail() {{
            try {{
                const isSample = document.getElementById('inp-sample-toggle').checked;
                const html = generateEmailHTML(isSample);
                const textContent = document.getElementById('inp-body').value || 'Admission Email';
                const blobHtml = new Blob([html], {{ type: 'text/html' }});
                const blobText = new Blob([textContent], {{ type: 'text/plain' }});
                const item = new ClipboardItem({{
                    'text/html': blobHtml,
                    'text/plain': blobText
                }});
                await navigator.clipboard.write([item]);
                showToast('Copied formatted email! Paste directly into Gmail / Outlook with Ctrl+V');
            }} catch (err) {{
                const frame = document.getElementById('live-iframe');
                if (frame && frame.contentWindow) {{
                    try {{
                        frame.contentWindow.focus();
                        frame.contentDocument.execCommand('selectAll', false, null);
                        frame.contentDocument.execCommand('copy', false, null);
                        showToast('Copied formatted email! Paste into Gmail / Outlook (Ctrl+V)');
                        return;
                    }} catch(e) {{}}
                }}
                copyHTML();
                showToast('HTML copied to clipboard!');
            }}
        }}

        function printTemplate() {{
            const frame = document.getElementById('live-iframe');
            if (frame && frame.contentWindow) {{
                frame.contentWindow.focus();
                frame.contentWindow.print();
            }} else {{
                window.print();
            }}
        }}

        let customSampleOverrides = {{}};

        function onCustomTestDataChange() {{
            customSampleOverrides = {{
                'student_name': document.getElementById('cust-student-name').value || 'Aarav Sharma',
                'student_class': document.getElementById('cust-student-class').value || 'Grade 1',
                'father_name': document.getElementById('cust-parent-name').value || 'Mr. Vikram Sharma',
                'current_fee_receipt_amount': document.getElementById('cust-fee-amount').value || '₹ 2,500',
                'current_fee_receipt_head_amount': document.getElementById('cust-fee-amount').value || '₹ 2,500',
                'otp': document.getElementById('cust-otp-code').value || '482910',
                'application_no': document.getElementById('cust-app-no').value || 'APP-2026-8941'
            }};
            rebuildPreview();
        }}

        function resetCustomTestData() {{
            document.getElementById('cust-student-name').value = 'Aarav Sharma';
            document.getElementById('cust-student-class').value = 'Grade 1';
            document.getElementById('cust-parent-name').value = 'Mr. Vikram Sharma';
            document.getElementById('cust-fee-amount').value = '₹ 2,500';
            document.getElementById('cust-otp-code').value = '482910';
            document.getElementById('cust-app-no').value = 'APP-2026-8941';
            customSampleOverrides = {{}};
            rebuildPreview();
            showToast('Reset sample test values to defaults');
        }}

        function toggleSampleCustomizer() {{
            const card = document.getElementById('sample-customizer-card');
            const btn = document.getElementById('btn-custom-sample-toggle');
            if (card.style.display === 'none') {{
                card.style.display = 'block';
                btn.classList.add('active');
            }} else {{
                card.style.display = 'none';
                btn.classList.remove('active');
            }}
        }}

        function updateReadinessScore() {{
            const subj = (document.getElementById('inp-subject').value || '').trim();
            const preheader = (document.getElementById('inp-preheader').value || '').trim();
            const body = (document.getElementById('inp-body').value || '').trim();
            const btnText = (document.getElementById('inp-button-text').value || '').trim();

            let score = 0;
            let issues = [];

            if (subj.length > 0 && subj.length <= 55) {{
                score += 25;
            }} else if (subj.length > 55) {{
                score += 15;
                issues.push('Subject > 55 chars');
            }} else {{
                issues.push('Missing Subject');
            }}

            if (preheader.length > 0) {{
                score += 25;
            }} else {{
                issues.push('No Preheader');
            }}

            if (btnText.length > 0) {{
                score += 25;
            }} else {{
                issues.push('No CTA text');
            }}

            const brokenRegex = /{{{{[^}}]*$/m;
            if (!brokenRegex.test(body)) {{
                score += 25;
            }} else {{
                issues.push('Unclosed {{ tag');
            }}

            const badge = document.getElementById('readiness-meter-badge');
            if (badge) {{
                if (score === 100) {{
                    badge.className = 'readiness-meter';
                    badge.style.color = '#34d399';
                    badge.style.borderColor = 'rgba(16, 185, 129, 0.3)';
                    badge.innerHTML = '🟢 100% Ready';
                }} else if (score >= 60) {{
                    badge.className = 'readiness-meter warning';
                    badge.style.color = '#fbbf24';
                    badge.style.borderColor = 'rgba(245, 158, 11, 0.3)';
                    badge.innerHTML = `🟡 ${{score}}% (${{issues[0]}})`;
                }} else {{
                    badge.className = 'readiness-meter warning';
                    badge.style.color = '#ef4444';
                    badge.style.borderColor = 'rgba(239, 68, 68, 0.3)';
                    badge.innerHTML = `🔴 ${{score}}% (${{issues[0]}})`;
                }}
            }}
        }}

        function showReadinessToast() {{
            const subj = (document.getElementById('inp-subject').value || '').trim();
            const preheader = (document.getElementById('inp-preheader').value || '').trim();
            showToast(`Readiness: ${{subj ? '✅ Subject' : '❌ No Subject'}} • ${{preheader ? '✅ Preheader' : '⚠️ No Preheader'}}`);
        }}

        function copyHTML() {{
            const html = generateEmailHTML(false);
            navigator.clipboard.writeText(html).then(() => showToast('Clean production HTML copied!'));
        }}

        function downloadHTML() {{
            const html = generateEmailHTML(false);
            const blob = new Blob([html], {{ type: 'text/html;charset=utf-8' }});
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            const scenario = document.getElementById('inp-template-selector').value || 'email_template';
            a.href = url;
            a.download = `${{scenario}}.html`;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);
            showToast('Template downloaded!');
        }}

        // Bulk ZIP Export
        async function exportAllAsZip() {{
            if (typeof JSZip === 'undefined') {{
                showToast('JSZip library loading...');
                return;
            }}
            const zip = new JSZip();
            const campusName = document.getElementById('inp-campus-name').value || 'Simply_Admission';
            showToast('Packaging 22 templates into ZIP...');

            const originalSelect = document.getElementById('inp-template-selector').value;

            CANONICAL_TEMPLATES.forEach(t => {{
                loadCanonicalTemplate(t);
                const html = generateEmailHTML(false);
                zip.file(`${{t.id}}.html`, html);
            }});

            // Restore original selection
            document.getElementById('inp-template-selector').value = originalSelect;
            onTemplateSelect(originalSelect);

            const content = await zip.generateAsync({{ type: 'blob' }});
            const url = URL.createObjectURL(content);
            const a = document.createElement('a');
            a.href = url;
            a.download = `${{campusName.replace(/\\s+/g, '_')}}_Admission_Templates.zip`;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);
            showToast('ZIP Bundle Downloaded!');
        }}

        // Bulk CRM CSV Export
        function exportCrmCsv() {{
            const campusName = document.getElementById('inp-campus-name').value || 'Simply Admission';
            let csvRows = ['"Scenario ID","Alert Name","Category","Subject","Primary Button"'];

            CANONICAL_TEMPLATES.forEach(t => {{
                const row = [
                    `"${{t.id}}"`,
                    `"${{t.name}}"`,
                    `"${{t.category || ''}}"`,
                    `"${{(t.subject || '').replace(/"/g, '""')}}"`,
                    `"${{(t.button_text || '').replace(/"/g, '""')}}"`
                ];
                csvRows.push(row.join(','));
            }});

            const csvString = csvRows.join('\\n');
            const blob = new Blob([csvString], {{ type: 'text/csv;charset=utf-8' }});
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = `${{campusName.replace(/\\s+/g, '_')}}_CRM_Alerts.csv`;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);
            showToast('CRM CSV Exported!');
        }}

        function openCodeModal() {{
            const html = generateEmailHTML(false);
            document.getElementById('modal-code-content').textContent = html;
            document.getElementById('code-modal').classList.add('show');
        }}

        function closeCodeModal() {{
            document.getElementById('code-modal').classList.remove('show');
        }}

        // Command Palette (Ctrl+K)
        function openCommandPalette() {{
            document.getElementById('cmd-modal').classList.add('show');
            const inp = document.getElementById('cmd-search-inp');
            inp.value = '';
            inp.focus();
            renderCmdResults('');
        }}

        function closeCommandPalette() {{
            document.getElementById('cmd-modal').classList.remove('show');
        }}

        function onCmdSearch(query) {{
            renderCmdResults(query.trim().toLowerCase());
        }}

        function renderCmdResults(q) {{
            const list = document.getElementById('cmd-results-list');
            list.innerHTML = '';

            let matches = [];
            CANONICAL_TEMPLATES.forEach(t => {{
                if (!q || t.name.toLowerCase().includes(q) || t.subject.toLowerCase().includes(q)) {{
                    matches.push({{ type: 'scenario', id: t.id, title: t.name, sub: t.category }});
                }}
            }});

            if (Object.keys(CLIENT_CAMPUSES).length > 1) {{
                Object.keys(CLIENT_CAMPUSES).forEach(cName => {{
                    if (!q || cName.toLowerCase().includes(q)) {{
                        matches.push({{ type: 'campus', id: cName, title: `Switch Campus: ${{cName}}`, sub: 'Brand Preset' }});
                    }}
                }});
            }}

            BRAND_PRESETS.forEach((bp, idx) => {{
                if (!q || bp.name.toLowerCase().includes(q) || 'theme'.includes(q) || 'palette'.includes(q)) {{
                    matches.push({{ type: 'theme', id: idx, title: `Theme: ${{bp.name}}`, sub: `${{bp.primary}} • Synchronized Palette` }});
                }}
            }});

            matches.slice(0, 10).forEach(m => {{
                const div = document.createElement('div');
                div.className = 'cmd-item';
                div.innerHTML = `<span><strong>${{m.title}}</strong></span> <span style="font-size:0.68rem; color:#94a3b8;">${{m.sub}}</span>`;
                div.onclick = () => {{
                    if (m.type === 'scenario') {{
                        switchView('studio');
                        document.getElementById('inp-template-selector').value = m.id;
                        onTemplateSelect(m.id);
                    }} else if (m.type === 'campus') {{
                        applyCampusPreset(m.id);
                    }} else if (m.type === 'theme') {{
                        applyBrandPreset(m.id);
                    }}
                    closeCommandPalette();
                }};
                list.appendChild(div);
            }});
        }}

        // Template Library Functions (Paginated & Searchable)
        let allArchiveTemplates = [];
        let filteredArchiveTemplates = [];
        let currentArchivePage = 1;
        const ARCHIVE_PAGE_SIZE = 8;

        function populateArchiveList() {{
            allArchiveTemplates = [];
            for (const [cName, cData] of Object.entries(CLIENTS_DATA)) {{
                (cData.templates || []).forEach(t => {{
                    allArchiveTemplates.push({{
                        client: cName,
                        file: t.file,
                        subject: t.subject,
                        content: t.raw_content
                    }});
                }});
            }}
            filteredArchiveTemplates = [...allArchiveTemplates];
            currentArchivePage = 1;
            renderArchivePagedList();

            if (filteredArchiveTemplates.length > 0) {{
                activeArchiveItem = filteredArchiveTemplates[0];
            }}
        }}

        function renderArchivePagedList() {{
            const container = document.getElementById('archive-items-container');
            const pageInfo = document.getElementById('archive-page-info');
            const btnPrev = document.getElementById('btn-archive-prev');
            const btnNext = document.getElementById('btn-archive-next');
            if (!container) return;
            container.innerHTML = '';

            const totalPages = Math.max(1, Math.ceil(filteredArchiveTemplates.length / ARCHIVE_PAGE_SIZE));
            if (currentArchivePage > totalPages) currentArchivePage = totalPages;
            if (currentArchivePage < 1) currentArchivePage = 1;

            if (pageInfo) {{
                pageInfo.textContent = `Page ${{currentArchivePage}} of ${{totalPages}} (${{filteredArchiveTemplates.length}} total)`;
            }}
            if (btnPrev) btnPrev.disabled = (currentArchivePage <= 1);
            if (btnNext) btnNext.disabled = (currentArchivePage >= totalPages);

            const startIdx = (currentArchivePage - 1) * ARCHIVE_PAGE_SIZE;
            const endIdx = startIdx + ARCHIVE_PAGE_SIZE;
            const pageItems = filteredArchiveTemplates.slice(startIdx, endIdx);

            if (pageItems.length === 0) {{
                container.innerHTML = '<div style="padding:16px; text-align:center; color:var(--text-dim); font-size:0.75rem;">No templates found</div>';
                return;
            }}

            pageItems.forEach((item, idx) => {{
                const card = document.createElement('div');
                const isSelected = activeArchiveItem && activeArchiveItem.file === item.file && activeArchiveItem.client === item.client;
                card.className = `archive-card ${{isSelected ? 'active' : ''}}`;
                card.innerHTML = `
                    <div class="archive-card-name">${{item.file}}</div>
                    <div class="archive-card-sub">${{item.client}} &bull; ${{item.subject || 'No Subject'}}</div>
                `;
                card.onclick = () => selectArchiveItem(item, card);
                container.appendChild(card);
            }});
        }}

        function stepArchivePage(direction) {{
            const totalPages = Math.max(1, Math.ceil(filteredArchiveTemplates.length / ARCHIVE_PAGE_SIZE));
            const newPage = currentArchivePage + direction;
            if (newPage >= 1 && newPage <= totalPages) {{
                currentArchivePage = newPage;
                renderArchivePagedList();
            }}
        }}

        function selectFirstArchiveItem() {{
            const firstCard = document.querySelector('.archive-card');
            if (firstCard) firstCard.click();
        }}

        function selectArchiveItem(item, cardEl) {{
            activeArchiveItem = item;
            document.querySelectorAll('.archive-card').forEach(c => c.classList.remove('active'));
            if (cardEl) cardEl.classList.add('active');

            document.getElementById('archive-current-title').textContent = `${{item.client}} / ${{item.file}}`;
            const frame = document.getElementById('archive-live-iframe');
            if (frame) frame.srcdoc = item.content;
        }}

        function filterArchiveList(query) {{
            const q = query.toLowerCase().trim();
            if (!q) {{
                filteredArchiveTemplates = [...allArchiveTemplates];
            }} else {{
                filteredArchiveTemplates = allArchiveTemplates.filter(item => {{
                    return item.file.toLowerCase().includes(q) ||
                           item.client.toLowerCase().includes(q) ||
                           (item.subject && item.subject.toLowerCase().includes(q));
                }});
            }}
            currentArchivePage = 1;
            renderArchivePagedList();
        }}

        function loadArchiveIntoStudio() {{
            if (!activeArchiveItem) return;
            switchView('studio');
            document.getElementById('inp-template-selector').value = 'custom';
            if (activeArchiveItem.subject) document.getElementById('inp-subject').value = activeArchiveItem.subject;
            rebuildPreview();
            showToast('Template loaded into Studio!');
        }}

        function copyArchiveSubject() {{
            if (!activeArchiveItem) return;
            navigator.clipboard.writeText(activeArchiveItem.subject || '').then(() => showToast('Subject copied!'));
        }}

        function copyArchiveHTML() {{
            if (!activeArchiveItem) return;
            navigator.clipboard.writeText(activeArchiveItem.content || '').then(() => showToast('Archive HTML copied!'));
        }}

        // AI Generator Mockup
        function runAiGenerator() {{
            const prompt = document.getElementById('ai-prompt').value || 'Admission Notification';
            const campusName = document.getElementById('inp-campus-name').value || 'Simply Admission';
            const html = generateEmailHTML(true);
            const frame = document.getElementById('ai-live-iframe');
            if (frame) frame.srcdoc = html;
            showToast('Campaign draft generated!');
        }}

        function loadAiIntoStudio() {{
            switchView('studio');
            showToast('AI Draft loaded into Studio!');
        }}

        // ═══════════════════════════════════════════════════════════
        // GUIDED INTERACTIVE TUTORIAL / ONBOARDING WALKTHROUGH
        // ═══════════════════════════════════════════════════════════
        let currentTutorialStep = 0;
        const TUTORIAL_STEPS = [
            {{
                title: "🎓 Welcome to Email Template Designer",
                badge: "Step 1: Mission & Architecture",
                body: `<p style="margin-bottom:12px; line-height:1.6; color:#cbd5e1;">Welcome! This enterprise suite empowers school admissions teams to craft <strong>100% email-client-proof</strong> notification templates. Every template uses bulletproof HTML table architecture, pure CSS layouts, zero emoticons, and high-resolution CDN icons that render flawlessly across Gmail, Apple Mail, and legacy Outlook.</p>
                <div style="background:rgba(37,99,235,0.15); border:1px solid rgba(56,189,248,0.3); border-radius:8px; padding:12px; font-size:0.75rem; color:#93c5fd;">
                  💡 <strong>Key Guarantee:</strong> Clean, uncluttered emails. The footer strictly features verified social links, Google Maps, and School Website icons.
                </div>`
            }},
            {{
                title: "🏫 Campus Brand Kit & One-Click Presets",
                badge: "Step 2: Brand Identity",
                body: `<p style="margin-bottom:12px; line-height:1.6; color:#cbd5e1;">Switch seamlessly between client campuses using the top pill bar or customize primary theme colors and background tints. Choose from 6 curated palettes like <em>Simply Blue</em>, <em>Emerald Academy</em>, or <em>Royal Indigo</em>.</p>
                <div style="background:rgba(16,185,129,0.15); border:1px solid rgba(16,185,129,0.3); border-radius:8px; padding:12px; font-size:0.75rem; color:#a7f3d0;">
                  🏫 <strong>Automatic Branding:</strong> Logos, candidate portal URLs, school addresses, and social channels update instantly across all alert templates.
                </div>`
            }},
            {{
                title: "⚡ 22 Pre-Mapped Alert Scenarios",
                badge: "Step 3: Admission Workflows",
                body: `<p style="margin-bottom:12px; line-height:1.6; color:#cbd5e1;">Select from 22 canonical admission scenarios filtered by category: <strong>🔑 Authentication</strong>, <strong>📝 Enquiry</strong>, <strong>📅 Campus Visits</strong>, <strong>💳 Fee Receipts</strong>, and <strong>🎓 Application Milestones</strong>.</p>
                <div style="background:rgba(245,158,11,0.15); border:1px solid rgba(245,158,11,0.3); border-radius:8px; padding:12px; font-size:0.75rem; color:#fde68a;">
                  ⚡ <strong>Power Tip:</strong> Cycle scenarios in 1 second using the <code>[</code> and <code>]</code> keyboard shortcuts, or press <code>Ctrl+K</code> to jump anywhere.
                </div>`
            }},
            {{
                title: "🏷️ 68 CRM Merge Variables & Component Inserters",
                badge: "Step 4: Dynamic Personalization",
                body: `<p style="margin-bottom:12px; line-height:1.6; color:#cbd5e1;">Insert student names, fee receipts, OTPs, or candidate credentials with 1 click. Expand the <strong>Explore All 68 Keys</strong> drawer or use the toolbar to insert Fee Tables, Interaction Schedules, or Document Checklists.</p>
                <div style="background:rgba(147,51,234,0.15); border:1px solid rgba(147,51,234,0.3); border-radius:8px; padding:12px; font-size:0.75rem; color:#d8b4fe;">
                  🔍 <strong>Smart Linter:</strong> Detects unclosed braces or invalid syntax in real time, with instant reading-time estimators and character counters.
                </div>`
            }},
            {{
                title: "🎨 Visual Styler, In-Preview Edit & 1-Click Export",
                badge: "Step 5: Visual Styling & Production",
                body: `<p style="margin-bottom:12px; line-height:1.6; color:#cbd5e1;">Use the <strong>Visual Design & Layout Styler</strong> to change typography, button pill radius, or logo alignment. Switch to <strong>🖥️+📱 Dual View</strong> to see Desktop (640px) and Mobile (375px) side-by-side, or click <strong>✏️ Live Edit</strong> to edit text directly inside the preview!</p>
                <div style="background:rgba(6,182,212,0.15); border:1px solid rgba(6,182,212,0.3); border-radius:8px; padding:12px; font-size:0.75rem; color:#a5f3fc;">
                  🚀 <strong>Export Options:</strong> Copy formatted emails to Gmail with <code>Ctrl+Shift+G</code>, grab clean production HTML with <code>Ctrl+S</code>, or download the full 22-template ZIP bundle.
                </div>`
            }}
        ];

        function startTutorial() {{
            currentTutorialStep = 0;
            renderTutorialStep(currentTutorialStep);
            document.getElementById('tutorial-modal').classList.add('show');
        }}

        function closeTutorial() {{
            document.getElementById('tutorial-modal').classList.remove('show');
        }}

        function renderTutorialStep(idx) {{
            const step = TUTORIAL_STEPS[idx];
            if (!step) return;
            document.getElementById('tut-title').innerHTML = step.title;
            document.getElementById('tut-content').innerHTML = `
                <div style="font-size:0.72rem; font-weight:700; text-transform:uppercase; letter-spacing:0.5px; color:#38bdf8; margin-bottom:8px;">${{step.badge}}</div>
                ${{step.body}}
            `;
            document.getElementById('tut-step-counter').textContent = `Step ${{idx + 1}} of ${{TUTORIAL_STEPS.length}}`;
            document.getElementById('tut-btn-prev').style.visibility = idx === 0 ? 'hidden' : 'visible';
            document.getElementById('tut-btn-next').textContent = idx === TUTORIAL_STEPS.length - 1 ? 'Get Started 🚀' : 'Next →';
        }}

        function nextTutorialStep() {{
            if (currentTutorialStep < TUTORIAL_STEPS.length - 1) {{
                currentTutorialStep++;
                renderTutorialStep(currentTutorialStep);
            }} else {{
                closeTutorial();
                showToast('Tour completed! Enjoy designing.');
            }}
        }}

        function prevTutorialStep() {{
            if (currentTutorialStep > 0) {{
                currentTutorialStep--;
                renderTutorialStep(currentTutorialStep);
            }}
        }}

        // ═══════════════════════════════════════════════════════════
        // KEYBOARD SHORTCUTS & AUTO-FIX MODALS
        // ═══════════════════════════════════════════════════════════
        function openShortcutsModal() {{
            document.getElementById('shortcuts-modal').classList.add('show');
        }}

        function closeShortcutsModal() {{
            document.getElementById('shortcuts-modal').classList.remove('show');
        }}

        function openAutoFixModal() {{
            const subj = (document.getElementById('inp-subject').value || '').trim();
            const preheader = (document.getElementById('inp-preheader').value || '').trim();
            const body = (document.getElementById('inp-body').value || '').trim();
            const btnText = (document.getElementById('inp-button-text').value || '').trim();

            const container = document.getElementById('autofix-modal-content');
            let items = [];

            if (!subj) {{
                items.push(`
                    <div style="padding:10px; background:rgba(239,68,68,0.1); border:1px solid rgba(239,68,68,0.3); border-radius:6px; margin-bottom:8px; display:flex; justify-content:space-between; align-items:center;">
                        <div>
                            <div style="font-size:0.78rem; font-weight:700; color:#f87171;">Missing Subject Line</div>
                            <div style="font-size:0.7rem; color:#cbd5e1;">Subject lines are required for inbox delivery.</div>
                        </div>
                        <button class="btn btn-outline" style="font-size:0.68rem; padding:3px 8px; color:#38bdf8;" onclick="applyAutoFix('subject')">Fix Now</button>
                    </div>
                `);
            }} else if (subj.length > 55) {{
                items.push(`
                    <div style="padding:10px; background:rgba(245,158,11,0.1); border:1px solid rgba(245,158,11,0.3); border-radius:6px; margin-bottom:8px; display:flex; justify-content:space-between; align-items:center;">
                        <div>
                            <div style="font-size:0.78rem; font-weight:700; color:#fbbf24;">Subject Line Too Long (${{subj.length}} chars)</div>
                            <div style="font-size:0.7rem; color:#cbd5e1;">Mobile inboxes truncate subjects over 50 characters.</div>
                        </div>
                        <button class="btn btn-outline" style="font-size:0.68rem; padding:3px 8px; color:#38bdf8;" onclick="applyAutoFix('trim-subject')">Trim to 50</button>
                    </div>
                `);
            }}

            if (!preheader) {{
                items.push(`
                    <div style="padding:10px; background:rgba(245,158,11,0.1); border:1px solid rgba(245,158,11,0.3); border-radius:6px; margin-bottom:8px; display:flex; justify-content:space-between; align-items:center;">
                        <div>
                            <div style="font-size:0.78rem; font-weight:700; color:#fbbf24;">Missing Preheader Text</div>
                            <div style="font-size:0.7rem; color:#cbd5e1;">Preheaders boost mobile open rates by 34%.</div>
                        </div>
                        <button class="btn btn-outline" style="font-size:0.68rem; padding:3px 8px; color:#38bdf8;" onclick="applyAutoFix('preheader')">Auto-Generate</button>
                    </div>
                `);
            }}

            if (!btnText) {{
                items.push(`
                    <div style="padding:10px; background:rgba(239,68,68,0.1); border:1px solid rgba(239,68,68,0.3); border-radius:6px; margin-bottom:8px; display:flex; justify-content:space-between; align-items:center;">
                        <div>
                            <div style="font-size:0.78rem; font-weight:700; color:#f87171;">Missing Button CTA Text</div>
                            <div style="font-size:0.7rem; color:#cbd5e1;">A clear primary action is needed.</div>
                        </div>
                        <button class="btn btn-outline" style="font-size:0.68rem; padding:3px 8px; color:#38bdf8;" onclick="applyAutoFix('button')">Set Default</button>
                    </div>
                `);
            }}

            const brokenRegex = /{{{{[^}}]*$/m;
            if (brokenRegex.test(body)) {{
                items.push(`
                    <div style="padding:10px; background:rgba(239,68,68,0.1); border:1px solid rgba(239,68,68,0.3); border-radius:6px; margin-bottom:8px; display:flex; justify-content:space-between; align-items:center;">
                        <div>
                            <div style="font-size:0.78rem; font-weight:700; color:#f87171;">Broken Variable Tag</div>
                            <div style="font-size:0.7rem; color:#cbd5e1;">Unclosed curly brace detected in body text.</div>
                        </div>
                        <button class="btn btn-outline" style="font-size:0.68rem; padding:3px 8px; color:#38bdf8;" onclick="applyAutoFix('tags')">Close Braces</button>
                    </div>
                `);
            }}

            if (items.length === 0) {{
                container.innerHTML = `
                    <div style="text-align:center; padding:24px 10px;">
                        <div style="font-size:2.2rem; margin-bottom:8px;">🎉</div>
                        <div style="font-size:0.92rem; font-weight:700; color:#34d399; margin-bottom:4px;">100% Delivery Readiness!</div>
                        <div style="font-size:0.76rem; color:#94a3b8;">Your template complies with all email client standards, mobile subject limits, and clean formatting rules.</div>
                    </div>
                `;
            }} else {{
                container.innerHTML = `
                    <div style="margin-bottom:12px; font-size:0.76rem; color:#cbd5e1;">
                        Fix the following ${{items.length}} recommendation${{items.length > 1 ? 's' : ''}} to maximize delivery rates:
                    </div>
                    ${{items.join('')}}
                `;
            }}

            document.getElementById('autofix-modal').classList.add('show');
        }}

        function closeAutoFixModal() {{
            document.getElementById('autofix-modal').classList.remove('show');
        }}

        function applyAutoFix(type) {{
            if (type === 'subject') {{
                document.getElementById('inp-subject').value = 'Important Admission Update - Simply Admission';
                onSubjectInput();
            }} else if (type === 'trim-subject') {{
                const s = document.getElementById('inp-subject').value;
                document.getElementById('inp-subject').value = s.substring(0, 48).trim() + '...';
                onSubjectInput();
            }} else if (type === 'preheader') {{
                const raw = (document.getElementById('inp-body').value || '').replace(/<[^>]+>/g, '').replace(/\\s+/g, ' ').trim();
                document.getElementById('inp-preheader').value = raw.substring(0, 75) + '...';
                rebuildPreview();
            }} else if (type === 'button') {{
                document.getElementById('inp-button-text').value = 'VIEW ADMISSION DETAILS';
                rebuildPreview();
            }} else if (type === 'tags') {{
                let b = document.getElementById('inp-body').value;
                b = b.replace(/{{([a-z0-9_]+)(?!}})/g, '{{$1}}');
                document.getElementById('inp-body').value = b;
                onBodyInput();
            }}
            showToast('Applied recommended fix!');
            openAutoFixModal();
        }}

        // ═══════════════════════════════════════════════════════════
        // ZEN MODE, LIVE EDIT & VISUAL STYLER CONTROLS
        // ═══════════════════════════════════════════════════════════
        function toggleZenMode() {{
            const isZen = document.body.classList.toggle('zen-mode');
            const btn = document.getElementById('btn-zen-mode');
            if (btn) btn.classList.toggle('active', isZen);
            showToast(isZen ? 'Fullscreen Zen Mode (Alt+Z / Esc to exit)' : 'Exited Zen Mode');
        }}

        function toggleInPreviewEdit() {{
            isLiveEditActive = !isLiveEditActive;
            const btn = document.getElementById('btn-inpreview-edit');
            if (btn) btn.classList.toggle('active', isLiveEditActive);
            if (isLiveEditActive) {{
                attachLiveEditListeners();
                showToast('Live Edit Active: Click text directly inside preview to edit!');
            }} else {{
                detachLiveEditListeners();
                showToast('Exited Live Edit mode');
            }}
        }}

        function attachLiveEditListeners() {{
            const frames = [document.getElementById('live-iframe')];
            if (currentViewport === 'dual') {{
                frames.push(document.getElementById('live-iframe-desktop'), document.getElementById('live-iframe-mobile'));
            }}
            frames.forEach(frame => {{
                if (!frame || !frame.contentDocument) return;
                const doc = frame.contentDocument;
                const editableElements = doc.querySelectorAll('h1, h2, p, a, td');
                editableElements.forEach(el => {{
                    el.contentEditable = 'true';
                    el.style.outline = '1px dashed rgba(56, 189, 248, 0.4)';
                    el.style.outlineOffset = '2px';
                    el.onblur = () => {{
                        if (el.tagName === 'P') {{
                            const paragraphs = Array.from(doc.querySelectorAll('td[align="left"] > p'));
                            if (paragraphs.length > 2) {{
                                const mainParas = paragraphs.slice(2, paragraphs.length - 1);
                                const newBody = mainParas.map(p => p.innerHTML.replace(/<br\\s*\\/?>/gi, '\\n')).join('\\n\\n');
                                if (newBody.trim()) {{
                                    document.getElementById('inp-body').value = newBody;
                                    onBodyInput();
                                }}
                            }}
                        }}
                    }};
                }});
            }});
        }}

        function detachLiveEditListeners() {{
            const frames = [document.getElementById('live-iframe'), document.getElementById('live-iframe-desktop'), document.getElementById('live-iframe-mobile')];
            frames.forEach(frame => {{
                if (!frame || !frame.contentDocument) return;
                const editableElements = frame.contentDocument.querySelectorAll('[contenteditable="true"]');
                editableElements.forEach(el => {{
                    el.contentEditable = 'false';
                    el.style.outline = 'none';
                }});
            }});
        }}

        function toggleDesignerAccordion() {{
            designerAccordionOpen = !designerAccordionOpen;
            const body = document.getElementById('designer-styler-body');
            const arrow = document.getElementById('designer-accordion-arrow');
            if (body) body.style.display = designerAccordionOpen ? 'block' : 'none';
            if (arrow) arrow.textContent = designerAccordionOpen ? '▲' : '▼';
        }}

        function setLogoAlign(align) {{
            currentLogoAlign = align;
            const btnCenter = document.getElementById('btn-logo-center');
            const btnLeft = document.getElementById('btn-logo-left');
            if (btnCenter) btnCenter.classList.toggle('active', align === 'center');
            if (btnLeft) btnLeft.classList.toggle('active', align === 'left');
            rebuildPreview();
        }}

        function setEditorMode(mode) {{
            currentEditorMode = mode;
            const btnForm = document.getElementById('btn-mode-form');
            const btnRaw = document.getElementById('btn-mode-raw');
            if (btnForm) btnForm.classList.toggle('active', mode === 'form');
            if (btnRaw) btnRaw.classList.toggle('active', mode === 'raw');

            if (mode === 'raw') {{
                openCodeModal();
            }}
        }}

        // ═══════════════════════════════════════════════════════════
        // UNDO / REDO HISTORY & AUTOSAVE
        // ═══════════════════════════════════════════════════════════
        function captureCurrentState() {{
            return {{
                subject: document.getElementById('inp-subject').value || '',
                preheader: document.getElementById('inp-preheader').value || '',
                headline: document.getElementById('inp-headline').value || '',
                greeting: document.getElementById('inp-greeting').value || '',
                body: document.getElementById('inp-body').value || '',
                buttonText: document.getElementById('inp-button-text').value || '',
                loginPrompt: document.getElementById('inp-login-prompt').value || '',
                includeNotice: document.getElementById('inp-include-notice') ? document.getElementById('inp-include-notice').checked : false,
                noticeText: document.getElementById('inp-notice-text') ? document.getElementById('inp-notice-text').value : '',
                includeRoadmap: document.getElementById('inp-include-roadmap') ? document.getElementById('inp-include-roadmap').checked : false,
                includeLogin: document.getElementById('inp-include-login') ? document.getElementById('inp-include-login').checked : true
            }};
        }}

        function pushUndoState() {{
            if (isUndoAction) return;
            const state = captureCurrentState();
            const last = undoHistory[undoHistory.length - 1];
            if (!last || JSON.stringify(last) !== JSON.stringify(state)) {{
                undoHistory.push(state);
                if (undoHistory.length > 30) undoHistory.shift();
                redoHistory = [];
            }}
        }}

        function undo() {{
            if (undoHistory.length > 1) {{
                isUndoAction = true;
                const current = undoHistory.pop();
                redoHistory.push(current);
                const prev = undoHistory[undoHistory.length - 1];
                applyState(prev);
                isUndoAction = false;
                showToast('Undone (Ctrl+Z)');
            }} else {{
                showToast('Nothing to undo');
            }}
        }}

        function redo() {{
            if (redoHistory.length > 0) {{
                isUndoAction = true;
                const next = redoHistory.pop();
                undoHistory.push(next);
                applyState(next);
                isUndoAction = false;
                showToast('Redone (Ctrl+Y)');
            }} else {{
                showToast('Nothing to redo');
            }}
        }}

        function applyState(s) {{
            if (!s) return;
            if (document.getElementById('inp-subject')) document.getElementById('inp-subject').value = s.subject;
            if (document.getElementById('inp-preheader')) document.getElementById('inp-preheader').value = s.preheader;
            if (document.getElementById('inp-headline')) document.getElementById('inp-headline').value = s.headline;
            if (document.getElementById('inp-greeting')) document.getElementById('inp-greeting').value = s.greeting;
            if (document.getElementById('inp-body')) document.getElementById('inp-body').value = s.body;
            if (document.getElementById('inp-button-text')) document.getElementById('inp-button-text').value = s.buttonText;
            if (document.getElementById('inp-login-prompt')) document.getElementById('inp-login-prompt').value = s.loginPrompt;
            if (document.getElementById('inp-include-notice')) document.getElementById('inp-include-notice').checked = s.includeNotice;
            if (document.getElementById('inp-notice-text')) document.getElementById('inp-notice-text').value = s.noticeText;
            if (document.getElementById('inp-include-roadmap')) document.getElementById('inp-include-roadmap').checked = s.includeRoadmap;
            if (document.getElementById('inp-include-login')) document.getElementById('inp-include-login').checked = s.includeLogin;

            onSubjectInput();
            onBodyInput();
        }}

        function saveToLocalStorage() {{
            try {{
                const state = captureCurrentState();
                localStorage.setItem('sa_designer_draft_state', JSON.stringify(state));
                setAutosaveStatus('Saved');
            }} catch (e) {{}}
        }}

        function setAutosaveStatus(txt) {{
            const el = document.getElementById('autosave-status');
            if (el) {{
                el.innerHTML = `<span class="autosave-dot"></span> ${{txt}}`;
            }}
        }}

        function resetTemplate() {{
            const select = document.getElementById('inp-template-selector');
            if (select && select.value !== 'custom') {{
                onTemplateSelect(select.value);
                showToast('Reset template to canonical baseline');
            }} else {{
                applyCampusPreset(currentActiveCampus);
                showToast('Reset to campus defaults');
            }}
        }}

        function showToast(msg) {{
            const toast = document.getElementById('toast');
            toast.textContent = msg;
            toast.classList.add('show');
            setTimeout(() => toast.classList.remove('show'), 2200);
        }}
    </script>
</body>
</html>"""

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)

    print("Successfully built index.html with Enterprise Enhancements!")
