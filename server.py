#서건식_2016025469
#server

#모듈 import
import socket
import threading
import time

#서버의 주소와 포트
host = "127.0.0.1"
port = 8089

#소켓 생성
#user는 멀티쓰레드(1대다 클라이언트 접속)을 위한 배열
#접속한 클라이언트를 넣는다.
global user
user = []
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)

#서버 handle 함수
def chat(s):
    try:
        #채팅에 입장하면 입장 메세지를 출력
        id=s.recv(1024)
        message = "{} 님이 입장하였습니다.".format(id.decode('utf-8'))

        #자신을 제외한 user들에게 출력시킨다.
        for i in user:
            if s!=i:
                i.send(message.encode('utf-8'))

        #메세지를 받을때마다 자신을 제외한 클라이언트에게 메세지를 보낸다.
        while s:
            print(message)
            data=s.recv(1024)
            message = "{} : {}".format(id.decode('utf-8'),data.decode('utf-8'))
            for i in user:
                if s!=i:
                    i.send(message.encode('utf-8'))
    #접속을 종료했을 때
    except:
        user.remove(s)
        message = "{} 님이 퇴장하였습니다.".format(id.decode('utf-8'))
        print(message)
        if user:
            for i in user:
                i.send(message.encode('utf-8'))
        



#접속 대기
print("{} 에 접속 대기중입니다.".format(host))

#accept를 받을 때 마다 새로운 클라이언트 쓰레드를 생
while 1:
    connect_soc, addr = s.accept()
    user.append(connect_soc)
    threading._start_new_thread(chat,(connect_soc,))


