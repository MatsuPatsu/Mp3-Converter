import webview
import subprocess
import os
import sys

class API:
    def download(self, url):
        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
        command = [
            'yt-dlp',
            '-x',
            '--audio-format', 'mp3',
            '--audio-quality', '0',
            '--embed-thumbnail',
            '--add-metadata',
            '-P', downloads_path,
            '-o', '%(title)s.%(ext)s',
            url
        ]
        try:
            subprocess.run(command, check=True)
            return f"✅ Downloaded to: {downloads_path}"
        except Exception as e:
            return f"❌ Error: {e}"

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and PyInstaller .exe """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

if __name__ == '__main__':
    api = API()
    html_file_path = resource_path("UI.html")  # use helper
    webview.create_window("YouTube to MP3", url=f"file://{html_file_path}", js_api=api)
    webview.start()