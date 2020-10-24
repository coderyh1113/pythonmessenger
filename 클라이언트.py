from socket import *
import threading
import time


def send(sock):
    while True:
        sendData = input('')
        sock.send(sendData.encode('utf-8'))


def receive(sock):
    while True:
        recvData = sock.recv(1024)
        print('상대방 :', recvData.decode('utf-8'))


port = int(input("포트를 설정하세요: "))
ip = input("서버에 보여지는 아이피를 바꿀 수 있습니다. 자신의 아이피를 무작위 번호로 정하세요: ") 

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect((ip , port))

print('접속 완료')

sender = threading.Thread(target=send, args=(clientSock,))
receiver = threading.Thread(target=receive, args=(clientSock,))

sender.start()
receiver.start()

while True:
    time.sleep(1)
    pass
