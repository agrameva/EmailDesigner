# 📧 Email Template Designer Tool

A production-ready, lightweight, and fully responsive designer studio to compose, preview, and export high-conversion HTML email templates for school admission workflows.

> **Engineered for [Simply Admission](https://simplyadmission.com)** • Zero-dependency self-hosted dashboard.
> **🌐 Ready for GitHub Pages Hosting** • See [DEPLOYMENT.md](DEPLOYMENT.md) for 1-click team deployment instructions.

---

## 🌟 Key Highlights & Production Architecture

- **🎨 Minimalist, High-End Dark UI/UX**: Built with fluid glassmorphism, crisp contrast (`#080c14` canvas / `#0f172a` panels), and responsive typography powered by *Plus Jakarta Sans* and *JetBrains Mono*.
- **📱 Fully Responsive Engine**: Flawless experience across Large Desktops, Laptops, Tablets, and Mobile phones. Includes a smart segmented switcher (`✏️ Editor` / `👁️ Preview`) on screens under `768px`.
- **🛡️ 100% Email-Client Proof HTML**: Generates bulletproof nested table layouts compatible with Microsoft Outlook (desktop & web), Gmail, Apple Mail, Yahoo, and iOS/Android native mail clients.
- **🚫 Zero-Emoticons Email Safety**: Automatically strips emoticons to prevent `?` rendering errors on legacy corporate mail servers while replacing them with pure CSS credential cards.
- **🔗 Clean Icon-Only Footer**:
  - Exclusively renders **Social Media**, **Google Maps**, and **Website** link icons using high-availability CDN assets (`https://img.icons8.com/color/48/...`).
  - **Zero "About Campus"** and **Zero Copyright / Disclaimers** in the footer for a modern, clutter-free look.
- **🏷️ Complete 68 CRM Variables System**: Fully integrated with [`variables.json`](variables.json), supporting 1-click insertion chips, category filters, and real-time search.
- **📋 22 Canonical Admission Alert Scenarios**: Pre-configured word-to-word templates for every stage of the admissions funnel from [`default_template_list.json`](default_template_list.json).
- **👁️ Responsive Multi-Device & Dual-View Engine**:
  - **🖥️+📱 Side-by-Side Dual View**: Simultaneous live desktop (640px) and mobile phone (375px) rendering side-by-side.
  - **📱 Multi-Device Modes**: Toggle between Desktop (640px), Tablet (480px), and Mobile Chassis (375px) with realistic speaker notch and drop-shadow styling.
  - **✏️ In-Preview Live Edit (`✏️ Live Edit`)**: Click directly on headings, paragraphs, and buttons inside the iframe preview to edit copy WYSIWYG style with instant sync back to the editor.
- **🎨 Visual Design & Layout Styler**:
  - **Typography Selector**: Choose between *Arial / Clean*, *Helvetica Modern*, *Georgia Classic*, *Tahoma Formal*, *Trebuchet MS*, or *Verdana Wide*.
  - **Button Corner Curvature**: Toggle between *Rounded (6px)*, *Full Pill (24px)*, or *Sharp Square (0px)*.
  - **Button Width**: Switch between *Auto Centered* and *Full Width Mobile CTA (100%)*.
  - **Header Banner Style**: Pick from *Minimal Clean Logo*, *Top Accent Bar*, or *Branded Header Box*.
  - **Logo Sizing & Alignment**: Real-time slider (32px – 80px) and alignment toggle (Center vs Left).
- **🧭 Modern Navigation Bar & Mobile Drawer**:
  - **Top Navigation Bar**: Streamlined header with branding, view switcher, campus selectors with horizontal scrollers, and quick action utility buttons.
  - **Responsive Hamburger Menu (`☰`) & Slide-Out Drawer**: Clean mobile drawer (`#mobile-nav-drawer`) with overlay backdrop providing 1-tap access to all 5 application views (Studio, Template Library, Campus Brand Kit, AI Campaign Generator, Hub Overview) and power utilities.
- **↔️ Horizontal & Vertical Scrollers with Scroll Chevrons**:
  - **Sleek Custom Scrollbars**: 6px dark scrollbar styling across all panels and code preview boxes.
  - **Interactive Chevron Buttons (`◀` / `▶`)**: 1-click smooth horizontal scroll controls for Campus Pills, Scenario Category Filters, Brand Theme Presets, Paginator Strip, and Quick CRM Variable Chips.
- **🔢 Interactive Paginators**:
  - **Studio Scenario Paginator**: Comprehensive paginator displaying current scenario page (e.g. `Page 1 of 22: Mobile No Verification OTP`), `⏮ First`, `◀ Prev`, `Next ▶`, `⏭ Last` steppers, plus clickable numbered pills (`1` to `22`) with real-time active highlighting.
  - **Template Library (Archive) Paginator**: Clean pagination controls in View 2 (`Page X of Y`), allowing seamless browsing across all client templates.
- **⤢ Expand & ⤡ Collapse Accordion Architecture**:
  - **1-Click Master Controls**: `⤢ Expand All` and `⤡ Collapse All` buttons to open or close all editor sections simultaneously.
  - **7 Self-Explanatory Section Cards**: Structured collapsible cards with badges and helper tooltips:
    1. *📋 1. Workflow Scenario & Paginator* (22 Alerts badge)
    2. *🎨 2. Quick Brand Theme Presets* (6 Palettes badge)
    3. *✨ 3. Visual Styler & Typography* (Layout & Styling badge)
    4. *✉️ 4. Subject Line & Inbox Snippet* (Inbox Preview badge)
    5. *📝 5. Message Body & CRM Variables* (68 Variables badge)
    6. *🧩 6. Modular Content Blocks* (Interactive Components badge)
    7. *✍️ 7. Sign-off & Team Closing* (Sign-off badge)
- **🎓 Interactive Guided Onboarding Tour & Rich Tooltips**:
  - **5-Step Onboarding Walkthrough**: Step-by-step interactive tutorial (`🎓 Tour`) covering architecture, brand themes, 22 alert scenarios, 68 CRM tags, and 1-click production export.
  - **Rich Floating Tooltip Engine**: Glassmorphic dark tooltips with micro-animations on all key controls and interactive help icons (`?`).
- **🛡️ 1-Click Delivery Readiness Audit & Auto-Fix**:
  - Live compliance meter with 1-click auto-fix modal (`openAutoFixModal()`) to automatically trim long subjects to 50 characters, auto-generate preheaders from body copy, set fallback CTA buttons, and fix broken variable braces.
- **⚡ Undo & Redo History & Autosave**:
  - Full revision timeline with dedicated buttons (`↶ Undo`, `↷ Redo`) and keyboard shortcuts (`Ctrl+Z`, `Ctrl+Y`).
  - Real-time autosave with `● Saved` badge and LocalStorage draft persistence.
- **⛶ Zen Fullscreen Focus Canvas**:
  - Toggle full-canvas mode (`Alt+Z`) to eliminate sidebars and focus purely on layout and design.
- **⚡ High-Productivity Ease-of-Use Features**:
  - 📋 **Paste into Gmail / Outlook (`Ctrl+V`)**: Copies formatted rich-text HTML directly to clipboard. You can paste directly into Gmail or Outlook Web compose window with images, styled buttons, and badges fully intact without writing or inspecting HTML.
  - 🎨 **12 Synchronized Brand Themes**: Instant harmonized palette presets (*Simply Blue*, *Emerald Luxe*, *Classic Crimson*, *Royal Indigo*, *Sunset Amber*, *Slate Noir*, *Nordic Teal*, *Midnight Obsidian*, *Amethyst Purple*, *Coral Blossom*, *Cyber Bronze*, *Titanium Tech*). Seamlessly synchronizes header, button accents, font colors, outer background canvas, card background, highlight pills, and credential boxes in 1 click with real-time WCAG AAA contrast auditing.
  - 🧩 **1-Click Component Inserters**: Visual toolbar buttons to instantly insert pre-built, table-safe components (`+ 💳 Fee Breakdown Table`, `+ 📅 Tour/Meeting Schedule`, `+ 📋 Document Checklist`, `+ 📞 Admissions Helpdesk Bar`).
  - ◀️ **Stepper Navigation & Category Filters**: Quickly cycle through all 22 alert scenarios with `◀ Prev` / `Next ▶` buttons or filter by category (`🔑 Auth`, `📝 Enquiry`, `📅 Visits`, `💳 Fees`, `🎓 Apps`). Keyboard shortcuts `[` and `]` cycle alerts instantly.
  - 🧪 **Interactive Test Data Customizer**: Live drawer allowing admissions teams to test real-world edge cases (custom student names, classes, fee amounts, OTP codes) that update the preview in real-time.
  - 🖨️ **1-Click Print / PDF Proof**: Directly print or export a clean letter-size email proof for stakeholder and management approvals.
- **🌙 Parent Dark Mode Simulator**: One-click preview toggle (`🌙 Dark Sim`) to simulate dark mode inverted email client rendering (Outlook / Apple Mail).
- **📬 Preheader Snippet & Inbox Preview**: Configurable hidden preheader text with zero-width character padding to control what parents see before opening the email.
- **📏 Subject Line Cutoff Counter**: Real-time character counter alerting when subject lines exceed mobile email client limits (50-60 characters).
- **💬 Omnichannel Companion (WhatsApp/SMS)**: Auto-derives plain-text companion messages from email content with 1-click clipboard copy for multi-channel admission workflows.
- **📦 Bulk Package Exports**:
  - 🗜️ **Export All 22 as ZIP**: Instant packaging and downloading of all active templates via in-browser JSZip.
  - 📊 **Export CRM CSV**: Formatted manifest export ready for bulk upload to LeadSquared, NoPaperForms, Salesforce, or HubSpot.
- **⚡ Keyboard Command Palette**: Instant modal navigator accessible via `Ctrl+K` or `⌘K` for lightning-fast keyboard-first template navigation.
- **⚡ Instant 1-Click Exports**:
  - 📋 **Copy Subject**: One-click subject line copy.
  - 📋 **Copy Clean HTML**: Ready to paste directly into any CRM, ESP, or campaign tool.
  - 💾 **Download `.html`**: Standalone HTML file export.
  - `</>` **View Code Modal**: Syntax-styled inspect window with line counter.

---

## 📂 Project Structure

```
Email Template Designer Tool/
├── variables.json                       ← 🏷️ Master 68 CRM Variables definition
├── default_template_list.json           ← 📋 22 Default CRM Alert Scenarios (JSON)
├── default_template_list.txt            ← 📋 22 Default CRM Alert Scenarios (Text)
│
├── samples/                             ← 📦 Production Sample Templates (Git tracked)
│   └── Canonical Suite/
│       └── templates/                   ← 22 Canonical word-to-word .html templates
│           ├── 01_mobile_no_verification_otp.html
│           ├── 02_email_id_verification_otp.html
│           ├── ...
│           └── 22_candidate_login.html
│
├── clients/                             ← 🔒 Production Client Templates (Git ignored)
│   ├── Simply Admission/
│   │   └── templates/                   ← Simply Admission templates
│   └── ...
│
├── scripts/                             ← Automation & Generator Scripts
│   ├── generate_dashboard_html.py       ← Responsive dashboard UI compiler
│   ├── generate_sample_templates.py     ← Builds the 22 sample .html templates
│   ├── generate_simply_admission_templates.py
│   └── generate_templates.py
│
├── build_dashboard.py                   ← Compiles index.html from samples & clients
├── run_server.bat                       ← One-click local HTTP server launcher
├── index.html                           ← Compiled standalone dashboard app
└── README.md                            ← Documentation
```

---

## 🚀 Quick Start

### 1. Launch Local Dashboard
Double-click **`run_server.bat`** in the project root.
- Starts a local HTTP server on port `8000`.
- Automatically opens your default web browser at: [http://localhost:8000](http://localhost:8000)

### 2. Rebuilding Dashboard
Whenever you add new client templates or modify sample files:
```bash
python build_dashboard.py
```
*Generates an updated `index.html` in milliseconds with all clients and sample templates automatically indexed.*

---

## 📋 The 22 Canonical Admission Alerts

Every scenario includes concise word-to-word copy, appropriate subject lines, active variables, and action buttons:

| # | Alert Scenario Name | Category | Primary Action / Button |
|---|---|---|---|
| **01** | `Mobile No. Verification OTP` | Authentication & Security | Verify on Portal |
| **02** | `Email ID Verification OTP` | Authentication & Security | Confirm Email |
| **03** | `Candidate Login With OTP` | Authentication & Security | Candidate Login |
| **04** | `Password Reset Communication to Student` | Authentication & Security | Candidate Login |
| **05** | `Forget Password OTP For School` | Authentication & Security | Reset Password |
| **06** | `Forget Password OTP For Student` | Authentication & Security | Set New Password |
| **07** | `Enquiry Acknowledgment` | Enquiry & Counseling | Admission Portal Login |
| **08** | `Enquiry Notification to Employee` | Enquiry & Counseling | Open CRM Dashboard |
| **09** | `Enquiry Notification to Counsellor` | Enquiry & Counseling | View Lead in CRM |
| **10** | `In case of duplicate Enquiry Communication to User` | Enquiry & Counseling | Check Application Status |
| **11** | `School Tour Scheduled` | Campus Tours | View Tour Details / Pass |
| **12** | `School Tour Reminder to Candidate` | Campus Tours | View Appointment |
| **13** | `School Tour Completed Thank You` | Campus Tours | Complete Application |
| **14** | `Reschedule School Tour` | Campus Tours | Candidate Portal |
| **15** | `One-to-One Meeting (Offline/In-person) Scheduled` | Interactions & Meetings | Candidate Portal |
| **16** | `One-to-One Meeting (Online/In-person) Scheduled` | Interactions & Meetings | Join Online Meeting |
| **17** | `Meeting Reminder to Candidate` | Interactions & Meetings | View Details |
| **18** | `Meeting Completed to Candidate` | Interactions & Meetings | Track Application |
| **19** | `Reschedule Meeting alert to Candidate` | Interactions & Meetings | Candidate Portal |
| **20** | `Adhoc Payment Alert to Candidate` | Fee & Payments | Pay Fee Online |
| **21** | `Fee Receipt Download URL Alert to Candidate` | Fee & Payments | Download Fee Receipt (PDF) |
| **22** | `Candidate Login` | Candidate Portal | Admission Portal Login |

---

## 🏷️ The 68 CRM Variables Catalog

All 68 variables defined in [`variables.json`](variables.json) are categorized below with their sample preview substitutions:

### 1. Student & Academic
| Variable Merge Tag | Description Label | Realistic Sample Preview |
|---|---|---|
| `{{student_name}}` | Student Name | Aarav Sharma |
| `{{student_class}}` | Class / Grade | Grade 1 |
| `{{academic_year}}` | Academic Year | 2026-2027 |
| `{{curriculum}}` | Curriculum | CBSE |
| `{{stream_name}}` | Stream Name | Science & Technology |
| `{{admissionNo}}` | Admission No. | ADM-2026-0512 |

### 2. Credentials & Portal Access
| Variable Merge Tag | Description Label | Realistic Sample Preview |
|---|---|---|
| `{{username}}` | UserName | aarav.sharma26 |
| `{{passwords}}` | Password | Pass@2026# |
| `{{otp}}` | OTP | 489201 |
| `{{output_form_url}}` | Output Form Url | https://simplyadmission.com/form/download/APP-2026-1042 |

### 3. Parents & Family
| Variable Merge Tag | Description Label | Realistic Sample Preview |
|---|---|---|
| `{{father_name}}` | Father Name | Rajesh Sharma |
| `{{father_mobile_no}}` | Father Mobile No | +91 98765 43210 |
| `{{father_email}}` | Father Email | rajesh.sharma@example.com |
| `{{mother_name}}` | Mother Name | Pooja Sharma |
| `{{mother_mobile_no}}` | Mother Mobile No | +91 98765 43211 |
| `{{mother_email}}` | Mother Email | pooja.sharma@example.com |
| `{{guardian_name}}` | Guardian Name | Vikram Sharma |
| `{{guardian_mobile_no}}` | Guardian Mobile No. | +91 98111 22334 |
| `{{guardian_email_id}}` | Guardian Email ID | vikram.sharma@example.com |
| `{{is_single_parent}}` | Is Single Parent | No |
| `{{parent_type}}` | Parent Type | Both Parents |

### 4. Enquiry & Application Pipeline
| Variable Merge Tag | Description Label | Realistic Sample Preview |
|---|---|---|
| `{{enquiry_auto_id}}` | Enquiry Auto ID | ENQ-2026-8849 |
| `{{application_no}}` | Application No | APP-2026-1042 |
| `{{enquiry_date}}` | Enquiry Date | 08-Oct-2026 |
| `{{enquiry_stage_name}}` | Enquiry Stage | Campus Visit Scheduled |
| `{{enquiry_sub_stage_name}}` | Enquiry Sub Stage | Slot Confirmed |
| `{{application_stage_name}}` | Application Stage | Document Verification |
| `{{application_sub_stage_name}}` | Application Sub Stage | Pending Records |
| `{{counsler_name}}` | Counsler Name | Ms. Ananya Sen |
| `{{employee_name}}` | Employee Name | Mr. Rohit Verma |
| `{{next_follow_up_date}}` | Next Follow-Up Date | 20-Oct-2026 |
| `{{last_remarks}}` | Last Remarks | Parents confirmed walkthrough attendance |
| `{{last_followup_date}}` | Last Followup Date | 10-Oct-2026 |
| `{{last_followup_time}}` | Last Followup Time | 04:15 PM |

### 5. Fees, Receipts & Payments
| Variable Merge Tag | Description Label | Realistic Sample Preview |
|---|---|---|
| `{{current_fee_receipt_head}}` | Fee Name | Registration & Assessment Fee |
| `{{current_fee_receipt_amount}}` | Fee Amount | 2,500 |
| `{{current_fee_receipt_paid_amount}}` | Paid Fee Amount | 2,500 |
| `{{current_fee_receipt_head_amount}}` | Paid Fee Amount with head | Registration Fee: 2,500 |
| `{{payment_link}}` | Payment Link | https://portal.simplyadmission.com/pay/online-fee/APP-2026-1042 |
| `{{payment_link_whats_app}}` | Payment Link Whatsapp | https://wa.me/919876543210?text=PayFee |
| `{{payment_link_barcode}}` | Payment Link Barcode | https://resources.edunexttechnologies.com/web-data/sample-qr.png |
| `{{admission_fee_payment_fee_receipt_url}}` | Admission Fee Receipt URL | https://portal.simplyadmission.com/receipt/adm-fee-2026.pdf |
| `{{registration_fee_payment_fee_receipt_url}}` | Registration Fee Receipt URL | https://portal.simplyadmission.com/receipt/reg-fee-2026.pdf |
| `{{bankName}}` | Bank Name | HDFC Bank Ltd |
| `{{branchName}}` | Branch Name | Noida Sector 62 |
| `{{issueDate}}` | Issue Date | 11-Oct-2026 |

### 6. Tours, Meetings & Schedules
| Variable Merge Tag | Description Label | Realistic Sample Preview |
|---|---|---|
| `{{school_tour_date}}` | School Tour Date | 18-Oct-2026 |
| `{{school_tour_from_time}}` | School Tour From Time | 10:00 AM |
| `{{school_tour_to_time}}` | School Tour Tour Time | 11:30 AM |
| `{{meeting_date}}` | Meeting Date | 16-Oct-2026 |
| `{{meeting_time}}` | Meeting Time | 11:00 AM |
| `{{meeting_url}}` | Meeting Url | https://meet.google.com/adm-2026-xyz |
| `{{date}}` | Date | 15-Oct-2026 |
| `{{time}}` | Time | 10:30 AM |

### 7. School & Contact Info
| Variable Merge Tag | Description Label | Realistic Sample Preview |
|---|---|---|
| `{{school_name}}` | School Name | Simply Admission |
| `{{school_address}}` | School Address | Noida Sector 68, UP, India |
| `{{school_email_id}}` | School Email Id | admissions@simplyadmission.com |
| `{{school_mobile_no}}` | School Mobile No. | +91 99999 88888 |
| `{{school_url}}` | School Url | https://simplyadmission.com |
| `{{email}}` | Email Id | parents.sharma@example.com |
| `{{mobile_no}}` | Mobile No | +91 98765 43210 |

### 8. Marketing & Attribution
| Variable Merge Tag | Description Label | Realistic Sample Preview |
|---|---|---|
| `{{lead_source}}` | Lead Source | Website Enquiry |
| `{{lead_medium}}` | Medium | Organic Search |
| `{{lead_campaign}}` | Campaign | Admissions 2026-27 |
| `{{source_of_info}}` | Source of Info | School Recommendation |
| `{{activity_name}}` | Activity | Interaction Booking |
| `{{sub_activity_name}}` | Sub-Activity | Email Notification Sent |
| `{{sub_activity_reason_name}}` | Sub-Activity Reason | Slot Booking Acknowledgement |

---

## 🛠️ Adding a New School Client

1. Create the client directory:
   ```bash
   clients/<School Name>/templates/
   ```
2. Place `.html` email templates inside that folder.
3. Include the standard subject line comment block at the top of each template:
   ```html
   <!--
   ================================================================================
   EMAIL SUBJECT: Your Subject Line Here
   ================================================================================
   -->
   ```
4. Run the build script:
   ```bash
   python build_dashboard.py
   ```
The new client will instantly appear under the **Template Library** tab and in the active school selector!

---

## 📄 License & Confidentiality

Internal admission management tool built for **Simply Admission** and partner institutions.
