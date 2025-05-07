import os
import yt_dlp

# Link YouTube
url = # "Here insert your own URL"

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
