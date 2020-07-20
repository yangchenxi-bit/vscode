import socket
import time
import os
localtime = 1
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# hadoop start
os.system("start-dfs.sh")
time.sleep(10)

# 绑定端口:
s.bind(('192.168.65.100', 9999))

print('Bind UDP on 9999...')

while True:
    # wenjian
    filename = f"/opt/software/hadoop/mkdata/{localtime}.txt"
    # 接收数据:
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    print('客户端发送的数据为',data.decode())
    reply = '已经接收到数据, %s!' % data.decode('utf-8')
    s.sendto(reply.encode('utf-8'), addr)

    with open(filename,'a') as f:

        f.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        f.write('   ')
        f.write(data.decode()+'\n')
        f.close()

    if list(os.stat(f'/opt/software/hadoop/mkdata/{localtime}.txt'))[6] >2048:
        os.system(f"hadoop fs -put ./mkdata/{localtime}.txt /mkdata")
        os.system(f"hadoop jar /opt/software/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.8.5.jar wordcount /mkdata/{localtime}.txt /output/{localtime}_out.txt")
        localtime += 1