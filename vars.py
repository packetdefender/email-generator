import random

from password_generator import PasswordGenerator
import random as r

PWD = PasswordGenerator()
PWD.minlen = 32
PWD.maxlen = 32
PWD.minschars = 0
PWD.minuchars = 15
PWD.minlchars = 15
PWD.minnumbers = 15

grz1 = r.randint(100,999)
grz2 = r.randint(1001,9999)
grz3 = r.randint(1001,9999)
zoom_passcode = r.randint(10000, 99999)
zoom_id = f'{grz1} {grz2} {grz3}'
zoom_id_ns = zoom_id.replace(" ","")

ZOOM_URL = f"https://wrathcoinc.zoom.com/j/{zoom_id_ns}/pwd={PWD.generate()}"

ZOOM_FULL_BODY = f"""
Join Zoom Meeting
{ZOOM_URL}

Meeting ID:  {zoom_id}
Passcode: {zoom_passcode}

---

One tap mobile
+16465551212,,{zoom_id_ns}# US (New York)
+13017187845,,{zoom_id_ns}# US (Washington DC)

---

Dial by your location
 +1 646 555 1212 US (New York)
 +1 301 718 9874 US (Washington DC)
 +1 669 800 7845 US (San Jose)

Meeting ID:  {zoom_id}

Find your local number: https://wrathcoinc.zoom.us/u/kWZTs62yF
"""

AWS_OUTAGE = {
    "Issue with Accessing Database server in AWS": "Mike, \nWe lost all ability to connect to Database servers in AWS.  Example Source: nsx_vsw_host_001 to 10.5.22.96 on port 3306",
    "P1 - Can not connect To Production AWS Database Hosts": "Mike, \nI can not connect to MYSQL from nsx_vsw_host_001 to 10.5.22.96",
    "We need to get everyone on a bridge": "Mike, \nCan not connect to production database hosts in AWS!",
    "Major AWS issue": "Mike, \nWhat is going on with networking in AWS, we can not access hosts in the DB subnet, expect a P1 ticket and a bridge soon!",
    "We need you to join this Zoom call in process": f"""
Join Zoom Meeting
{ZOOM_URL}

Meeting ID:  {zoom_id}
Passcode: {zoom_passcode}

---

One tap mobile
+16465551212,,{zoom_id_ns}# US (New York)
+13017187845,,{zoom_id_ns}# US (Washington DC)

---

Dial by your location
 +1 646 555 1212 US (New York)
 +1 301 718 9874 US (Washington DC)
 +1 669 800 7845 US (San Jose)

Meeting ID:  {zoom_id}

Find your local number: https://wrathcoinc.zoom.us/u/kWZTs62yF
""",
    "Can you jump on this troubleshooting bridge": f"Mike,\n\n We need you to join this Zoom call in process: {ZOOM_URL}",
    "We need you on this troubleshooting bridge NOW": f"Mike,\n\n We need you to join this Zoom call in process: {ZOOM_URL}",
}

ZOOM_PREFIX = [
    "We need you to join this Zoom call in process",
    "Can you jump on this troubleshooting bridge",
    "We need you on this troubleshooting bridge NOW"
]

SECURITY = {
    # 'I think I am infected with Malware': "Mike, \nI got a email from helpdesk@wrathinc.co asking for my admin password"
    #                                       " so they can reset it, which I gave them.  I think I was hacked, can you "
    #                                       "check to see what my server 10.5.22.96 can access?",
    "We are being audited": "Mike, \nWe are in the middle of a audit and we need need that cloud security posture "
                            "ticket taken care of!",
    "CVE Lookup": "Mike,\nDo any of our devices have any config-based vulnerabilities?  I need to know with 100% "
                  "certainty and need it in 5 mins.",

}

WEB_VIP = {
    "Several tickets created for web_app_PUB_VIP": "Please investigate why TCP/22 is open to the internet and remediate ASAP.",
    "Security Alert for 'web_app_PUB_VIP'": "A non-standard port is open for web_app_PUB_VIP, please investigate why.",
}



random_int = random.randint(0, len(ZOOM_PREFIX)-1)
SUBJECT = f"Zoom troubleshooting bridge - AWS Outage / Troubleshooting"
BODY = f"Mike,\n\n We need you to join this Zoom call in process: {ZOOM_URL}"
SMTP_SERVER = 'smtp.dreamhost.com'
SMTP_PORT = 465
MY_EMAIL = 'mike@wrathcoinc.com'
MY_PASSWORD = ''
