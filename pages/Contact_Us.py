import streamlit
from send_email import send_mail

streamlit.header("Contact Me")

with streamlit.form(key="email_forms"):
    user_email = streamlit.text_input("Your email address")
    raw_message = streamlit.text_area("Your message")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message}
"""
    button = streamlit.form_submit_button("Submit")
    if button:
        send_mail(message)
        streamlit.info("Your email was sent succesfully")