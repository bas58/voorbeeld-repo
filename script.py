import requests

r = requests.get("https://b.stuivenberg@kpnmail.nl")
print(r.status_code)
print( r.ok)