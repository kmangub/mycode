import requests

while True:

    x = requests.get('http://0.0.0.0:2224/fast')
    print(x.text)
