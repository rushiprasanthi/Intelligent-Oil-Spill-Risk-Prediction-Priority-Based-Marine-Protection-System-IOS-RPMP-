import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

SENDER_EMAIL = "parvathambhavanarushi6@gmail.com"
SENDER_PASSWORD = "arufixtwygaepzee"


def send_spill_email(receiver_email, data):
    port = data["deployment"]["nearest_port"]["name"]
    distance = data["deployment"]["nearest_port"]["distance_km"]
    eta = data["deployment"]["eta_hours"]
    ships = data["deployment"]["ships_required"]

    subject = f"🚨 IMMEDIATE ACTION REQUIRED – Oil Spill Response ({port})"

    body = f"""
OFFICIAL OIL SPILL RESPONSE ALERT
IOS-RPMP – Intelligent Marine Emergency System
--------------------------------------------------

⚠️ PRIORITY LEVEL: {data['risk']['priority_label'].upper()}

This is an AUTOMATED EMERGENCY DIRECTIVE.
Immediate operational response is required.

--------------------------------------------------
📍 DEPLOYMENT INSTRUCTIONS (NEAREST PORT)
--------------------------------------------------
Designated Response Port : {port}
Distance to Spill Site   : {distance} km
Estimated Time of Arrival: {eta} hours
Response Vessels Needed : {ships}

➡ ACTION REQUIRED:
• Mobilize {ships} oil spill response vessels immediately
• Initiate containment boom deployment
• Prepare skimming & recovery equipment
• Coordinate with coastal authorities

--------------------------------------------------
🌊 SPILL & DAMAGE ASSESSMENT
--------------------------------------------------
Containment Direction : {data['simulation']['projected_direction_deg']}°
Ecosystem Impact      : {data['damage_control']['ecosystem_impact_percent']}%
Damage Controlled     : {data['damage_control']['damage_controlled_percent']}%
Economic Loss (Est.)  : ${data['economic_loss_musd']} Million
Fishery Area Affected : {data['damage_control']['fishery_area_sqkm']} sq km

--------------------------------------------------
🧠 SYSTEM ASSESSMENT
--------------------------------------------------
{data['risk']['explanation']['summary']}

--------------------------------------------------
⏱ RESPONSE TIME IS CRITICAL
Failure to act immediately may result in irreversible
environmental and economic damage.

This alert was generated automatically by IOS-RPMP.
DO NOT REPLY TO THIS EMAIL.

--------------------------------------------------
"""

    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = receiver_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    server.send_message(msg)
    server.quit()
