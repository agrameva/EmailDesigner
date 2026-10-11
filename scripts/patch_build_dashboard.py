import re

file_path = "build_dashboard.py"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Remove "about_campus" lines from CLIENT_CAMPUSES
content = re.sub(r'\s*"about_campus":\s*"[^"]*",?\n', '\n', content)

# 2. Fix form hint
content = content.replace(
    'Used in greeting, subject line, header, and copyright',
    'Used in greeting, subject line, and header'
)

# 3. Remove the entire About Campus textarea form row
about_campus_form_row = """                            <div class="form-row">
                                <label class="form-label">About Campus (Tagline / Footer info)</label>
                                <textarea class="form-textarea" id="inp-about-campus" rows="2" placeholder="Brief campus tagline (Leave blank to hide)" oninput="rebuildPreview()">Simply Admission simplifies the entire admission process for parents and institutions.</textarea>
                                <span class="form-hint">If blank, this section will NOT be displayed in footer</span>
                            </div>"""

if about_campus_form_row in content:
    content = content.replace(about_campus_form_row, '')
else:
    # regex fallback
    content = re.sub(r'<div class="form-row">\s*<label class="form-label">About Campus[^<]*</label>[\s\S]*?</div>', '', content)

# 4. Remove JS lines accessing inp-about-campus
content = re.sub(r'^\s*document\.getElementById\(\'inp-about-campus\'\)\.value\s*=.*?;\n', '', content, flags=re.MULTILINE)
content = re.sub(r'^\s*c\.about_campus\s*=.*?;\n', '', content, flags=re.MULTILINE)
content = re.sub(r'^\s*let aboutCampus\s*=.*?;\n', '', content, flags=re.MULTILINE)
content = re.sub(r'^\s*aboutCampus\s*=.*?;\n', '', content, flags=re.MULTILINE)
content = re.sub(r'^\s*aboutCampus:\s*document\.getElementById\(\'inp-about-campus\'\).*?,\n', '', content, flags=re.MULTILINE)
content = re.sub(r'^\s*aboutCampus:\s*customParams\.aboutCampus.*?,\n', '', content, flags=re.MULTILINE)

# 5. Replace footer generation in generateEmailHTML
old_footer_block = """            // CONDITIONAL SOCIAL MEDIA ICONS (Only render if link has value)
            let socialIconsHTML = '';
            const socialCells = [];
            if (fb) socialCells.push(`<td><a href="${fb}" target="_blank" title="Facebook"><img src="https://img.icons8.com/color/48/facebook-new.png" width="26" height="26" border="0" style="display:block; width:26px; height:26px;"/></a></td>`);
            if (insta) socialCells.push(`<td><a href="${insta}" target="_blank" title="Instagram"><img src="https://img.icons8.com/color/48/instagram-new--v1.png" width="26" height="26" border="0" style="display:block; width:26px; height:26px;"/></a></td>`);
            if (twitter) socialCells.push(`<td><a href="${twitter}" target="_blank" title="Twitter"><img src="https://img.icons8.com/color/48/twitter--v1.png" width="26" height="26" border="0" style="display:block; width:26px; height:26px;"/></a></td>`);
            if (li) socialCells.push(`<td><a href="${li}" target="_blank" title="LinkedIn"><img src="https://img.icons8.com/color/48/linkedin.png" width="26" height="26" border="0" style="display:block; width:26px; height:26px;"/></a></td>`);
            if (yt) socialCells.push(`<td><a href="${yt}" target="_blank" title="YouTube"><img src="https://img.icons8.com/color/48/youtube-play.png" width="26" height="26" border="0" style="display:block; width:26px; height:26px;"/></a></td>`);

            if (socialCells.length > 0) {
                socialIconsHTML = `
                <table border="0" cellpadding="6" cellspacing="0" align="center" style="margin: 0 auto 12px;">
                  <tr>
                    ${socialCells.join('\\n                    ')}
                  </tr>
                </table>
                `;
            }

            // CONDITIONAL ADDRESS:
            let addressHTML = '';
            if (campusAddress) {
                addressHTML = `<p style="margin: 0 0 6px 0; font-family: ${brandFont}; font-size: 12px; color: #64748b;">${campusAddress}</p>`;
            }

            // CONDITIONAL ABOUT CAMPUS:
            let aboutCampusHTML = '';
            if (aboutCampus) {
                aboutCampusHTML = `<p style="margin: 0 0 10px 0; font-family: ${brandFont}; font-size: 11px; color: #94a3b8; font-style: italic;">${aboutCampus}</p>`;
            }"""

new_footer_block = """            // Footer: ONLY social media links, google map link, and website link (CDN icons)
            const footerIcons = [];
            if (fb) footerIcons.push(`<td align="center" style="padding: 0 8px;"><a href="${fb}" target="_blank" title="Facebook" style="display:inline-block; text-decoration:none;"><img src="https://img.icons8.com/color/48/facebook-new.png" alt="Facebook" width="28" height="28" border="0" style="display:block; width:28px; height:28px; border:0; outline:none; text-decoration:none;" /></a></td>`);
            if (insta) footerIcons.push(`<td align="center" style="padding: 0 8px;"><a href="${insta}" target="_blank" title="Instagram" style="display:inline-block; text-decoration:none;"><img src="https://img.icons8.com/color/48/instagram-new--v1.png" alt="Instagram" width="28" height="28" border="0" style="display:block; width:28px; height:28px; border:0; outline:none; text-decoration:none;" /></a></td>`);
            if (twitter) footerIcons.push(`<td align="center" style="padding: 0 8px;"><a href="${twitter}" target="_blank" title="Twitter" style="display:inline-block; text-decoration:none;"><img src="https://img.icons8.com/color/48/twitter--v1.png" alt="Twitter" width="28" height="28" border="0" style="display:block; width:28px; height:28px; border:0; outline:none; text-decoration:none;" /></a></td>`);
            if (li) footerIcons.push(`<td align="center" style="padding: 0 8px;"><a href="${li}" target="_blank" title="LinkedIn" style="display:inline-block; text-decoration:none;"><img src="https://img.icons8.com/color/48/linkedin.png" alt="LinkedIn" width="28" height="28" border="0" style="display:block; width:28px; height:28px; border:0; outline:none; text-decoration:none;" /></a></td>`);
            if (yt) footerIcons.push(`<td align="center" style="padding: 0 8px;"><a href="${yt}" target="_blank" title="YouTube" style="display:inline-block; text-decoration:none;"><img src="https://img.icons8.com/color/48/youtube-play.png" alt="YouTube" width="28" height="28" border="0" style="display:block; width:28px; height:28px; border:0; outline:none; text-decoration:none;" /></a></td>`);

            const mapLink = locationLink || 'https://maps.google.com';
            footerIcons.push(`<td align="center" style="padding: 0 8px;"><a href="${mapLink}" target="_blank" title="Google Map" style="display:inline-block; text-decoration:none;"><img src="https://img.icons8.com/color/48/google-maps-new.png" alt="Google Map" width="28" height="28" border="0" style="display:block; width:28px; height:28px; border:0; outline:none; text-decoration:none;" /></a></td>`);

            const webLink = websiteUrl || 'http://simplyadmission.com';
            footerIcons.push(`<td align="center" style="padding: 0 8px;"><a href="${webLink}" target="_blank" title="Website" style="display:inline-block; text-decoration:none;"><img src="https://img.icons8.com/color/48/domain--v1.png" alt="Website" width="28" height="28" border="0" style="display:block; width:28px; height:28px; border:0; outline:none; text-decoration:none;" /></a></td>`);

            const footerIconsHTML = `
            <table border="0" cellpadding="0" cellspacing="0" align="center" style="margin: 0 auto;">
              <tr>
                ${footerIcons.join('\\n                ')}
              </tr>
            </table>
            `;"""

if old_footer_block in content:
    content = content.replace(old_footer_block, new_footer_block)
else:
    print("WARNING: old_footer_block not matched exactly!")

# 6. Replace campus footer in HTML template
old_campus_footer_html = """        <!-- Campus Footer -->
        <tr>
          <td align="center" style="padding: 20px 24px 22px; background-color: #fafafa; font-family: ${brandFont}; text-align: center;">
            ${socialIconsHTML}
            ${addressHTML}
            ${aboutCampusHTML}
            <p style="margin: 0; font-family: ${brandFont}; font-size: 11px; color: #94a3b8;">
              &copy; ${new Date().getFullYear()} ${campusName}. All rights reserved.
            </p>
          </td>
        </tr>"""

new_campus_footer_html = """        <!-- Campus Footer (Only social media link, google map link, and website link) -->
        <tr>
          <td align="center" style="padding: 20px 20px 22px; background-color: #fafafa;">
            ${footerIconsHTML}
          </td>
        </tr>"""

if old_campus_footer_html in content:
    content = content.replace(old_campus_footer_html, new_campus_footer_html)
else:
    print("WARNING: old_campus_footer_html not matched exactly!")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Patching build_dashboard.py completed!")
