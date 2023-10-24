import os
import requests
from dotenv import load_dotenv
import jinja2


load_dotenv()

DOMAIN = os.getenv("MAILGUN_DOMAIN")

template_loader = jinja2.FileSystemLoader("templates")
template_env = jinja2.Environment(loader=template_loader)


def render_template(template_filename, **context):
    return template_env(template_filename).render(**context)


def send_simple_message(to, subject, body, html):
    api_key = os.getenv("MAILGUN_DOMAIN")

    return requests.post(
        f"https://api.mailgun.net/V3/{DOMAIN}/messages",
        auth=("api", api_key),
        data={"from": f"Excited User <mailgun@{DOMAIN}>",
              "to": [to], subject: subject, "text": body}
    )


def send_user_registration_email(email, username):
    return send_simple_message(email, "Successfully signed up", f"Hi {username}! You have successfully signed up.", render_template("email/action.html", username=username))
