import socket
import random
import time
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data = ''
while True:



        # data = input("输入你想发送的数据：")
    data = ''
    for i in range (20):
        x = str(random.randint(0,1))
        data += x
    print(la)

    # data = str(random.randint(0,1))

    s.sendto(data.encode(), ('192.168.65.100', 9999))
    time.sleep(1)
        # 接收数据:
    print(s.recv(1024).decode('utf-8'))

    if data == "EXIT":
        break
        # 发送数据:




s.close()