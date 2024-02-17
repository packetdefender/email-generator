import smtplib as s
import names as n
import time
import vars
import random

user_names = [n.get_full_name() for _ in range(1, 4 + 1)]


for i,name in enumerate(user_names):
    email_subject, email_body = random.choice(list(vars.AWS_OUTAGE.items()))
    with s.SMTP_SSL(vars.SMTP_SERVER, vars.SMTP_PORT) as c:
        c.login(vars.MY_EMAIL, vars.MY_PASSWORD)
        c.sendmail(from_addr='noreply@wrathcoinc.com',
                   to_addrs=vars.MY_EMAIL,
                   msg=f"From:{name}\n"
                       f"Subject: {email_subject}\n\n "
                       f"{email_body}")

        time.sleep(1)
        print(f"---- Generated email for {name}, waiting to send next email ----")
