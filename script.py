import sys
import requests

print (sys.version)
print(sys.executable)


def greet(wie_te_groeten):
    greeting = "Hallo, {}".format(wie_te_groeten)
    return greeting


r = requests.get("https://b.stuivenberg@kpnmail.nl")
print(r.status_code)