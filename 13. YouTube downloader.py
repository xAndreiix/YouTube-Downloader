import os
import yt_dlp

# Link YouTube
url = "https://www.youtube.com/watch?v=PaXXwyA9aYE&ab_channel=TOHOanimation%E3%83%81%E3%83%A3%E3%83%B3%E3%83%8D%E3%83%AB"

# Calea de descărcare
desktop_path = os.path.expanduser("~/Desktop")

# Opțiuni de descărcare
ydl_opts = {
    'format': 'best',
    'outtmpl': os.path.join(desktop_path, '%(title)s.%(ext)s'),
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(url, download=True)
    print(f"Titlu: {info['title']}")
    print("Descărcare finalizată.")
