from socket import *
import time
from sys import argv
import json

port = int(argv[1])
ip = ''
if len(argv) > 2:
    ip = argv[2]

print(f'{ip}' + ' ' + f'{port}')

jim = {
    "response": 0,
    "alert": 'Запрос прошел'
}

s = socket(AF_INET, SOCK_STREAM)  # Создает сокет TCP
s.bind((ip, port))                # Присваивает порт 8888
s.listen(5)                       # Переходит в режим ожидания запросов;
# Одновременно обслуживает не более
# 5 запросов.


while True:
    client, addr = s.accept()

    request = client.recv(1024)
    data = json.loads(request)
    print(data)

    if data['action'] == 'presence':
        jim['response'] = 'OK'

    response = json.dumps(jim)

    client.send(response.encode('utf-8'))
    client.close()
