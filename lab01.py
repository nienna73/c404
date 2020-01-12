import requests

req = requests.get("https://raw.githubusercontent.com/nienna73/c404/master/lab01.py")
print(req.text)
