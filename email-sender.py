from email.message import EmailMessage
import ssl
import smtplib
email_sender = "bluesara24@gmail.com"
email_pass = "guzkuipesemljvbj"
email_receiver = ""

subject = "heyyy"
body = """
    Yo what up it yo girl, Sara.\nI just happened to write this lil bit of python code to tell you how much I appreciate you! You have always been super supportive of me and have brightened up each and every one of my days. :D I can't believe I get to lay my eyes upon such a beautiful person and call them mine. I love you so much and am looking forward to the next time we meet.\nYour Lover,\n Sara <3
"""
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)
context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_pass)
    smtp.sendmail(email_sender, email_receiver, em.as_string())