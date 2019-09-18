import requests
import uuid

FILE = './codmw.jpg'
TARGET = 'http://localhost:8000'

name = str(uuid.uuid4())

files = [
    (name, (FILE, open(FILE, 'rb'), 'image/jpeg'))
]

resp = requests.post(TARGET, files=files)

print(str(resp.content, 'utf-8'))
