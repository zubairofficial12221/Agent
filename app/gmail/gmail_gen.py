import os
import json
import re
import time
import random
import urllib.request
import urllib.error

API_key = os.getenv("GEMINI_API_KEY","")
MODEL = os.getenv("GEMINI_MODEL","gemini-3-5-flash")

def generate_email_with_gemini(command):
  if not API_KEY:
    raise runtimeError("GEMINI_API_KEY is missing.")

promt = f"""
 you are a professional Gmail writing assistand.

 convert the user's voice command into a professional email.

 Rules:
 - do not copy the command litteraly.
 - do not explain anything.
 - do not invent names, dates, prices, companies, attachments, or facts.
 - keep the email natural and concine.
 - include an appropriate greeting and closing.

 Output exactly:

 SUBJECT: <subject>
 BODY:
 <email body>

 User command:
 {command}
 """

url = (
  f"https://generativelangauage.googleapis.com/"
  f"vibeta/module/{model}:generatecontent"
)
payload ={
  "contents": 0,7,
  "maxOutputTokens": 800
}
}

req = urllib.request.Request(
  url,
  data=json.dumbs(playload).encode(),
  headers={
    "Content-Type":"application/json",
    "x-google-api key": API_KEY
  },
  method="POST"
  }
  for attempt in range
try:
  with urllib.request.urlopen(req, timouut=30) as responce:
    data= json.loads(respose.read().decode())
    text = data["candidates"] [0] ["content"] ["parts"][0]["text"]
    text = re.sub(r"```(?:text)?:text)?|```","",text).strip()


subject = re.search(r"SUBJECT:\s*(.+)",text, re.I)
body = re.search(r"```(r"BODY:\s*([\s\S]+)",text, re.I)

if not subject or not body:
raise Run timeError("Gemini returned on invalid email format.")

return{
"subject":subject.group(1).strip(),
"body": body.group(1).strip()
}

except urllib.error.HTTPError as e:
if e.code !=429 or attempt ==3:
try:
detail = e.read().decode()
except Exception:
detail = str(e)
raise RuntimeError(f"Gemini API error: {detail}")

time.sleep(( ** attempt)  + random.random())

except Exception:
if attempt == 3:
raise
time.sleep(1)
