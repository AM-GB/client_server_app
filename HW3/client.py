from socket import *
import time
from sys import argv
import json

ip = argv[1]
port = int(argv[2])

print(ip + ' ' + f'{port}')

jim = {
    "action": "presence",
    "time": time.time(),
    "type": "status",
    "user": {
        "account_name": "I'm",
        "status": "Yep, I am here!"
    }
}

s = socket(AF_INET, SOCK_STREAM)  # Создать сокет TCP
s.connect((ip, int(port)))   # Соединиться с сервером

request = json.dumps(jim)
s.send(request.encode('utf-8'))

response = s.recv(1024)
data = json.loads(response)
print(data)

s.close()
