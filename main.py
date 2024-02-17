import smtplib as s
import names as n
import random as r
import time
import vars

num_users = int(input("How many emails do you want to send: "))

user_names = [n.get_full_name() for _ in range(1, num_users + 1)]
it_names = [n.get_full_name() for _ in range(1, r.randint(2, 10))]

def send_generic_email(names):
    for i,name in enumerate(names):
        print(i, name)
        email_sub = r.choice(vars.IT_SUBJECTS)
        print(vars.IT_BODY['generic'])
        with s.SMTP_SSL(vars.SMTP_SERVER, vars.SMTP_PORT) as c:
            c.login(vars.MY_EMAIL, vars.MY_PASSWORD)
            c.sendmail(from_addr='noreply@wrathcoinc.com',
                       to_addrs=vars.MY_EMAIL,
                       msg=f"From:{name}\n"
                           f"Subject: {email_sub}\n\n "
                           f"{vars.IT_BODY['lunch'] if 'lunch' in email_sub else vars.IT_BODY['generic']}")

            time.sleep(1)
            print(f"---- Generated email for {name}, waiting to send next email ----")


def send_zoom_meeting(names):
    for name in names:
        with s.SMTP_SSL(vars.SMTP_SERVER, vars.SMTP_PORT) as c:
            c.login(vars.MY_EMAIL, vars.MY_PASSWORD)
            c.sendmail(from_addr='noreply@wrathcoinc.com',
                       to_addrs=vars.MY_EMAIL,
                       msg=f"From:{name}\n"
                           f"Subject: {vars.SUBJECT}\n\n "
                           f"{vars.BODY}")
            time.sleep(1)
            print(f"---- Generated email for {name}, waiting to send next email ----")


send_generic_email(user_names)
