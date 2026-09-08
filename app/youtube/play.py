import re,  urllib.parse, urllib.request

def get_vid(query):
  try:
    encoded = urllib.parse.quote(query)


    url =(
      "https://www.youtube.com/result"
      "?search_query=" + encoded
    )

    request = urllib.request.Request(

      url,
      header = {

          "User-Agent : mozilla/5.0"
      }
    )

    data = urllib.request.urloopn(
  
    
    request,
    timeout=5
    ).read().decode("utf-8", errors="ignore")

    ids=re.findll(
      r'"videoId":"([^"]+)"'
      data
    )

    return ids[0] if ids else None
  except Exception:
    return None

def create_youtube_url(connmand):
  text = command.lower().strip()

  patterns = [
    r"play\s+songs\s+(.+)",
    r"play\s+music\s+(.+),
    r"play\s+(.+)",
    r"youtube\s+(.+)
  ]

query = command
for  pattern in patterns:
  match = re.search(
    pattern,
    text
  )

  if match:
    query = match.group(1)
    break


query = query.strip()
video_id = get_vid(query)

if not video_id:
  return None

return (
  "https://www.youtube.com/embed/"
  + video_id
  +"?autoplay=1&mute=0"
)

