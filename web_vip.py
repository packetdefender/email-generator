import smtplib as s
import names as n
import random as r
import time
import vars

user_names = [n.get_full_name() for _ in range(1, 2 + 1)]


def send_generic_email(names):
    email_subject = list(vars.WEB_VIP.keys())
    email_body = list(vars.WEB_VIP.values())
    for name in names:
        time.sleep(300)
        with s.SMTP_SSL(vars.SMTP_SERVER, vars.SMTP_PORT) as c:
            c.login(vars.MY_EMAIL, vars.MY_PASSWORD)
            c.sendmail(from_addr='noreply@wrathcoinc.com',
                       to_addrs=vars.MY_EMAIL,
                       msg=f"From:{name}\n"
                           f"Subject: {email_subject[-1]}\n\n "
                           f"{email_body[-1]}")
            email_body.pop()
            email_subject.pop()
            time.sleep(1)
            print(f"---- Generated email for {name}, waiting to send next email ----")


send_generic_email(user_names)
