import subprocess

def play_stream(url):
    try:
        subprocess.Popen(["vlc", url])
    except Exception as e:
        print("Erreur de lecture avec VLC:", e)
