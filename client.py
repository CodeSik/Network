#서건식_2016025469
#client

#모듈 import
import socket
import threading
import time

#서버의 주소와 포트
host = "127.0.0.1"
port = 8089

#소캣 생성
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

#메세지를 받는 함수
#한글도 지원(utf-8)
def recv(s):
    while 1:
        data = s.recv(1024)
        data = data.decode('utf-8')

        if not data:
            continue
        else:
            print(data)

#메세지를 보내는 함수
#한글도 지원(utf-8)
def send(s):
    while 1:
        data = input("")
        if not data:
            continue
        else:
            s.send(data.encode('utf-8'))

#id를 서버로 보내주고, 상대에게 보낼 때 메세지와 함께 출력
id = input("ID를 입력하세요:")
s.send(id.encode('utf-8'))

#쓰레드를 각각 실행하여 동시에 일어날 수 있도록 함
threading._start_new_thread(send,(s,))
threading._start_new_thread(recv,(s,))

#인터프리터 언어이기 때문에 쓰레드를 계속 실행시키기 위한 코
while 1:
    pass
