import random
import smtplib

# participant, participants e-mails and targets list, replace "Name 1, Name 2, ..." for the participant's names!
# target list should always be exactly the same as participants list!
participants = ["Name 1", "Name 2", "Name 3", "Name 4", "Name 5", "Name 6"]
participants_e_mail = ["E-Mail Name 1", "E-Mail Name 2", "E-Mail Name 3", "E-Mail Name 4",
                       "E-Mail Name 5", "E-Mail Name 6"]
targets = ["Name 1", "Name 2", "Name 3", "Name 4", "Name 5", "Name 6"]

# function for mailing, i chose gmail as provider, however, look up smtplib documentation for other providers
def sendmail(sender_mail, sender_pw, chosen_mail, target):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(sender_mail, sender_pw)
        subject = 'Your Secret Santa'
        body = "The receiver of your gift will be " + target
        message = f'Subject: {subject}\n\n{body}'

        smtp.sendmail(sender_mail, chosen_mail, message)
        print("E-mail for" + p_chosen + "sent!")

# chosing random participant and the chosen participants target
while len(participants) > 0:
    p_chosen = random.choice(participants)
    ps_target = random.choice(targets)
    while p_chosen == ps_target:
        ps_target = random.choice(targets)

# sending mail
    sendmail("Input sender mail here", "Input sender password here", participants_e_mail[participants.index(p_chosen)], ps_target)

# sorting out picked participants and it's target
    participants_e_mail.pop(participants.index(p_chosen))
    participants.pop(participants.index(p_chosen))
    targets.pop(targets.index(ps_target))
