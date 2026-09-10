import os
import json
import re 
import time
import random
import urllib.request
import urllib.error

API_KEY = os.getenv("GEMINI_API_KEY", "")
MODEL = os.getenv("GEMINI_MODEL","gemini-3.5-flash")

def generate_email_with_gemini(command):
  if not API_KEY:
    raise runtimeError("GEMINI_API_KEY is missing.")
  prompt = f"""
you are a professional Gmail email writing assistant.
Convert the user's voice command into a professioinal email.

Rules:
- Do not copy the command literally 
