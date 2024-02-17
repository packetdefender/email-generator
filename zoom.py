from email import utils
import smtplib as s
import names as n
import time
import vars
import random

# user_name = [n.get_full_name() for _ in range(1, 1 + 1)]
# for name in user_name:
#     email = f'{name.replace(" ", ".")}@wrathcoinc.com'
#     print(name)
#     print(email)

def send_zoom_meeting():
    user_name = [n.get_full_name() for _ in range(1, 1 + 1)]
    for name in user_name:
        email = f'{name.replace(" ", ".")}@wrathcoinc.com'
        with s.SMTP_SSL(vars.SMTP_SERVER, vars.SMTP_PORT) as c:
            c.login(vars.MY_EMAIL, vars.MY_PASSWORD)
            c.sendmail(from_addr='noreply@wrathcoinc.com',
                       to_addrs=vars.MY_EMAIL,
                       msg=f"From:{utils.formataddr((name, email))}\n"
                           f"To:{utils.formataddr(('Mike Lossmann','mike@wrathcoinc.com'))}\n"
                           f"Subject: {vars.SUBJECT}\n\n "
                           f"{vars.BODY}")
            time.sleep(1)
            print(f"---- Generated email for {name}, waiting to send next email ----")


def send_aws_ts():
    user_name = [n.get_full_name() for _ in range(1, 1 + 1)]
    for name in user_name:
        email = f'{name.replace(" ", ".")}@wrathcoinc.com'
        email_subject, email_body = random.choice(list(vars.AWS_OUTAGE.items()))
        with s.SMTP_SSL(vars.SMTP_SERVER, vars.SMTP_PORT) as c:
            c.login(vars.MY_EMAIL, vars.MY_PASSWORD)
            c.sendmail(from_addr='noreply@wrathcoinc.com',
                       to_addrs=vars.MY_EMAIL,
                       msg=f"From:{utils.formataddr((name, email))}\n"
                           f"To:{utils.formataddr(('Mike Lossmann','mike@wrathcoinc.com'))}\n"
                           f"Subject: {email_subject}\n\n "
                           f"{email_body}")

            time.sleep(1)
            print(f"---- Generated email for {name}, waiting to send next email ----")



c = 1
while c < 10:
    print(c)
    if c % 2 == 0 or c % 3 == 0 or c % 4 == 0:
        send_zoom_meeting()
        c += 1
        time.sleep(1)
    elif c % 1 == 0:
        send_aws_ts()
        c += 1
        time.sleep(1)


# https://forwardnetworks.zoom.us/j/82763264025?pwd=0oVtxabN3CMWsGUqWTVsyObXfyRiE4.1