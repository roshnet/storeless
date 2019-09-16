import requests

FILE = './payload.txt'
TARGET = 'http://localhost:8000'

files = [
    ('docfile', (FILE, open(FILE, 'rb'), 'application/octet'))
]

resp = requests.post(TARGET, files=files)

print(str(resp.content, 'utf-8'))
