import os
import shutil

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "samples", "Canonical Suite", "templates")

# Common CDN icons
ICON_FB = "https://img.icons8.com/color/48/facebook-new.png"
ICON_INSTA = "https://img.icons8.com/color/48/instagram-new--v1.png"
ICON_LI = "https://img.icons8.com/color/48/linkedin.png"
ICON_MAP = "https://img.icons8.com/color/48/google-maps-new.png"
ICON_WEB = "https://img.icons8.com/color/48/domain--v1.png"

LOGO_URL = "https://resources.edunexttechnologies.com/web-data/simplyadmission/img/Simpli_Admission-logo.png"
THEME_COLOR = "#11a14a"

TEMPLATES_DATA = [
    {
        "filename": "01_mobile_no_verification_otp.html",
        "alert_name": "Mobile No. Verification OTP",
        "subject": "Mobile Verification OTP - {{school_name}}",
        "headline": "Mobile Number Verification",
        "greeting": "Dear Parent / Candidate,",
        "body": """<p style="margin: 0 0 16px 0;">Thank you for connecting with <strong>{{school_name}}</strong>.</p>
<p style="margin: 0 0 16px 0;">Your One-Time Password (OTP) for verifying your mobile number <strong>{{mobile_no}}</strong> is:</p>
<div style="text-align: center; margin: 20px 0;">
  <span style="display: inline-block; font-family: monospace; font-size: 24px; font-weight: bold; letter-spacing: 6px; background-color: #f1f5f9; color: #0f172a; padding: 12px 28px; border-radius: 6px; border: 1px solid #cbd5e1;">{{otp}}</span>
</div>
<p style="margin: 0 0 16px 0;">This OTP is valid for 10 minutes. For your security, do not share this OTP with anyone.</p>
<div style="margin: 18px 0;">
  <a href="{{school_url}}" target="_blank" style="display: inline-block; padding: 10px 22px; background-color: #11a14a; color: #ffffff; text-decoration: none; border-radius: 4px; font-weight: bold; font-size: 13px;">Verify on Portal &rarr;</a>
</div>"""
    },
    {
        "filename": "02_email_id_verification_otp.html",
        "alert_name": "Email ID Verification OTP",
        "subject": "Email Verification OTP - {{school_name}}",
        "headline": "Email Address Verification",
        "greeting": "Dear Parent / Candidate,",
        "body": """<p style="margin: 0 0 16px 0;">Thank you for registering your interest with <strong>{{school_name}}</strong>.</p>
<p style="margin: 0 0 16px 0;">Your One-Time Password (OTP) for verifying your email address <strong>{{email}}</strong> is:</p>
<div style="text-align: center; margin: 20px 0;">
  <span style="display: inline-block; font-family: monospace; font-size: 24px; font-weight: bold; letter-spacing: 6px; background-color: #f1f5f9; color: #0f172a; padding: 12px 28px; border-radius: 6px; border: 1px solid #cbd5e1;">{{otp}}</span>
</div>
<p style="margin: 0 0 16px 0;">This OTP is valid for 10 minutes. Please enter this code on the verification screen to proceed.</p>
<div style="margin: 18px 0;">
  <a href="{{school_url}}" target="_blank" style="display: inline-block; padding: 10px 22px; background-color: #11a14a; color: #ffffff; text-decoration: none; border-radius: 4px; font-weight: bold; font-size: 13px;">Confirm Email &rarr;</a>
</div>"""
    },
    {
        "filename": "03_candidate_login_with_otp.html",
        "alert_name": "Candidate Login With OTP",
        "subject": "Candidate Login OTP - {{school_name}}",
        "headline": "Candidate Portal Login OTP",
        "greeting": "Dear {{student_name}} & Parents,",
        "body": """<p style="margin: 0 0 16px 0;">We received a login request for <strong>{{student_name}}</strong>'s candidate portal at <strong>{{school_name}}</strong> (Username: <strong>{{username}}</strong>).</p>
<p style="margin: 0 0 16px 0;">Your One-Time Password (OTP) is:</p>
<div style="text-align: center; margin: 20px 0;">
  <span style="display: inline-block; font-family: monospace; font-size: 24px; font-weight: bold; letter-spacing: 6px; background-color: #f1f5f9; color: #0f172a; padding: 12px 28px; border-radius: 6px; border: 1px solid #cbd5e1;">{{otp}}</span>
</div>
<p style="margin: 0 0 16px 0;">This code is valid for 10 minutes. If you did not initiate this login request, please alert {{school_mobile_no}}.</p>
<div style="margin: 18px 0;">
  <a href="{{school_url}}" target="_blank" style="display: inline-block; padding: 10px 22px; background-color: #11a14a; color: #ffffff; text-decoration: none; border-radius: 4px; font-weight: bold; font-size: 13px;">Login to Portal &rarr;</a>
</div>"""
    },
    {
        "filename": "04_password_reset_communication_to_student.html",
        "alert_name": "Password Reset Communication to Student",
        "subject": "Password Reset Successful - {{school_name}}",
        "headline": "Candidate Password Successfully Updated",
        "greeting": "Dear {{student_name}} & Parents,",
        "body": """<p style="margin: 0 0 16px 0;">This is to confirm that the login password for candidate account <strong>{{username}}</strong> was successfully updated on <strong>{{date}}</strong> at <strong>{{time}}</strong>.</p>
<p style="margin: 0 0 16px 0;">You can now log in to the <strong>{{school_name}}</strong> Candidate Portal using your updated password to manage application forms, document uploads, and fee payments.</p>
<p style="margin: 0 0 16px 0;">If you did not make this change, please contact us immediately at <strong>{{school_email_id}}</strong> or <strong>{{school_mobile_no}}</strong>.</p>
<div style="margin: 18px 0;">
  <a href="{{school_url}}" target="_blank" style="display: inline-block; padding: 10px 22px; background-color: #11a14a; color: #ffffff; text-decoration: none; border-radius: 4px; font-weight: bold; font-size: 13px;">Candidate Login &rarr;</a>
</div>"""
    },
    {
        "filename": "05_forget_password_otp_for_school.html",
        "alert_name": "Forget Password OTP For School",
        "subject": "Staff Password Reset OTP - {{school_name}}",
        "headline": "Staff Portal Password Reset",
        "greeting": "Dear {{employee_name}},",
        "body": """<p style="margin: 0 0 16px 0;">A password reset request was submitted for your staff account at <strong>{{school_name}}</strong>.</p>
<p style="margin: 0 0 16px 0;">Your One-Time Password (OTP) is:</p>
<div style="text-align: center; margin: 20px 0;">
  <span style="display: inline-block; font-family: monospace; font-size: 24px; font-weight: bold; letter-spacing: 6px; background-color: #f1f5f9; color: #0f172a; padding: 12px 28px; border-radius: 6px; border: 1px solid #cbd5e1;">{{otp}}</span>
</div>
<p style="margin: 0 0 16px 0;">This OTP will expire in 10 minutes. If you did not request this, please notify the campus administrator.</p>
<div style="margin: 18px 0;">
  <a href="{{school_url}}" target="_blank" style="display: inline-block; padding: 10px 22px; background-color: #11a14a; color: #ffffff; text-decoration: none; border-radius: 4px; font-weight: bold; font-size: 13px;">Reset Password &rarr;</a>
</div>"""
    },
    {
        "filename": "06_forget_password_otp_for_student.html",
        "alert_name": "Forget Password OTP For Student",
        "subject": "Password Reset OTP - {{school_name}}",
        "headline": "Reset Candidate Password",
        "greeting": "Dear {{student_name}} & Parents,",
        "body": """<p style="margin: 0 0 16px 0;">We received a request to reset the password for your admission portal account (Username: <strong>{{username}}</strong>).</p>
<p style="margin: 0 0 16px 0;">Your One-Time Password (OTP) to set a new password is:</p>
<div style="text-align: center; margin: 20px 0;">
  <span style="display: inline-block; font-family: monospace; font-size: 24px; font-weight: bold; letter-spacing: 6px; background-color: #f1f5f9; color: #0f172a; padding: 12px 28px; border-radius: 6px; border: 1px solid #cbd5e1;">{{otp}}</span>
</div>
<p style="margin: 0 0 16px 0;">This OTP is valid for 10 minutes. Do not share this OTP with anyone.</p>
<div style="margin: 18px 0;">
  <a href="{{school_url}}" target="_blank" style="display: inline-block; padding: 10px 22px; background-color: #11a14a; color: #ffffff; text-decoration: none; border-radius: 4px; font-weight: bold; font-size: 13px;">Reset Password &rarr;</a>
</div>"""
    },
    {
        "filename": "07_enquiry_acknowledgment.html",
        "alert_name": "Enquiry Acknowledgment",
        "subject": "Admission Enquiry Acknowledgment - {{school_name}}",
        "headline": "Admission Enquiry Received",
        "greeting": "Dear Parents,",
        "body": """<p style="margin: 0 0 16px 0;">Thank you for your interest in <strong>{{school_name}}</strong> for <strong>{{student_name}}</strong>'s admission for Class <strong>{{student_class}}</strong> (Academic Year: <strong>{{academic_year}}</strong>).</p>
<p style="margin: 0 0 16px 0;">Your Enquiry ID is <strong>{{enquiry_auto_id}}</strong> (Registered on: <strong>{{enquiry_date}}</strong>).</p>
<p style="margin: 0 0 16px 0;">Our Admissions Counselor, <strong>{{counsler_name}}</strong>, will connect with you shortly to assist with next steps.</p>
<table width="100%" border="0" cellpadding="0" cellspacing="0" style="margin: 18px 0; background-color: #f8fafc; border: 1px solid #e2e8f0; border-left: 4px solid #11a14a; border-radius: 4px;">
  <tr>
    <td style="padding: 14px 18px; font-family: Arial, sans-serif; font-size: 13px; color: #333333; line-height: 1.6;">
      <div style="font-weight: bold; color: #1e293b; margin-bottom: 6px;">PORTAL LOGIN CREDENTIALS</div>
      <div>Portal URL: <a href="{{school_url}}" target="_blank" style="color: #11a14a; font-weight: bold;">{{school_url}}</a></div>
      <div>Username: <span style="font-family: monospace; background-color: #e2e8f0; padding: 2px 6px; border-radius: 3px;">{{username}}</span></div>
      <div>Password: <span style="font-family: monospace; background-color: #e2e8f0; padding: 2px 6px; border-radius: 3px;">{{passwords}}</span></div>
    </td>
  </tr>
</table>
<div style="margin: 18px 0;">
  <a href="{{school_url}}" target="_blank" style="display: inline-block; padding: 10px 22px; background-color: #11a14a; color: #ffffff; text-decoration: none; border-radius: 4px; font-weight: bold; font-size: 13px;">Admission Portal Login &rarr;</a>
</div>"""
    },
    {
        "filename": "08_enquiry_notification_to_employee.html",
        "alert_name": "Enquiry Notification to Employee",
        "subject": "New Admission Enquiry #{{enquiry_auto_id}} - {{student_name}}",
        "headline": "New Admission Lead Assigned",
        "greeting": "Dear {{employee_name}},",
        "body": """<p style="margin: 0 0 16px 0;">A new admission enquiry has been assigned to your department for follow-up.</p>
<div style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 14px 18px; margin: 16px 0; font-size: 13px; line-height: 1.6;">
  <strong>Lead Profile:</strong><br/>
  &bull; Enquiry ID: <strong>{{enquiry_auto_id}}</strong> (Date: {{enquiry_date}})<br/>
  &bull; Student Name: <strong>{{student_name}}</strong> (Class: <strong>{{student_class}}</strong>)<br/>
  &bull; Father: <strong>{{father_name}}</strong> ({{father_mobile_no}} | {{father_email}})<br/>
  &bull; Mother: <strong>{{mother_name}}</strong> ({{mother_mobile_no}} | {{mother_email}})<br/>
  &bull; Lead Source: <strong>{{lead_source}}</strong> (Campaign: {{lead_campaign}})<br/>
  &bull; Next Follow-Up Date: <strong>{{next_follow_up_date}}</strong>
</div>
<p style="margin: 0 0 16px 0;">Please review the lead details in CRM and initiate connection within the designated timeline.</p>
<div style="margin: 18px 0;">
  <a href="{{school_url}}" target="_blank" style="display: inline-block; padding: 10px 22px; background-color: #11a14a; color: #ffffff; text-decoration: none; border-radius: 4px; font-weight: bold; font-size: 13px;">Open CRM Dashboard &rarr;</a>
</div>"""
    },
    {
        "filename": "09_enquiry_notification_to_counsellor.html",
        "alert_name": "Enquiry Notification to Counsellor",
        "subject": "Counselor Assignment: Lead #{{enquiry_auto_id}} ({{student_name}} - {{student_class}})",
        "headline": "Admission Lead Allocated to You",
        "greeting": "Dear {{counsler_name}},",
        "body": """<p style="margin: 0 0 16px 0;">A prospective student lead has been assigned to your counseling portfolio.</p>
<div style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 14px 18px; margin: 16px 0; font-size: 13px; line-height: 1.6;">
  <strong>Student Details:</strong><br/>
  &bull; Student Name: <strong>{{student_name}}</strong> (Class: <strong>{{student_class}}</strong>)<br/>
  &bull; Enquiry Reference: <strong>{{enquiry_auto_id}}</strong><br/>
  &bull; Curriculum / Stream: <strong>{{curriculum}}</strong> / <strong>{{stream_name}}</strong><br/>
  &bull; Father: <strong>{{father_name}}</strong> ({{father_mobile_no}})<br/>
  &bull; Mother: <strong>{{mother_name}}</strong> ({{mother_mobile_no}})<br/>
  &bull; Source: <strong>{{lead_source}}</strong><br/>
  &bull; Last Remarks: <em>{{last_remarks}}</em>
</div>
<p style="margin: 0 0 16px 0;">Kindly connect with the parents and schedule the next interaction.</p>
<div style="margin: 18px 0;">
  <a href="{{school_url}}" target="_blank" style="display: inline-block; padding: 10px 22px; background-color: #11a14a; color: #ffffff; text-decoration: none; border-radius: 4px; font-weight: bold; font-size: 13px;">View Lead in CRM &rarr;</a>
</div>"""
    },
    {
        "filename": "10_duplicate_enquiry_communication_to_user.html",
        "alert_name": "In case of duplicate Enquiry Communication to User",
        "subject": "Admission Enquiry Status - {{school_name}}",
        "headline": "Existing Enquiry File Located",
        "greeting": "Dear Parents,",
        "body": """<p style="margin: 0 0 16px 0;">Thank you for contacting <strong>{{school_name}}</strong>.</p>
<p style="margin: 0 0 16px 0;">Our records indicate that an active admission enquiry for <strong>{{student_name}}</strong> (Class: <strong>{{student_class}}</strong>) is already registered under Enquiry ID: <strong>{{enquiry_auto_id}}</strong>.</p>
<p style="margin: 0 0 16px 0;">Your designated counselor <strong>{{counsler_name}}</strong> is handling your file and will contact you directly on <strong>{{mobile_no}}</strong>. You do not need to register again.</p>
<div style="margin: 18px 0;">
  <a href="{{school_url}}" target="_blank" style="display: inline-block; padding: 10px 22px; background-color: #11a14a; color: #ffffff; text-decoration: none; border-radius: 4px; font-weight: bold; font-size: 13px;">Check Application Status &rarr;</a>
</div>"""
    },
    {
        "filename": "11_school_tour_scheduled.html",
        "alert_name": "School Tour Scheduled",
        "subject": "Campus Tour Confirmed - {{school_name}}",
        "headline": "Campus Tour Appointment Confirmed",
        "greeting": "Dear Parents,",
        "body": """<p style="margin: 0 0 16px 0;">We are delighted to confirm your guided campus tour for <strong>{{student_name}}</strong> at <strong>{{school_name}}</strong>.</p>
<div style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 14px 18px; margin: 16px 0; font-size: 13px; line-height: 1.6;">
  <strong>Tour Schedule:</strong><br/>
  &bull; Date: <strong>{{school_tour_date}}</strong><br/>
  &bull; Time: <strong>{{school_tour_from_time}} to {{school_tour_to_time}}</strong><br/>
  &bull; Campus Address: <strong>{{school_address}}</strong><br/>
  &bull; Contact Desk: <strong>{{school_mobile_no}}</strong>
</div>
<p style="margin: 0 0 16px 0;">Our admissions counselor will guide you through the classrooms, activity centers, and sports facilities.</p>
<div style="margin: 18px 0;">
  <a href="{{school_url}}" target="_blank" style="display: inline-block; padding: 10px 22px; background-color: #11a14a; color: #ffffff; text-decoration: none; border-radius: 4px; font-weight: bold; font-size: 13px;">View Tour Pass &rarr;</a>
</div>"""
    },
    {
        "filename": "12_school_tour_reminder_to_candidate.html",
        "alert_name": "School Tour Reminder to Candidate",
        "subject": "Reminder: Scheduled Campus Tour - {{school_name}}",
        "headline": "Campus Tour Reminder",
        "greeting": "Dear Parents,",
        "body": """<p style="margin: 0 0 16px 0;">This is a friendly reminder regarding your scheduled campus tour for <strong>{{student_name}}</strong> at <strong>{{school_name}}</strong>.</p>
<div style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 14px 18px; margin: 16px 0; font-size: 13px; line-height: 1.6;">
  <strong>Appointment Details:</strong><br/>
  &bull; Scheduled Date: <strong>{{school_tour_date}}</strong><br/>
  &bull; Time Slot: <strong>{{school_tour_from_time}} to {{school_tour_to_time}}</strong><br/>
  &bull; Location: <strong>{{school_address}}</strong>
</div>
<p style="margin: 0 0 16px 0;">Kindly arrive 10 minutes prior to your time slot. If you need assistance, please call <strong>{{school_mobile_no}}</strong>.</p>
<div style="margin: 18px 0;">
  <a href="{{school_url}}" target="_blank" style="display: inline-block; padding: 10px 22px; background-color: #11a14a; color: #ffffff; text-decoration: none; border-radius: 4px; font-weight: bold; font-size: 13px;">View Appointment &rarr;</a>
</div>"""
    },
    {
        "filename": "13_school_tour_completed_thank_you.html",
        "alert_name": "School Tour Completed Thank You",
        "subject": "Thank You for Visiting {{school_name}}",
        "headline": "Thank You for Visiting Our Campus",
        "greeting": "Dear Parents,",
        "body": """<p style="margin: 0 0 16px 0;">It was a pleasure hosting you and <strong>{{student_name}}</strong> for the campus tour on <strong>{{school_tour_date}}</strong>.</p>
<p style="margin: 0 0 16px 0;">We hope you had a pleasant experience exploring the academic facilities and environment at <strong>{{school_name}}</strong>.</p>
<p style="margin: 0 0 16px 0;"><strong>Next Step:</strong> To proceed with admission for Class <strong>{{student_class}}</strong>, please complete your online application and document submission on the candidate portal.</p>
<div style="margin: 18px 0;">
  <a href="{{school_url}}" target="_blank" style="display: inline-block; padding: 10px 22px; background-color: #11a14a; color: #ffffff; text-decoration: none; border-radius: 4px; font-weight: bold; font-size: 13px;">Complete Application &rarr;</a>
</div>"""
    },
    {
        "filename": "14_reschedule_school_tour.html",
        "alert_name": "Reschedule School Tour",
        "subject": "Campus Tour Rescheduled - {{school_name}}",
        "headline": "Campus Tour Slot Rescheduled",
        "greeting": "Dear Parents,",
        "body": """<p style="margin: 0 0 16px 0;">As per your request, your campus tour for <strong>{{student_name}}</strong> at <strong>{{school_name}}</strong> has been rescheduled.</p>
<div style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 14px 18px; margin: 16px 0; font-size: 13px; line-height: 1.6;">
  <strong>Revised Tour Details:</strong><br/>
  &bull; New Date: <strong>{{school_tour_date}}</strong><br/>
  &bull; New Time: <strong>{{school_tour_from_time}} to {{school_tour_to_time}}</strong><br/>
  &bull; Venue: <strong>{{school_address}}</strong>
</div>
<p style="margin: 0 0 16px 0;">We look forward to meeting you and your child on the revised date.</p>
<div style="margin: 18px 0;">
  <a href="{{school_url}}" target="_blank" style="display: inline-block; padding: 10px 22px; background-color: #11a14a; color: #ffffff; text-decoration: none; border-radius: 4px; font-weight: bold; font-size: 13px;">Candidate Portal &rarr;</a>
</div>"""
    },
    {
        "filename": "15_one_to_one_meeting_offline_scheduled.html",
        "alert_name": "One-to-One Meeting (Offline/In-person) Scheduled",
        "subject": "In-Person Interaction Scheduled - {{school_name}}",
        "headline": "In-Person Interaction Confirmed",
        "greeting": "Dear Parents,",
        "body": """<p style="margin: 0 0 16px 0;">An in-person one-to-one interaction session has been confirmed for <strong>{{student_name}}</strong> (Application No: <strong>{{application_no}}</strong>) for Class <strong>{{student_class}}</strong>.</p>
<div style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 14px 18px; margin: 16px 0; font-size: 13px; line-height: 1.6;">
  <strong>Interaction Details:</strong><br/>
  &bull; Date: <strong>{{meeting_date}}</strong><br/>
  &bull; Time: <strong>{{meeting_time}}</strong><br/>
  &bull; Counselor: <strong>{{counsler_name}}</strong><br/>
  &bull; Venue: <strong>{{school_address}}</strong>
</div>
<p style="margin: 0 0 16px 0;">Kindly bring previous academic records and arrive 10 minutes prior to the scheduled time.</p>
<div style="margin: 18px 0;">
  <a href="{{school_url}}" target="_blank" style="display: inline-block; padding: 10px 22px; background-color: #11a14a; color: #ffffff; text-decoration: none; border-radius: 4px; font-weight: bold; font-size: 13px;">Candidate Portal &rarr;</a>
</div>"""
    },
    {
        "filename": "16_one_to_one_meeting_online_scheduled.html",
        "alert_name": "One-to-One Meeting (Online/In-person) Scheduled",
        "subject": "Online Interaction Scheduled - {{school_name}}",
        "headline": "Online Interaction Confirmed",
        "greeting": "Dear Parents,",
        "body": """<p style="margin: 0 0 16px 0;">An online one-to-one interaction for <strong>{{student_name}}</strong> (Class: <strong>{{student_class}}</strong>) has been scheduled.</p>
<div style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 14px 18px; margin: 16px 0; font-size: 13px; line-height: 1.6;">
  <strong>Meeting Details:</strong><br/>
  &bull; Date: <strong>{{meeting_date}}</strong><br/>
  &bull; Time: <strong>{{meeting_time}}</strong><br/>
  &bull; Counselor: <strong>{{counsler_name}}</strong><br/>
  &bull; Video Link: <a href="{{meeting_url}}" target="_blank" style="color: #11a14a; font-weight: bold;">{{meeting_url}}</a>
</div>
<p style="margin: 0 0 16px 0;">Please ensure a stable connection and join 5 minutes before the scheduled time.</p>
<div style="margin: 18px 0;">
  <a href="{{meeting_url}}" target="_blank" style="display: inline-block; padding: 10px 22px; background-color: #11a14a; color: #ffffff; text-decoration: none; border-radius: 4px; font-weight: bold; font-size: 13px;">Join Online Meeting &rarr;</a>
</div>"""
    },
    {
        "filename": "17_meeting_reminder_to_candidate.html",
        "alert_name": "Meeting Reminder to Candidate",
        "subject": "Reminder: Interaction Scheduled - {{school_name}}",
        "headline": "Admission Interaction Reminder",
        "greeting": "Dear Parents,",
        "body": """<p style="margin: 0 0 16px 0;">This is a reminder for your upcoming one-to-one interaction for <strong>{{student_name}}</strong> (Application No: <strong>{{application_no}}</strong>).</p>
<div style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 14px 18px; margin: 16px 0; font-size: 13px; line-height: 1.6;">
  <strong>Schedule:</strong><br/>
  &bull; Date: <strong>{{meeting_date}}</strong><br/>
  &bull; Time: <strong>{{meeting_time}}</strong><br/>
  &bull; Assigned Counselor: <strong>{{counsler_name}}</strong><br/>
  &bull; Link / Venue: <strong>{{meeting_url}}</strong>
</div>
<p style="margin: 0 0 16px 0;">Our academic team looks forward to meeting with you and {{student_name}}.</p>
<div style="margin: 18px 0;">
  <a href="{{school_url}}" target="_blank" style="display: inline-block; padding: 10px 22px; background-color: #11a14a; color: #ffffff; text-decoration: none; border-radius: 4px; font-weight: bold; font-size: 13px;">View Details &rarr;</a>
</div>"""
    },
    {
        "filename": "18_meeting_completed_to_candidate.html",
        "alert_name": "Meeting Completed to Candidate",
        "subject": "Interaction Completed - {{school_name}}",
        "headline": "Interaction Successfully Completed",
        "greeting": "Dear Parents,",
        "body": """<p style="margin: 0 0 16px 0;">Thank you for attending the interaction session for <strong>{{student_name}}</strong> (Application No: <strong>{{application_no}}</strong>) at <strong>{{school_name}}</strong>.</p>
<p style="margin: 0 0 16px 0;">Our admissions committee is reviewing the interaction assessment and application documents. Further updates regarding provisional admission will be communicated shortly.</p>
<p style="margin: 0 0 16px 0;">You can track real-time application status directly on your candidate portal.</p>
<div style="margin: 18px 0;">
  <a href="{{school_url}}" target="_blank" style="display: inline-block; padding: 10px 22px; background-color: #11a14a; color: #ffffff; text-decoration: none; border-radius: 4px; font-weight: bold; font-size: 13px;">Track Application &rarr;</a>
</div>"""
    },
    {
        "filename": "19_reschedule_meeting_alert_to_candidate.html",
        "alert_name": "Reschedule Meeting alert to Candidate",
        "subject": "Interaction Rescheduled - {{school_name}}",
        "headline": "Interaction Session Rescheduled",
        "greeting": "Dear Parents,",
        "body": """<p style="margin: 0 0 16px 0;">Your one-to-one admission interaction for <strong>{{student_name}}</strong> (Class: <strong>{{student_class}}</strong>) has been rescheduled.</p>
<div style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 14px 18px; margin: 16px 0; font-size: 13px; line-height: 1.6;">
  <strong>Revised Interaction Schedule:</strong><br/>
  &bull; New Date: <strong>{{meeting_date}}</strong><br/>
  &bull; New Time: <strong>{{meeting_time}}</strong><br/>
  &bull; Counselor: <strong>{{counsler_name}}</strong><br/>
  &bull; Link / Venue: <strong>{{meeting_url}}</strong>
</div>
<p style="margin: 0 0 16px 0;">Please review your updated schedule on your candidate portal.</p>
<div style="margin: 18px 0;">
  <a href="{{school_url}}" target="_blank" style="display: inline-block; padding: 10px 22px; background-color: #11a14a; color: #ffffff; text-decoration: none; border-radius: 4px; font-weight: bold; font-size: 13px;">Candidate Portal &rarr;</a>
</div>"""
    },
    {
        "filename": "20_adhoc_payment_alert_to_candidate.html",
        "alert_name": "Adhoc Payment Alert to Candidate",
        "subject": "Payment Notice: {{current_fee_receipt_head}} - {{school_name}}",
        "headline": "Fee Payment Notice",
        "greeting": "Dear Parents,",
        "body": """<p style="margin: 0 0 16px 0;">This communication is regarding the fee payment for <strong>{{student_name}}</strong> (Application No: <strong>{{application_no}}</strong>) for Class <strong>{{student_class}}</strong>.</p>
<div style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 14px 18px; margin: 16px 0; font-size: 13px; line-height: 1.6;">
  <strong>Payment Summary:</strong><br/>
  &bull; Fee Component: <strong>{{current_fee_receipt_head}}</strong><br/>
  &bull; Payable Amount: INR <strong>{{current_fee_receipt_amount}}</strong><br/>
  &bull; Issue Date: <strong>{{issueDate}}</strong>
</div>
<p style="margin: 0 0 16px 0;">Please complete the payment through the secure payment link below:</p>
<div style="margin: 18px 0;">
  <a href="{{payment_link}}" target="_blank" style="display: inline-block; padding: 10px 22px; background-color: #11a14a; color: #ffffff; text-decoration: none; border-radius: 4px; font-weight: bold; font-size: 13px;">Pay Fee Online &rarr;</a>
</div>"""
    },
    {
        "filename": "21_fee_receipt_download_url_alert_to_candidate.html",
        "alert_name": "Fee Receipt Download URL Alert to Candidate",
        "subject": "Fee Receipt Ready: {{current_fee_receipt_head}} - {{school_name}}",
        "headline": "Fee Receipt Available for Download",
        "greeting": "Dear Parents,",
        "body": """<p style="margin: 0 0 16px 0;">We gratefully acknowledge receipt of INR <strong>{{current_fee_receipt_paid_amount}}</strong> towards <strong>{{current_fee_receipt_head}}</strong> for <strong>{{student_name}}</strong> (Application No: <strong>{{application_no}}</strong>).</p>
<p style="margin: 0 0 16px 0;">Your official fee receipt is generated and ready for instant download.</p>
<div style="margin: 18px 0;">
  <a href="{{registration_fee_payment_fee_receipt_url}}" target="_blank" style="display: inline-block; padding: 10px 22px; background-color: #107c41; color: #ffffff; text-decoration: none; border-radius: 4px; font-weight: bold; font-size: 13px;">Download Fee Receipt (PDF) &rarr;</a>
</div>
<p style="margin: 0 0 16px 0;">You can also access your payment receipts and ledger on the candidate portal.</p>
<div style="margin: 18px 0;">
  <a href="{{school_url}}" target="_blank" style="display: inline-block; padding: 8px 18px; background-color: #475569; color: #ffffff; text-decoration: none; border-radius: 4px; font-size: 12px;">Candidate Portal &rarr;</a>
</div>"""
    },
    {
        "filename": "22_candidate_login.html",
        "alert_name": "Candidate Login",
        "subject": "Candidate Portal Credentials - {{school_name}}",
        "headline": "Welcome to Candidate Portal",
        "greeting": "Dear Parents,",
        "body": """<p style="margin: 0 0 16px 0;">Welcome to <strong>{{school_name}}</strong> Admission Portal for <strong>{{student_name}}</strong> (Class: <strong>{{student_class}}</strong>).</p>
<p style="margin: 0 0 16px 0;">Your candidate account is activated. Use the credentials below to log in and manage your application:</p>
<table width="100%" border="0" cellpadding="0" cellspacing="0" style="margin: 18px 0; background-color: #f8fafc; border: 1px solid #e2e8f0; border-left: 4px solid #11a14a; border-radius: 4px;">
  <tr>
    <td style="padding: 14px 18px; font-family: Arial, sans-serif; font-size: 13px; color: #333333; line-height: 1.6;">
      <div style="font-weight: bold; color: #1e293b; margin-bottom: 6px;">PORTAL CREDENTIALS</div>
      <div>Portal URL: <a href="{{school_url}}" target="_blank" style="color: #11a14a; font-weight: bold;">{{school_url}}</a></div>
      <div>Username: <span style="font-family: monospace; background-color: #e2e8f0; padding: 2px 6px; border-radius: 3px;">{{username}}</span></div>
      <div>Password: <span style="font-family: monospace; background-color: #e2e8f0; padding: 2px 6px; border-radius: 3px;">{{passwords}}</span></div>
    </td>
  </tr>
</table>
<div style="margin: 18px 0;">
  <a href="{{school_url}}" target="_blank" style="display: inline-block; padding: 10px 22px; background-color: #11a14a; color: #ffffff; text-decoration: none; border-radius: 4px; font-weight: bold; font-size: 13px;">Login to Portal &rarr;</a>
</div>"""
    }
]

def build_template_html(tmpl):
    return f"""<!--
================================================================================
EMAIL SUBJECT: {tmpl['subject']}
================================================================================
-->
<table width="100%" border="0" cellpadding="0" cellspacing="0" bgcolor="#f4f5f7" style="background-color: #f4f5f7; margin: 0; padding: 25px 0; font-family: Arial, Helvetica, sans-serif;">
  <tr>
    <td align="center" valign="top">
      <table width="600" border="0" cellpadding="0" cellspacing="0" bgcolor="#ffffff" style="width: 100%; max-width: 600px; background-color: #ffffff; border-radius: 6px; overflow: hidden; border: 1px solid #e2e8f0;">
        <!-- Top Accent Line -->
        <tr>
          <td height="4" bgcolor="{THEME_COLOR}" style="height: 4px; background-color: {THEME_COLOR}; font-size: 1px; line-height: 1px;">&nbsp;</td>
        </tr>
        <!-- Logo -->
        <tr>
          <td align="center" style="padding: 24px 20px 20px; background-color: #ffffff; border-bottom: 1px solid #eeeeee;">
            <a href="{{{{school_url}}}}" target="_blank" style="text-decoration: none;">
              <img src="{LOGO_URL}" alt="{{{{school_name}}}}" width="180" border="0" style="display: block; width: 180px; max-width: 100%; height: auto; margin: 0 auto; outline: none; border: none; text-decoration: none;" />
            </a>
          </td>
        </tr>
        <!-- Body Content -->
        <tr>
          <td align="left" style="padding: 30px 30px 24px; font-family: Arial, Helvetica, sans-serif; font-size: 14px; line-height: 1.65; color: #333333;">
            <p style="margin: 0 0 16px 0; font-size: 16px; font-weight: bold; color: {THEME_COLOR};">
              {tmpl['headline']}
            </p>
            <p style="margin: 0 0 16px 0; font-size: 14px; line-height: 1.6; color: #333333;">
              {tmpl['greeting']}
            </p>
{tmpl['body']}
            <p style="margin: 22px 0 0 0; font-size: 14px; line-height: 1.6; color: #333333;">
              Warm regards,<br />
              <strong>Team Admissions</strong><br />
              <span style="color: #64748b; font-size: 13px;">{{{{school_name}}}}</span>
            </p>
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
        <!-- Footer: ONLY social media links, google map link, and website link (CDN icons) -->
        <tr>
          <td align="center" style="padding: 20px 20px 22px; background-color: #fafafa;">
            <table border="0" cellpadding="0" cellspacing="0" align="center" style="margin: 0 auto;">
              <tr>
                <td align="center" style="padding: 0 10px;">
                  <a href="{{{{facebook_url}}}}" target="_blank" title="Facebook" style="display: inline-block; text-decoration: none;">
                    <img src="{ICON_FB}" alt="Facebook" width="28" height="28" border="0" style="display: block; width: 28px; height: 28px; border: 0; outline: none; text-decoration: none;" />
                  </a>
                </td>
                <td align="center" style="padding: 0 10px;">
                  <a href="{{{{instagram_url}}}}" target="_blank" title="Instagram" style="display: inline-block; text-decoration: none;">
                    <img src="{ICON_INSTA}" alt="Instagram" width="28" height="28" border="0" style="display: block; width: 28px; height: 28px; border: 0; outline: none; text-decoration: none;" />
                  </a>
                </td>
                <td align="center" style="padding: 0 10px;">
                  <a href="{{{{linkedin_url}}}}" target="_blank" title="LinkedIn" style="display: inline-block; text-decoration: none;">
                    <img src="{ICON_LI}" alt="LinkedIn" width="28" height="28" border="0" style="display: block; width: 28px; height: 28px; border: 0; outline: none; text-decoration: none;" />
                  </a>
                </td>
                <td align="center" style="padding: 0 10px;">
                  <a href="{{{{google_map_url}}}}" target="_blank" title="Google Map" style="display: inline-block; text-decoration: none;">
                    <img src="{ICON_MAP}" alt="Google Map" width="28" height="28" border="0" style="display: block; width: 28px; height: 28px; border: 0; outline: none; text-decoration: none;" />
                  </a>
                </td>
                <td align="center" style="padding: 0 10px;">
                  <a href="{{{{school_url}}}}" target="_blank" title="Website" style="display: inline-block; text-decoration: none;">
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

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Clear existing old files in Canonical Suite templates
    for f in os.listdir(OUTPUT_DIR):
        if f.endswith('.html') or f.endswith('.htm'):
            os.remove(os.path.join(OUTPUT_DIR, f))

    for tmpl in TEMPLATES_DATA:
        html = build_template_html(tmpl)
        filepath = os.path.join(OUTPUT_DIR, tmpl["filename"])
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Generated: {tmpl['filename']}")

    print(f"\nSuccessfully created {len(TEMPLATES_DATA)} sample templates in {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
