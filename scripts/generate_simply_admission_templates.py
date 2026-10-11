import os

LOGO_URL = "https://resources.edunexttechnologies.com/web-data/simplyadmission/img/Simpli_Admission-logo.png"
BRAND_COLOR = "#11a14a"

FB_URL = "https://www.facebook.com/simplyadmission"
INSTA_URL = "https://www.instagram.com/simply_admission/"
TWITTER_URL = "https://twitter.com/AdmissionSimply"
LI_URL = "https://www.linkedin.com/company/simplyadmission/?viewAsMember=true"
WEB_URL = "http://simplyadmission.com"
MAP_URL = "https://www.google.com/maps/search/Simply+Admission,+Noida+Sector+68"
FORM_URL = "{{candidate_login_url}}"
MEDICAL_FORM_URL = "{{medical_form_url}}"
JODO_URL = "{{payment_link}}"
BROCHURE_URL = "{{brochure_url}}"

# Social Media Icons (High availability, email-safe 48px PNG scaled to 28x28)
ICON_FB = "https://img.icons8.com/color/48/facebook-new.png"
ICON_INSTA = "https://img.icons8.com/color/48/instagram-new--v1.png"
ICON_TWITTER = "https://img.icons8.com/color/48/twitter--v1.png"
ICON_LI = "https://img.icons8.com/color/48/linkedin.png"
ICON_WEB = "https://img.icons8.com/color/48/domain--v1.png"
ICON_MAP = "https://img.icons8.com/color/48/google-maps-new.png"

def wrap_template(subject, body_html):
    return f"""<!--
================================================================================
EMAIL SUBJECT: {subject}
================================================================================
-->
<table width="100%" border="0" cellpadding="0" cellspacing="0" bgcolor="#f4f5f7" style="background-color: #f4f5f7; margin: 0; padding: 25px 0; font-family: Arial, Helvetica, sans-serif;">
  <tr>
    <td align="center" valign="top">
      <table width="600" border="0" cellpadding="0" cellspacing="0" bgcolor="#ffffff" style="width: 100%; max-width: 600px; background-color: #ffffff; border-radius: 6px; overflow: hidden; border: 1px solid #e2e8f0;">
        <!-- Top Accent Line -->
        <tr>
          <td height="4" bgcolor="{BRAND_COLOR}" style="height: 4px; background-color: {BRAND_COLOR}; font-size: 1px; line-height: 1px;">&nbsp;</td>
        </tr>
        <!-- Top Logo -->
        <tr>
          <td align="center" style="padding: 24px 20px 20px; background-color: #ffffff; border-bottom: 1px solid #eeeeee;">
            <a href="{WEB_URL}" target="_blank" style="text-decoration: none;">
              <img src="{LOGO_URL}" alt="Simply Admission" width="180" border="0" style="display: block; width: 180px; max-width: 100%; height: auto; margin: 0 auto; outline: none; border: none; text-decoration: none;" />
            </a>
          </td>
        </tr>
        <!-- Body Content Area -->
        <tr>
          <td align="left" style="padding: 30px 30px 24px; font-family: Arial, Helvetica, sans-serif; font-size: 14px; line-height: 1.65; color: #333333;">
{body_html}
          </td>
        </tr>
        <!-- Divider -->
        <tr>
          <td style="padding: 0 30px;">
            <table width="100%" border="0" cellpadding="0" cellspacing="0">
              <tr>
                <td height="1" bgcolor="#e8e8e8" style="height: 1px; background-color: #e8e8e8; font-size: 1px; line-height: 1px;">&nbsp;</td>
              </tr>
            </table>
          </td>
        </tr>
        <!-- Footer Social Links with Icons -->
        <tr>
          <td align="center" style="padding: 20px 20px 22px; background-color: #fafafa;">
            <table border="0" cellpadding="0" cellspacing="0" align="center" style="margin: 0 auto;">
              <tr>
                <td align="center" style="padding: 0 10px;">
                  <a href="{FB_URL}" target="_blank" title="Facebook" style="display: inline-block; text-decoration: none;">
                    <img src="{ICON_FB}" alt="Facebook" width="28" height="28" border="0" style="display: block; width: 28px; height: 28px; border: 0; outline: none; text-decoration: none;" />
                  </a>
                </td>
                <td align="center" style="padding: 0 10px;">
                  <a href="{INSTA_URL}" target="_blank" title="Instagram" style="display: inline-block; text-decoration: none;">
                    <img src="{ICON_INSTA}" alt="Instagram" width="28" height="28" border="0" style="display: block; width: 28px; height: 28px; border: 0; outline: none; text-decoration: none;" />
                  </a>
                </td>
                <td align="center" style="padding: 0 10px;">
                  <a href="{TWITTER_URL}" target="_blank" title="Twitter" style="display: inline-block; text-decoration: none;">
                    <img src="{ICON_TWITTER}" alt="Twitter" width="28" height="28" border="0" style="display: block; width: 28px; height: 28px; border: 0; outline: none; text-decoration: none;" />
                  </a>
                </td>
                <td align="center" style="padding: 0 10px;">
                  <a href="{LI_URL}" target="_blank" title="LinkedIn" style="display: inline-block; text-decoration: none;">
                    <img src="{ICON_LI}" alt="LinkedIn" width="28" height="28" border="0" style="display: block; width: 28px; height: 28px; border: 0; outline: none; text-decoration: none;" />
                  </a>
                </td>
                <td align="center" style="padding: 0 10px;">
                  <a href="{MAP_URL}" target="_blank" title="Google Map" style="display: inline-block; text-decoration: none;">
                    <img src="{ICON_MAP}" alt="Google Map" width="28" height="28" border="0" style="display: block; width: 28px; height: 28px; border: 0; outline: none; text-decoration: none;" />
                  </a>
                </td>
                <td align="center" style="padding: 0 10px;">
                  <a href="{WEB_URL}" target="_blank" title="Website" style="display: inline-block; text-decoration: none;">
                    <img src="{ICON_WEB}" alt="Website" width="28" height="28" border="0" style="display: block; width: 28px; height: 28px; border: 0; outline: none; text-decoration: none;" />
                  </a>
                </td>
              </tr>
            </table>
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>"""

# Template 1
t1_body = f"""              <p style="margin: 0 0 16px 0; font-family: Arial, Helvetica, sans-serif; font-size: 14px; line-height: 1.6; color: #333333;">Dear Parents,</p>
              <p style="margin: 0 0 16px 0; font-family: Arial, Helvetica, sans-serif; font-size: 14px; line-height: 1.6; color: #333333;">Greetings from Simply Admission!</p>
              <p style="margin: 0 0 16px 0; font-family: Arial, Helvetica, sans-serif; font-size: 14px; line-height: 1.6; color: #333333;">Thank you for your interest in {{{{student_class}}}} admission for {{{{student_name}}}}. Your enquiry number is <strong>{{{{enquiry_auto_id}}}}</strong>.</p>
              <p style="margin: 0 0 16px 0; font-family: Arial, Helvetica, sans-serif; font-size: 14px; line-height: 1.6; color: #333333;"><strong>Complete your Application Form:</strong> &nbsp;&#128279; <a href="{FORM_URL}" target="_blank" style="color: {BRAND_COLOR}; font-weight: bold; text-decoration: underline;">ADMISSION PORTAL LOGIN</a> &nbsp;&nbsp;&#128100; Username: {{{{username}}}} &nbsp;&nbsp;&#128273; Password: {{{{passwords}}}}</p>
              <p style="margin: 0 0 16px 0; font-family: Arial, Helvetica, sans-serif; font-size: 14px; line-height: 1.6; color: #333333;">Learn more about us: <a href="{INSTA_URL}" target="_blank" style="color: {BRAND_COLOR}; text-decoration: underline;">Instagram</a> | <a href="{WEB_URL}" target="_blank" style="color: {BRAND_COLOR}; text-decoration: underline;">Website</a> | <a href="{MAP_URL}" target="_blank" style="color: {BRAND_COLOR}; text-decoration: underline;">Location</a></p>
              <p style="margin: 0 0 20px 0; font-family: Arial, Helvetica, sans-serif; font-size: 14px; line-height: 1.6; color: #333333;">Our Admissions team will get in touch shortly.</p>
              <p style="margin: 0; font-family: Arial, Helvetica, sans-serif; font-size: 14px; line-height: 1.6; color: #333333;">Warm regards,<br /><strong>Team Admissions</strong><br />Simply Admission</p>"""

# Template 2
t2_body = f"""              <p style="margin: 0 0 16px 0; font-family: Arial, Helvetica, sans-serif; font-size: 14px; line-height: 1.6; color: #333333;">Dear Parents,</p>
              <p style="margin: 0 0 16px 0; font-family: Arial, Helvetica, sans-serif; font-size: 14px; line-height: 1.6; color: #333333;">Thank you for reaching out to Simply Admission. This confirms your admission application submission for {{{{student_name}}}} in {{{{student_class}}}}, application number {{{{enquiry_auto_id}}}}.</p>
              <p style="margin: 0 0 16px 0; font-family: Arial, Helvetica, sans-serif; font-size: 14px; line-height: 1.6; color: #333333;">To continue or review your application: &nbsp;&#128279; <a href="{FORM_URL}" target="_blank" style="color: {BRAND_COLOR}; font-weight: bold; text-decoration: underline;">CANDIDATE LOGIN</a> &nbsp;&nbsp;Username: {{{{username}}}} &nbsp;&nbsp;Password: {{{{passwords}}}}</p>
              <p style="margin: 0 0 20px 0; font-family: Arial, Helvetica, sans-serif; font-size: 14px; line-height: 1.6; color: #333333;">Our Admissions team will be in touch shortly to guide you on the next steps.</p>
              <p style="margin: 0; font-family: Arial, Helvetica, sans-serif; font-size: 14px; line-height: 1.6; color: #333333;">Warm regards,<br /><strong>Team Admissions</strong><br />Simply Admission | <a href="{WEB_URL}" target="_blank" style="color: {BRAND_COLOR}; text-decoration: underline;">simplyadmission.com</a></p>"""

# Template 3
t3_body = f"""              <p style="margin: 0 0 16px 0; font-family: Arial, Helvetica, sans-serif; font-size: 14px; line-height: 1.6; color: #333333;">Dear Parent,</p>
              <p style="margin: 0 0 16px 0; font-family: Arial, Helvetica, sans-serif; font-size: 14px; line-height: 1.6; color: #333333;">Thank you for taking the time to speak with us regarding {{{{student_name}}}}'s admission via Simply Admission.</p>
              <p style="margin: 0 0 16px 0; font-family: Arial, Helvetica, sans-serif; font-size: 14px; line-height: 1.6; color: #333333;">Next Step: Complete Your Registration. To proceed, kindly complete the online registration and necessary payments.</p>
              <p style="margin: 0 0 16px 0; font-family: Arial, Helvetica, sans-serif; font-size: 14px; line-height: 1.6; color: #333333;">Login to the Admission Portal using the credentials shared on your registered email ID: &nbsp;&#128279; <a href="{FORM_URL}" target="_blank" style="color: {BRAND_COLOR}; font-weight: bold; text-decoration: underline;">CANDIDATE LOGIN</a></p>
              <p style="margin: 0 0 20px 0; font-family: Arial, Helvetica, sans-serif; font-size: 14px; line-height: 1.6; color: #333333;">Our Admission Team will follow up shortly. We look forward to assisting you further.</p>
              <p style="margin: 0; font-family: Arial, Helvetica, sans-serif; font-size: 14px; line-height: 1.6; color: #333333;">Warm regards,<br /><strong>Team Admissions</strong><br />Simply Admission</p>"""

# Template 4
t4_body = f"""              <p style="margin: 0 0 16px 0; font-family: Arial, Helvetica, sans-serif; font-size: 14px; line-height: 1.6; color: #333333;">Dear Parent,</p>
              <p style="margin: 0 0 16px 0; font-family: Arial, Helvetica, sans-serif; font-size: 14px; line-height: 1.6; color: #333333;">Greetings from Simply Admission.</p>
              <p style="margin: 0 0 16px 0; font-family: Arial, Helvetica, sans-serif; font-size: 14px; line-height: 1.6; color: #333333;">This is to confirm receipt of INR {{{{current_fee_receipt_amount}}}} towards the Registration Fee, against Application No: {{{{application_no}}}}.</p>
              <p style="margin: 0 0 16px 0; font-family: Arial, Helvetica, sans-serif; font-size: 14px; line-height: 1.6; color: #333333;">To upload any remaining documents or track your application, please log in here: &nbsp;&#128279; <a href="{FORM_URL}" target="_blank" style="color: {BRAND_COLOR}; font-weight: bold; text-decoration: underline;">CANDIDATE LOGIN</a></p>
              <p style="margin: 0 0 16px 0; font-family: Arial, Helvetica, sans-serif; font-size: 14px; line-height: 1.6; color: #333333;">Your application will now be reviewed by our Admissions Team, who will contact you shortly regarding the next steps.</p>
              <p style="margin: 0; font-family: Arial, Helvetica, sans-serif; font-size: 14px; line-height: 1.6; color: #333333;">Regards,<br /><strong>Team Admissions</strong><br />Simply Admission</p>"""

# Template 5
t5_body = f"""              <p style="margin: 0 0 16px 0; font-family: Arial, Helvetica, sans-serif; font-size: 14px; line-height: 1.6; color: #333333;">Dear Parent,</p>
              <p style="margin: 0 0 16px 0; font-family: Arial, Helvetica, sans-serif; font-size: 14px; line-height: 1.6; color: #333333;">Greetings from Simply Admission.</p>
              <p style="margin: 0 0 16px 0; font-family: Arial, Helvetica, sans-serif; font-size: 14px; line-height: 1.6; color: #333333;">This is a reminder that {{{{student_name}}}}'s registration for {{{{student_class}}}} remains incomplete. We strongly recommend completing your registration and any pending fee payments without delay to avoid missing out on enrollment opportunities.</p>
              <p style="margin: 0 0 16px 0; font-family: Arial, Helvetica, sans-serif; font-size: 14px; line-height: 1.6; color: #333333;">Complete Registration Now: &nbsp;&#128279; <a href="{FORM_URL}" target="_blank" style="color: {BRAND_COLOR}; font-weight: bold; text-decoration: underline;">CANDIDATE LOGIN</a> &nbsp;(Use the User ID & Password sent to your registered email ID)</p>
              <p style="margin: 0 0 20px 0; font-family: Arial, Helvetica, sans-serif; font-size: 14px; line-height: 1.6; color: #333333;">We look forward to assisting you in finalizing your application.</p>
              <p style="margin: 0; font-family: Arial, Helvetica, sans-serif; font-size: 14px; line-height: 1.6; color: #333333;">Warm regards,<br /><strong>Team Admissions</strong><br />Simply Admission.</p>"""

# Template 6
t6_body = f"""              <p style="margin: 0 0 16px 0; font-family: Arial, Helvetica, sans-serif; font-size: 14px; line-height: 1.6; color: #333333;">Dear Parent,</p>
              <p style="margin: 0 0 16px 0; font-family: Arial, Helvetica, sans-serif; font-size: 14px; line-height: 1.6; color: #333333;">Warm greetings from Simply Admission!</p>
              <p style="margin: 0 0 16px 0; font-family: Arial, Helvetica, sans-serif; font-size: 14px; line-height: 1.6; color: #333333;">We tried connecting with you a little while ago regarding {{{{student_name}}}}'s admission enquiry for {{{{student_class}}}}, but seem to have missed you.</p>
              <p style="margin: 0 0 16px 0; font-family: Arial, Helvetica, sans-serif; font-size: 14px; line-height: 1.6; color: #333333;">To continue your application or access the portal, click here: &nbsp;&#128279; <a href="{FORM_URL}" target="_blank" style="color: {BRAND_COLOR}; font-weight: bold; text-decoration: underline;">CANDIDATE LOGIN</a></p>
              <p style="margin: 0 0 20px 0; font-family: Arial, Helvetica, sans-serif; font-size: 14px; line-height: 1.6; color: #333333;">Simply reply to this email with a suitable time to connect, and we'd be delighted to help you take the next step.</p>
              <p style="margin: 0; font-family: Arial, Helvetica, sans-serif; font-size: 14px; line-height: 1.6; color: #333333;">Warm regards,<br /><strong>Team Admissions</strong><br />Simply Admission</p>"""

# Template 7
t7_body = f"""              <p style="margin: 0 0 16px 0; font-family: Arial, Helvetica, sans-serif; font-size: 14px; line-height: 1.6; color: #333333;">Dear Parents,</p>
              <p style="margin: 0 0 16px 0; font-family: Arial, Helvetica, sans-serif; font-size: 14px; line-height: 1.6; color: #333333;">We are delighted to inform you that {{{{student_name}}}}'s registration for {{{{student_class}}}} admission has been granted!</p>
              <p style="margin: 0 0 16px 0; font-family: Arial, Helvetica, sans-serif; font-size: 14px; line-height: 1.6; color: #333333;"><strong>Congratulations on this exciting milestone!</strong></p>
              <p style="margin: 0 0 16px 0; font-family: Arial, Helvetica, sans-serif; font-size: 14px; line-height: 1.6; color: #333333;">To confirm the admission and pay the required admission fees, or to upload pending documents, please log in to the portal:</p>
              <p style="margin: 0 0 16px 0; font-family: Arial, Helvetica, sans-serif; font-size: 14px; line-height: 1.6; color: #333333;">&#128279; <a href="{FORM_URL}" target="_blank" style="color: {BRAND_COLOR}; font-weight: bold; text-decoration: underline;">CANDIDATE LOGIN</a></p>
              <p style="margin: 0 0 12px 0; font-family: Arial, Helvetica, sans-serif; font-size: 14px; line-height: 1.6; color: #333333;">Please ensure any remaining mandatory documents are submitted through the portal to avoid your admission being placed on hold.</p>
              <p style="margin: 0 0 20px 0; font-family: Arial, Helvetica, sans-serif; font-size: 14px; line-height: 1.6; color: #333333;">We encourage you to take the next steps promptly.</p>
              <p style="margin: 0; font-family: Arial, Helvetica, sans-serif; font-size: 14px; line-height: 1.6; color: #333333;">Warm regards,<br /><strong>Team Admissions</strong><br />Simply Admission</p>"""

templates = [
    ("01_enquiry_acknowledgement", "Your Admission Enquiry – Simply Admission", t1_body),
    ("02_application_submission", "Application Submission – Simply Admission", t2_body),
    ("03_call_connected", "Thank You for Speaking With Us – Next Steps for Admission", t3_body),
    ("04_registration_fee_paid", "Registration Fee Confirmation – Simply Admission", t4_body),
    ("05_registration_pending", "Registration Pending – Simply Admission", t5_body),
    ("06_dnp_did_not_pick", "Admission Enquiry Follow-up – Simply Admission", t6_body),
    ("07_admission_granted", "Admission Granted – Simply Admission", t7_body),
]

out_dir = os.path.join("clients", "Simply Admission", "templates")
os.makedirs(out_dir, exist_ok=True)

for slug, subject, body in templates:
    full_html = wrap_template(subject, body)
    htm_path = os.path.join(out_dir, f"{slug}.htm")
    html_path = os.path.join(out_dir, f"{slug}.html")
    with open(htm_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"Generated {htm_path} and {html_path}")

# Also generate a handy markdown reference file
subjects_md_path = os.path.join(out_dir, "SUBJECTS.md")
with open(subjects_md_path, "w", encoding="utf-8") as f:
    f.write("# Simply Admission - Email Template Subjects Reference\n\n")
    f.write("| # | Template Name | File Name | Subject Line |\n")
    f.write("|---|---|---|---|\n")
    for i, (slug, subject, _) in enumerate(templates, 1):
        f.write(f"| {i} | {slug.replace('_', ' ').title()} | `{slug}.htm` | **{subject}** |\n")

print("All 7 templates and SUBJECTS.md generated successfully for Simply Admission!")
