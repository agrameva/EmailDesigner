import os
import json
import re

# ═══════════════════════════════════════════════════════════════════════════════
# SCAN DIRECTORIES FOR TEMPLATES
# ═══════════════════════════════════════════════════════════════════════════════
SCAN_DIRS = [
    ("samples", "📦 Canonical Templates"),
    ("clients", "📁 Production Templates"),
]

clients = {}

def scan_folder(base_dir, source_label):
    """Scan a base directory for client folders containing a templates/ subfolder."""
    if not os.path.isdir(base_dir):
        return
    for item in sorted(os.listdir(base_dir)):
        client_dir = os.path.join(base_dir, item)
        if not os.path.isdir(client_dir):
            continue
        templates_dir = os.path.join(client_dir, 'templates')
        if not os.path.isdir(templates_dir):
            for sub_root, dirs, _ in os.walk(client_dir):
                if 'templates' in dirs:
                    templates_dir = os.path.join(sub_root, 'templates')
                    break
            else:
                continue

        templates = []
        for t in sorted(os.listdir(templates_dir)):
            if t.endswith('.html') or t.endswith('.htm'):
                if t.endswith('.htm') and os.path.exists(os.path.join(templates_dir, t + 'l')):
                    continue
                filepath = os.path.join(templates_dir, t)
                subject = ""
                html_body = ""
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        full_content = f.read()
                        m = re.search(r'EMAIL SUBJECT:\s*(.+)', full_content[:800])
                        if m:
                            subject = m.group(1).strip()
                        html_body = full_content
                except:
                    pass
                templates.append({
                    "file": t,
                    "subject": subject,
                    "raw_content": html_body
                })

        if templates:
            rel_path = templates_dir.replace('\\', '/')
            if rel_path.startswith('./'):
                rel_path = rel_path[2:]

            clients[item] = {
                "name": item,
                "path": rel_path,
                "source": source_label,
                "templates": templates
            }

for folder, label in SCAN_DIRS:
    scan_folder(folder, label)

# ═══════════════════════════════════════════════════════════════════════════════
# ALL 22 CANONICAL CRM ADMISSION ALERTS (CONCISE WORD-TO-WORD, ZERO EMOJIS)
# ═══════════════════════════════════════════════════════════════════════════════
CANONICAL_TEMPLATES = [
    {
        "id": "01_mobile_no_verification_otp",
        "category": "Authentication & Security",
        "name": "01. Mobile No. Verification OTP",
        "subject": "Mobile Verification OTP - {{school_name}}",
        "headline": "Mobile Number Verification",
        "greeting": "Dear Parent / Candidate,",
        "body": "Thank you for connecting with {{school_name}}.\n\nYour One-Time Password (OTP) for verifying your mobile number <strong>{{mobile_no}}</strong> is:\n\n<div style=\"text-align:center; margin:20px 0;\"><span style=\"display:inline-block; font-family:monospace; font-size:24px; font-weight:bold; letter-spacing:6px; background-color:#f1f5f9; color:#0f172a; padding:12px 28px; border-radius:6px; border:1px solid #cbd5e1;\">{{otp}}</span></div>\n\nThis OTP is valid for 10 minutes. For your security, please do not share this OTP with anyone.",
        "include_login": False,
        "login_prompt": "",
        "button_text": "VERIFY ON PORTAL"
    },
    {
        "id": "02_email_id_verification_otp",
        "category": "Authentication & Security",
        "name": "02. Email ID Verification OTP",
        "subject": "Email Verification OTP - {{school_name}}",
        "headline": "Email Address Verification",
        "greeting": "Dear Parent / Candidate,",
        "body": "Thank you for registering your interest with {{school_name}}.\n\nYour One-Time Password (OTP) for verifying your email address <strong>{{email}}</strong> is:\n\n<div style=\"text-align:center; margin:20px 0;\"><span style=\"display:inline-block; font-family:monospace; font-size:24px; font-weight:bold; letter-spacing:6px; background-color:#f1f5f9; color:#0f172a; padding:12px 28px; border-radius:6px; border:1px solid #cbd5e1;\">{{otp}}</span></div>\n\nThis OTP will expire in 10 minutes. Please enter this code on the verification screen to proceed.",
        "include_login": False,
        "login_prompt": "",
        "button_text": "CONFIRM EMAIL"
    },
    {
        "id": "03_candidate_login_with_otp",
        "category": "Authentication & Security",
        "name": "03. Candidate Login With OTP",
        "subject": "Candidate Login OTP - {{school_name}}",
        "headline": "Candidate Portal Login OTP",
        "greeting": "Dear {{student_name}} & Parents,",
        "body": "We received a login request for <strong>{{student_name}}</strong>'s candidate portal at <strong>{{school_name}}</strong> (Username: <strong>{{username}}</strong>).\n\nYour One-Time Password (OTP) to log in is:\n\n<div style=\"text-align:center; margin:20px 0;\"><span style=\"display:inline-block; font-family:monospace; font-size:24px; font-weight:bold; letter-spacing:6px; background-color:#f1f5f9; color:#0f172a; padding:12px 28px; border-radius:6px; border:1px solid #cbd5e1;\">{{otp}}</span></div>\n\nThis code is valid for 10 minutes. If you did not initiate this login request, please alert {{school_mobile_no}}.",
        "include_login": True,
        "login_prompt": "You may also log in using your registered credentials below:",
        "button_text": "CANDIDATE LOGIN"
    },
    {
        "id": "04_password_reset_communication_to_student",
        "category": "Authentication & Security",
        "name": "04. Password Reset Communication to Student",
        "subject": "Password Reset Successful - {{school_name}}",
        "headline": "Candidate Password Successfully Updated",
        "greeting": "Dear {{student_name}} & Parents,",
        "body": "This communication confirms that the login password for candidate account <strong>{{username}}</strong> was successfully updated on <strong>{{date}}</strong> at <strong>{{time}}</strong>.\n\nYou can now log in to the <strong>{{school_name}}</strong> Candidate Portal using your updated password to manage application forms, document uploads, and fee payments.\n\nIf you did not perform this change, please report it immediately to our admissions office at {{school_email_id}}.",
        "include_login": True,
        "login_prompt": "Access your candidate portal with your updated password:",
        "button_text": "CANDIDATE LOGIN"
    },
    {
        "id": "05_forget_password_otp_for_school",
        "category": "Authentication & Security",
        "name": "05. Forget Password OTP For School",
        "subject": "Staff Password Reset OTP - {{school_name}}",
        "headline": "Staff Portal Password Reset",
        "greeting": "Dear {{employee_name}},",
        "body": "A password reset request has been received for your school staff account at <strong>{{school_name}}</strong>.\n\nYour One-Time Password (OTP) is:\n\n<div style=\"text-align:center; margin:20px 0;\"><span style=\"display:inline-block; font-family:monospace; font-size:24px; font-weight:bold; letter-spacing:6px; background-color:#f1f5f9; color:#0f172a; padding:12px 28px; border-radius:6px; border:1px solid #cbd5e1;\">{{otp}}</span></div>\n\nThis code is valid for 10 minutes. If you did not make this request, please contact the campus administrator immediately.",
        "include_login": False,
        "login_prompt": "",
        "button_text": "RESET PASSWORD"
    },
    {
        "id": "06_forget_password_otp_for_student",
        "category": "Authentication & Security",
        "name": "06. Forget Password OTP For Student",
        "subject": "Password Reset OTP - {{school_name}}",
        "headline": "Reset Your Candidate Password",
        "greeting": "Dear {{student_name}} & Parents,",
        "body": "We received a request to reset the password for your admission portal account (Username: <strong>{{username}}</strong>).\n\nUse the following One-Time Password (OTP) to verify your identity and set a new password:\n\n<div style=\"text-align:center; margin:20px 0;\"><span style=\"display:inline-block; font-family:monospace; font-size:24px; font-weight:bold; letter-spacing:6px; background-color:#f1f5f9; color:#0f172a; padding:12px 28px; border-radius:6px; border:1px solid #cbd5e1;\">{{otp}}</span></div>\n\nThis OTP will expire in 10 minutes. Do not share this OTP with anyone.",
        "include_login": True,
        "login_prompt": "Or proceed directly to the portal recovery page:",
        "button_text": "RECOVER ACCOUNT"
    },
    {
        "id": "07_enquiry_acknowledgment",
        "category": "Enquiry & Counseling",
        "name": "07. Enquiry Acknowledgment",
        "subject": "Admission Enquiry Acknowledgment - {{school_name}}",
        "headline": "Admission Enquiry Received",
        "greeting": "Dear Parents,",
        "body": "Thank you for your interest in <strong>{{school_name}}</strong> for <strong>{{student_name}}</strong>'s admission for Class <strong>{{student_class}}</strong> (Academic Year: <strong>{{academic_year}}</strong>).\n\nYour Enquiry ID is <strong>{{enquiry_auto_id}}</strong> (Registered on: <strong>{{enquiry_date}}</strong>).\n\nOur Admissions Counselor, <strong>{{counsler_name}}</strong>, will review your details and connect with you shortly to assist you with the next steps.",
        "include_login": True,
        "login_prompt": "Complete your Application Form using your Candidate Portal credentials below:",
        "button_text": "ADMISSION PORTAL LOGIN"
    },
    {
        "id": "08_enquiry_notification_to_employee",
        "category": "Enquiry & Counseling",
        "name": "08. Enquiry Notification to Employee",
        "subject": "New Admission Enquiry #{{enquiry_auto_id}} - {{student_name}}",
        "headline": "New Admission Lead Assigned",
        "greeting": "Dear {{employee_name}},",
        "body": "A new admission enquiry has been logged in the CRM system and assigned to your department for follow-up.\n\n<strong>Lead Profile:</strong>\n&bull; Enquiry ID: <strong>{{enquiry_auto_id}}</strong>\n&bull; Student Name: <strong>{{student_name}}</strong> (Class: <strong>{{student_class}}</strong>)\n&bull; Parent: <strong>{{father_name}}</strong> / <strong>{{mother_name}}</strong>\n&bull; Contact: <strong>{{mobile_no}}</strong> | <strong>{{email}}</strong>\n&bull; Lead Source: <strong>{{lead_source}}</strong> (Campaign: {{lead_campaign}})\n&bull; Follow-Up Due Date: <strong>{{next_follow_up_date}}</strong>\n\nPlease log in to the CRM dashboard to initiate communication and record interaction notes.",
        "include_login": False,
        "login_prompt": "",
        "button_text": "OPEN CRM DASHBOARD"
    },
    {
        "id": "09_enquiry_notification_to_counsellor",
        "category": "Enquiry & Counseling",
        "name": "09. Enquiry Notification to Counsellor",
        "subject": "Counselor Assignment: Lead #{{enquiry_auto_id}} ({{student_name}} - {{student_class}})",
        "headline": "Admission Lead Allocated to You",
        "greeting": "Dear {{counsler_name}},",
        "body": "A prospective parent lead has been allocated to your counseling portfolio.\n\n<strong>Student Information:</strong>\n&bull; Student: <strong>{{student_name}}</strong> (Class: <strong>{{student_class}}</strong>)\n&bull; Enquiry Reference: <strong>{{enquiry_auto_id}}</strong>\n&bull; Father: <strong>{{father_name}}</strong> ({{father_mobile_no}})\n&bull; Mother: <strong>{{mother_name}}</strong> ({{mother_mobile_no}})\n&bull; Curriculum / Stream: <strong>{{curriculum}}</strong> / <strong>{{stream_name}}</strong>\n&bull; Source: <strong>{{lead_source}}</strong>\n\nPrevious Activity: <em>{{activity_name}} - {{last_remarks}}</em>\n\nPlease initiate connection with the family within the scheduled timeline.",
        "include_login": False,
        "login_prompt": "",
        "button_text": "VIEW LEAD IN CRM"
    },
    {
        "id": "10_duplicate_enquiry_communication_to_user",
        "category": "Enquiry & Counseling",
        "name": "10. In case of duplicate Enquiry Communication to User",
        "subject": "Admission Enquiry Status - {{school_name}}",
        "headline": "Existing Enquiry File Located",
        "greeting": "Dear Parents,",
        "body": "Thank you for reaching out to <strong>{{school_name}}</strong>.\n\nOur system indicates that an active admission enquiry for <strong>{{student_name}}</strong> (Class: <strong>{{student_class}}</strong>) is already on file under Enquiry ID: <strong>{{enquiry_auto_id}}</strong>.\n\nTo ensure consistent assistance without duplicate files, your assigned admissions counselor <strong>{{counsler_name}}</strong> will contact you on <strong>{{mobile_no}}</strong> regarding your existing enquiry. You do not need to register again.",
        "include_login": True,
        "login_prompt": "You can view your existing application status on the Candidate Portal:",
        "button_text": "CHECK APPLICATION STATUS"
    },
    {
        "id": "11_school_tour_scheduled",
        "category": "Campus Tours",
        "name": "11. School Tour Scheduled",
        "subject": "Campus Tour Confirmed - {{school_name}}",
        "headline": "Your Campus Walkthrough is Confirmed",
        "greeting": "Dear Parents,",
        "body": "We are delighted to welcome you and <strong>{{student_name}}</strong> for a guided campus tour at <strong>{{school_name}}</strong>.\n\n<strong>Tour Appointment Details:</strong>\n<div style=\"background-color:#f8fafc; border:1px solid #e2e8f0; border-radius:6px; padding:14px; margin:16px 0;\"><strong>Date:</strong> {{school_tour_date}}<br><strong>Time:</strong> {{school_tour_from_time}} to {{school_tour_to_time}}<br><strong>Campus Address:</strong> {{school_address}}</div>\nOur admissions executive will show you through our modern learning studios, science and innovation labs, sports arenas, and answer your curriculum questions.",
        "include_login": True,
        "login_prompt": "Access your candidate portal for campus location map and visitor pass:",
        "button_text": "CANDIDATE LOGIN"
    },
    {
        "id": "12_school_tour_reminder_to_candidate",
        "category": "Campus Tours",
        "name": "12. School Tour Reminder to Candidate",
        "subject": "Reminder: Your Campus Tour Tomorrow - {{school_name}}",
        "headline": "Campus Tour Reminder",
        "greeting": "Dear Parents,",
        "body": "This is a friendly reminder regarding your scheduled campus tour for <strong>{{student_name}}</strong> at <strong>{{school_name}}</strong>.\n\n<div style=\"background-color:#f8fafc; border:1px solid #e2e8f0; border-radius:6px; padding:14px; margin:16px 0;\"><strong>Scheduled Date:</strong> {{school_tour_date}}<br><strong>Time Slot:</strong> {{school_tour_from_time}} to {{school_tour_to_time}}<br><strong>Campus Location:</strong> {{school_address}}</div>\nKindly arrive 10 minutes prior to your designated slot. In case you need directions or wish to reschedule, feel free to contact our admissions desk at {{school_mobile_no}}.",
        "include_login": True,
        "login_prompt": "Manage tour details or view appointment pass on your Candidate Portal:",
        "button_text": "VIEW APPOINTMENT"
    },
    {
        "id": "13_school_tour_completed_thank_you",
        "category": "Campus Tours",
        "name": "13. School Tour Completed Thank You",
        "subject": "Thank You for Visiting {{school_name}}",
        "headline": "Thank You for Visiting Our Campus",
        "greeting": "Dear Parents,",
        "body": "It was our absolute pleasure hosting you and <strong>{{student_name}}</strong> for the campus walkthrough on <strong>{{school_tour_date}}</strong>.\n\nWe trust you experienced firsthand the vibrant academic community, caring mentors, and modern infrastructure that distinguish <strong>{{school_name}}</strong>.\n\n<strong>Next Steps:</strong> To secure your admission preference for Class <strong>{{student_class}}</strong>, kindly complete the online registration form and upload the required documents through your portal.",
        "include_login": True,
        "login_prompt": "Continue your admission application on the Candidate Portal below:",
        "button_text": "CONTINUE REGISTRATION"
    },
    {
        "id": "14_reschedule_school_tour",
        "category": "Campus Tours",
        "name": "14. Reschedule School Tour",
        "subject": "Campus Tour Rescheduled - {{school_name}}",
        "headline": "Campus Tour Slot Rescheduled",
        "greeting": "Dear Parents,",
        "body": "As per your request, your campus tour for <strong>{{student_name}}</strong> at <strong>{{school_name}}</strong> has been successfully rescheduled.\n\n<strong>Updated Campus Tour Schedule:</strong>\n<div style=\"background-color:#f8fafc; border:1px solid #e2e8f0; border-radius:6px; padding:14px; margin:16px 0;\"><strong>New Date:</strong> {{school_tour_date}}<br><strong>New Time Slot:</strong> {{school_tour_from_time}} to {{school_tour_to_time}}<br><strong>Campus Address:</strong> {{school_address}}</div>\nWe look forward to meeting you and your child on the revised date.",
        "include_login": True,
        "login_prompt": "Review your updated appointment on the Candidate Portal:",
        "button_text": "CANDIDATE LOGIN"
    },
    {
        "id": "15_one_to_one_meeting_offline_scheduled",
        "category": "Interactions & Meetings",
        "name": "15. One-to-One Meeting (Offline/In-person) Scheduled",
        "subject": "In-Person Interaction Scheduled - {{school_name}}",
        "headline": "One-to-One Interaction Confirmed",
        "greeting": "Dear Parents,",
        "body": "An in-person one-to-one interaction session has been confirmed for <strong>{{student_name}}</strong> (Application No: <strong>{{application_no}}</strong>) for Class <strong>{{student_class}}</strong>.\n\n<strong>Interaction Details:</strong>\n<div style=\"background-color:#f8fafc; border:1px solid #e2e8f0; border-radius:6px; padding:14px; margin:16px 0;\"><strong>Date:</strong> {{meeting_date}}<br><strong>Time:</strong> {{meeting_time}}<br><strong>Meeting Counselor:</strong> {{counsler_name}}<br><strong>Venue:</strong> {{school_address}}</div>\nPlease ensure both parents accompany the candidate. Kindly carry the child's previous year academic progress cards and birth certificate.",
        "include_login": True,
        "login_prompt": "Review interaction guidelines and documents checklist on your Candidate Portal:",
        "button_text": "CANDIDATE LOGIN"
    },
    {
        "id": "16_one_to_one_meeting_online_scheduled",
        "category": "Interactions & Meetings",
        "name": "16. One-to-One Meeting (Online/In-person) Scheduled",
        "subject": "Online Admission Interaction Scheduled - {{school_name}}",
        "headline": "Online Interaction Confirmed",
        "greeting": "Dear Parents,",
        "body": "Your online one-to-one admission interaction for <strong>{{student_name}}</strong> (Class: <strong>{{student_class}}</strong>) has been scheduled.\n\n<strong>Online Meeting Schedule & Access Link:</strong>\n<div style=\"background-color:#f8fafc; border:1px solid #e2e8f0; border-radius:6px; padding:14px; margin:16px 0;\"><strong>Date:</strong> {{meeting_date}}<br><strong>Time:</strong> {{meeting_time}}<br><strong>Counselor:</strong> {{counsler_name}}<br><strong>Meeting Video URL:</strong> <a href=\"{{meeting_url}}\" target=\"_blank\" style=\"color:#0284c7; font-weight:bold;\">{{meeting_url}}</a></div>\nPlease join the meeting link 5 minutes prior to the scheduled time in a quiet environment with audio and video enabled.",
        "include_login": True,
        "login_prompt": "You can also join the session directly from your Candidate Portal:",
        "button_text": "JOIN FROM PORTAL"
    },
    {
        "id": "17_meeting_reminder_to_candidate",
        "category": "Interactions & Meetings",
        "name": "17. Meeting Reminder to Candidate",
        "subject": "Reminder: Interaction Scheduled - {{school_name}}",
        "headline": "Admission Interaction Reminder",
        "greeting": "Dear Parents,",
        "body": "This is a friendly reminder that your scheduled one-to-one interaction for <strong>{{student_name}}</strong> (Application No: <strong>{{application_no}}</strong>) is approaching.\n\n<div style=\"background-color:#f8fafc; border:1px solid #e2e8f0; border-radius:6px; padding:14px; margin:16px 0;\"><strong>Date:</strong> {{meeting_date}}<br><strong>Time:</strong> {{meeting_time}}<br><strong>Assigned Counselor:</strong> {{counsler_name}}<br><strong>Link / Venue:</strong> {{meeting_url}}</div>\nOur academic panel looks forward to an engaging discussion with you and {{student_name}}.",
        "include_login": True,
        "login_prompt": "Access your meeting link and candidate details on the portal:",
        "button_text": "CANDIDATE LOGIN"
    },
    {
        "id": "18_meeting_completed_to_candidate",
        "category": "Interactions & Meetings",
        "name": "18. Meeting Completed to Candidate",
        "subject": "Interaction Completed - {{school_name}}",
        "headline": "Interaction Successfully Completed",
        "greeting": "Dear Parents,",
        "body": "Thank you for participating in the interaction session with our educators for <strong>{{student_name}}</strong> (Application No: <strong>{{application_no}}</strong>) at <strong>{{school_name}}</strong>.\n\nOur Admissions Committee is currently reviewing the interaction assessment and application records. We will communicate the provisional admission decision and offer details shortly.\n\nYou may monitor your application status in real-time through your candidate portal.",
        "include_login": True,
        "login_prompt": "Track application status and view remarks on your Candidate Portal:",
        "button_text": "TRACK APPLICATION"
    },
    {
        "id": "19_reschedule_meeting_alert_to_candidate",
        "category": "Interactions & Meetings",
        "name": "19. Reschedule Meeting alert to Candidate",
        "subject": "Interaction Rescheduled - {{school_name}}",
        "headline": "Interaction Session Rescheduled",
        "greeting": "Dear Parents,",
        "body": "Your one-to-one admission interaction for <strong>{{student_name}}</strong> (Class: <strong>{{student_class}}</strong>) has been rescheduled.\n\n<strong>Revised Interaction Schedule:</strong>\n<div style=\"background-color:#f8fafc; border:1px solid #e2e8f0; border-radius:6px; padding:14px; margin:16px 0;\"><strong>New Date:</strong> {{meeting_date}}<br><strong>New Time:</strong> {{meeting_time}}<br><strong>Counselor:</strong> {{counsler_name}}<br><strong>Meeting Link / Venue:</strong> {{meeting_url}}</div>\nPlease review the updated appointment in your candidate portal.",
        "include_login": True,
        "login_prompt": "Confirm attendance or modify preferences on the Candidate Portal:",
        "button_text": "CANDIDATE LOGIN"
    },
    {
        "id": "20_adhoc_payment_alert_to_candidate",
        "category": "Fee & Payments",
        "name": "20. Adhoc Payment Alert to Candidate",
        "subject": "Payment Notice: {{current_fee_receipt_head}} - {{school_name}}",
        "headline": "Admission Fee Payment Notice",
        "greeting": "Dear Parents,",
        "body": "This communication is regarding the fee payment for <strong>{{student_name}}</strong> (Application No: <strong>{{application_no}}</strong>) for Class <strong>{{student_class}}</strong>.\n\n<strong>Payment Details:</strong>\n<div style=\"background-color:#f8fafc; border:1px solid #e2e8f0; border-radius:6px; padding:14px; margin:16px 0;\"><strong>Fee Component:</strong> {{current_fee_receipt_head}}<br><strong>Payable Amount:</strong> INR <strong>{{current_fee_receipt_amount}}</strong><br><strong>Issue Date:</strong> {{issueDate}}</div>\nKindly complete the payment through our secure payment gateway to ensure uninterrupted processing of your application.",
        "include_login": True,
        "login_prompt": "Pay online directly through your Candidate Portal or click below:",
        "button_text": "PAY FEE ONLINE"
    },
    {
        "id": "21_fee_receipt_download_url_alert_to_candidate",
        "category": "Fee & Payments",
        "name": "21. Fee Receipt Download URL Alert to Candidate",
        "subject": "Fee Receipt Ready: {{current_fee_receipt_head}} - {{school_name}}",
        "headline": "Fee Payment Receipt Generated",
        "greeting": "Dear Parents,",
        "body": "We gratefully acknowledge receipt of INR <strong>{{current_fee_receipt_paid_amount}}</strong> towards <strong>{{current_fee_receipt_head}}</strong> for <strong>{{student_name}}</strong> (Application No: <strong>{{application_no}}</strong>).\n\nYour official computerized fee receipt is generated and ready for instant download.\n\n<div style=\"margin:16px 0;\"><a href=\"{{registration_fee_payment_fee_receipt_url}}\" target=\"_blank\" style=\"display:inline-block; padding:10px 22px; background-color:#107c41; color:#ffffff; text-decoration:none; border-radius:4px; font-weight:bold; font-size:13px;\">Download Official Receipt (PDF) &rarr;</a></div>\nA permanent record of this transaction is also saved under your Candidate Portal ledger.",
        "include_login": True,
        "login_prompt": "Access your candidate portal to view fee ledger and transaction history:",
        "button_text": "VIEW FEE LEDGER"
    },
    {
        "id": "22_candidate_login",
        "category": "Candidate Portal",
        "name": "22. Candidate Login",
        "subject": "Candidate Portal Credentials - {{school_name}}",
        "headline": "Welcome to Your Candidate Portal",
        "greeting": "Dear Parents,",
        "body": "Welcome to <strong>{{school_name}}</strong> Admission Portal for <strong>{{student_name}}</strong> (Class: <strong>{{student_class}}</strong>).\n\nYour candidate account has been activated. Through your secure portal, you can:\n&bull; Complete and submit the Admission Application Form\n&bull; Upload mandatory student and parent documents\n&bull; Pay registration and admission fees online\n&bull; View interaction schedules and download offer letters\n\nPlease find your secure login credentials below.",
        "include_login": True,
        "login_prompt": "Use your registered credentials to log in to the Admission Portal:",
        "button_text": "ADMISSION PORTAL LOGIN"
    }
]

# ═══════════════════════════════════════════════════════════════════════════════
# CLIENT CAMPUSES (Zero About-Campus, Clean Links)
# ═══════════════════════════════════════════════════════════════════════════════
CLIENT_CAMPUSES = {
    "Simply Admission": {
        "campus_name": "Simply Admission",
        "campus_address": "Simply Admission, Sector 68, Noida, Uttar Pradesh, India",
        "campus_location_link": "https://www.google.com/maps/search/Simply+Admission,+Noida+Sector+68",
        "campus_logo_link": "https://resources.edunexttechnologies.com/web-data/simplyadmission/img/Simpli_Admission-logo.png",
        "website": "http://simplyadmission.com",
        "candidate_login_url": "{{school_url}}",
        "theme_color": "#11a14a",
        "bg_color": "#f4f5f7",
        "brand_font": "'Segoe UI', Arial, sans-serif",
        "facebook": "https://www.facebook.com/simplyadmission",
        "instagram": "https://www.instagram.com/simply_admission/",
        "twitter": "https://twitter.com/AdmissionSimply",
        "linkedin": "https://www.linkedin.com/company/simplyadmission/?viewAsMember=true",
        "youtube": "",
        "doc_links": [
            {"title": "Admission Portal Login", "url": "http://simplyadmission.com", "category": "Candidate Portal", "note": "Primary admission workflow link"},
            {"title": "Online Registration Form", "url": "http://simplyadmission.com/clp/SimplyAdmission", "category": "Application Form", "note": "Student online registration page"}
        ]
    }
}

# ═══════════════════════════════════════════════════════════════════════════════
# CRM VARIABLES 68 KEYS DICTIONARY (LOADED FROM variables.json)
# ═══════════════════════════════════════════════════════════════════════════════
vars_path = os.path.join(os.path.dirname(__file__), "variables.json")
raw_vars = {}
if os.path.exists(vars_path):
    with open(vars_path, "r", encoding="utf-8") as f:
        raw_vars = json.load(f)

SAMPLES_MAP = {
    "student_name": "Aarav Sharma",
    "enquiry_auto_id": "ENQ-2026-8849",
    "passwords": "Pass@2026#",
    "username": "aarav.sharma26",
    "student_class": "Grade 1",
    "father_name": "Rajesh Sharma",
    "mother_name": "Pooja Sharma",
    "academic_year": "2026-2027",
    "curriculum": "CBSE",
    "father_email": "rajesh.sharma@example.com",
    "father_mobile_no": "+91 98765 43210",
    "mother_email": "pooja.sharma@example.com",
    "mother_mobile_no": "+91 98765 43211",
    "date": "15-Oct-2026",
    "time": "10:30 AM",
    "otp": "489201",
    "email": "parents.sharma@example.com",
    "mobile_no": "+91 98765 43210",
    "school_name": "Simply Admission",
    "counsler_name": "Ms. Ananya Sen",
    "enquiry_stage_name": "Campus Visit Scheduled",
    "enquiry_sub_stage_name": "Slot Confirmed",
    "application_stage_name": "Document Verification",
    "application_sub_stage_name": "Pending Records",
    "next_follow_up_date": "20-Oct-2026",
    "last_remarks": "Parents confirmed walkthrough attendance",
    "activity_name": "Interaction Booking",
    "sub_activity_name": "Email Notification Sent",
    "sub_activity_reason_name": "Slot Booking Acknowledgement",
    "current_fee_receipt_head": "Registration & Assessment Fee",
    "current_fee_receipt_amount": "2,500",
    "application_no": "APP-2026-1042",
    "lead_source": "Website Enquiry",
    "lead_medium": "Organic Search",
    "lead_campaign": "Admissions 2026-27",
    "last_followup_date": "10-Oct-2026",
    "last_followup_time": "04:15 PM",
    "stream_name": "Science & Technology",
    "enquiry_date": "08-Oct-2026",
    "meeting_url": "https://meet.google.com/adm-2026-xyz",
    "school_url": "https://simplyadmission.com",
    "output_form_url": "https://simplyadmission.com/form/download/APP-2026-1042",
    "admissionNo": "ADM-2026-0512",
    "employee_name": "Mr. Rohit Verma",
    "school_tour_date": "18-Oct-2026",
    "school_tour_from_time": "10:00 AM",
    "school_tour_to_time": "11:30 AM",
    "payment_link": "https://portal.simplyadmission.com/pay/online-fee/APP-2026-1042",
    "payment_link_whats_app": "https://wa.me/919876543210?text=PayFee",
    "school_address": "Noida Sector 68, UP, India",
    "school_email_id": "admissions@simplyadmission.com",
    "school_mobile_no": "+91 99999 88888",
    "source_of_info": "School Recommendation",
    "is_single_parent": "No",
    "parent_type": "Both Parents",
    "current_fee_receipt_paid_amount": "2,500",
    "current_fee_receipt_head_amount": "Registration Fee: 2,500",
    "payment_link_barcode": "https://resources.edunexttechnologies.com/web-data/sample-qr.png",
    "meeting_date": "16-Oct-2026",
    "meeting_time": "11:00 AM",
    "bankName": "HDFC Bank Ltd",
    "branchName": "Noida Sector 62",
    "issueDate": "11-Oct-2026",
    "guardian_name": "Vikram Sharma",
    "guardian_email_id": "vikram.sharma@example.com",
    "guardian_mobile_no": "+91 98111 22334",
    "admission_fee_payment_fee_receipt_url": "https://portal.simplyadmission.com/receipt/adm-fee-2026.pdf",
    "registration_fee_payment_fee_receipt_url": "https://portal.simplyadmission.com/receipt/reg-fee-2026.pdf"
}

CATEGORY_MAPPINGS = {
    "Student & Academic": ["student_name", "student_class", "academic_year", "curriculum", "stream_name", "admissionNo"],
    "Credentials & Portal": ["username", "passwords", "otp", "output_form_url"],
    "Parents & Family": ["father_name", "father_mobile_no", "father_email", "mother_name", "mother_mobile_no", "mother_email", "guardian_name", "guardian_mobile_no", "guardian_email_id", "is_single_parent", "parent_type"],
    "Enquiry & Application": ["enquiry_auto_id", "application_no", "enquiry_date", "enquiry_stage_name", "enquiry_sub_stage_name", "application_stage_name", "application_sub_stage_name", "counsler_name", "employee_name", "last_remarks", "next_follow_up_date"],
    "Fee & Payment": ["current_fee_receipt_head", "current_fee_receipt_amount", "current_fee_receipt_paid_amount", "current_fee_receipt_head_amount", "payment_link", "payment_link_whats_app", "payment_link_barcode", "admission_fee_payment_fee_receipt_url", "registration_fee_payment_fee_receipt_url", "bankName", "branchName", "issueDate"],
    "Tours & Meetings": ["school_tour_date", "school_tour_from_time", "school_tour_to_time", "meeting_date", "meeting_time", "meeting_url", "date", "time", "last_followup_date", "last_followup_time"],
    "School & Contact": ["school_name", "school_address", "school_email_id", "school_mobile_no", "school_url", "email", "mobile_no"],
    "Marketing & Source": ["lead_source", "lead_medium", "lead_campaign", "source_of_info", "activity_name", "sub_activity_name", "sub_activity_reason_name"]
}

CRM_VARIABLES_CATALOG = {}
assigned_keys = set()
for cat, keys in CATEGORY_MAPPINGS.items():
    CRM_VARIABLES_CATALOG[cat] = []
    for k in keys:
        if k in raw_vars:
            CRM_VARIABLES_CATALOG[cat].append({
                "key": k,
                "label": raw_vars[k],
                "sample": SAMPLES_MAP.get(k, f"[{raw_vars[k]}]")
            })
            assigned_keys.add(k)

other_keys = [k for k in raw_vars.keys() if k not in assigned_keys]
if other_keys:
    CRM_VARIABLES_CATALOG["Other Details"] = []
    for k in other_keys:
        CRM_VARIABLES_CATALOG["Other Details"].append({
            "key": k,
            "label": raw_vars[k],
            "sample": SAMPLES_MAP.get(k, f"[{raw_vars[k]}]")
        })

clients_json = json.dumps(clients)
templates_json = json.dumps(CANONICAL_TEMPLATES)
campuses_json = json.dumps(CLIENT_CAMPUSES)
crm_vars_json = json.dumps(CRM_VARIABLES_CATALOG)

# Write modern template generator
import scripts.generate_dashboard_html as gen_html
gen_html.build(clients_json, templates_json, campuses_json, crm_vars_json)

print("Rebuilt index.html with Optimized Fully Responsive Minimalist UI/UX!")
