# user_name = [n.get_full_name() for _ in range(1, 1 + 1)]
# for name in user_name:
#     email = f'{name.replace(" ", ".")}@wrathcoinc.com'
#     print(name)
#     print(email)

# def send_zoom_meeting():
#     user_name = [n.get_full_name() for _ in range(1, 1 + 1)]
#     for name in user_name:
#         email = f'{name.replace(" ", ".")}@wrathcoinc.com'
#         with s.SMTP_SSL(vars.SMTP_SERVER, vars.SMTP_PORT) as c:
#             c.login(vars.MY_EMAIL, vars.MY_PASSWORD)
#             c.sendmail(from_addr='noreply@wrathcoinc.com',
#                        to_addrs=vars.MY_EMAIL,
#                        msg=f"From:{utils.formataddr((name, email))}\n"
#                            f"To:{utils.formataddr(('Mike Lossmann','mike@wrathcoinc.com'))}\n"
#                            f"Subject: {vars.SUBJECT}\n\n "
#                            f"{vars.BODY},\n\n {name}")
#             time.sleep(1)
#             print(f"---- Generated email for {name}, waiting to send next email ----")
#
# def send_zoom_full_meeting():
#     user_name = [n.get_full_name() for _ in range(1, 1 + 1)]
#     for name in user_name:
#         email = f'{name.replace(" ", ".")}@wrathcoinc.com'
#         with s.SMTP_SSL(vars.SMTP_SERVER, vars.SMTP_PORT) as c:
#             c.login(vars.MY_EMAIL, vars.MY_PASSWORD)
#             c.sendmail(from_addr='noreply@wrathcoinc.com',
#                        to_addrs=vars.MY_EMAIL,
#                        msg=f"From:{utils.formataddr((name, email))}\n"
#                            f"To:{utils.formataddr(('Mike Lossmann','mike@wrathcoinc.com'))}\n"
#                            f"Subject: Please join Zoom meeting in progress\n\n "
#                            f"{vars.ZOOM_FULL_BODY}")
#             time.sleep(1)
#             print(f"---- Generated email for {name}, waiting to send next email ----")
