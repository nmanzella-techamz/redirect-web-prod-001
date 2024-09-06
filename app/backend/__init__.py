import os
from fastapi import HTTPException
from fastapi.responses import RedirectResponse
import starlette.status as status
import requests

async def link_click_redirection(org: str):
    missing_env_var_msg = 'Expected environment variable on server is missing'
    ntfy_sh_topic = os.getenv("NTFY_SH_TOPIC")
    if not ntfy_sh_topic:
        raise HTTPException(status_code=500, detail=missing_env_var_msg)
    send_to_url = os.getenv("REDIRECT_URL")
    if not send_to_url:
        raise HTTPException(status_code=500, detail=missing_env_var_msg)
    topic = f"https://ntfy.sh/{ntfy_sh_topic}"
    message = f"Link Clicked by: {org}".encode(encoding='utf-8')
    requests.post(url=topic, data=message)
    return RedirectResponse(url=send_to_url, status_code=status.HTTP_302_FOUND)

async def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Redirects</title>
    </head>
    <body>

    <div class="container">
        For redirects and APIs...
    </div>

    </body>
    </html>
    """