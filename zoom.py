from email import utils
import smtplib as s
import names as n
import time
import vars
import random


def send_aws_ts():
    num_emails = int(input("How many emails do you want to send: "))
    user_name = [n.get_full_name() for _ in range(1, num_emails + 1)]
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
                           f"{email_body} \n\n {name}")

            time.sleep(1)
            print(f"---- Generated email for {name}, waiting to send next email ----")


send_aws_ts()