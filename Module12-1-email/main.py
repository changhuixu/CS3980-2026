import resend
import os
from dotenv import load_dotenv

load_dotenv()
resend.api_key = os.getenv("RESEND_API_KEY")

r = resend.Emails.send(
    {
        "from": "donotreply@resend.dev",
        "to": "cxu.uiowa@gmail.com",
        "subject": "Hello World",
        "html": "<p>Congrats on sending your <strong>first email</strong>!</p>",
    }
)
