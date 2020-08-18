#！/usr/bin/env python
# Author:Hank
import socket
'''
实现tcp程序的客户端的编程
核心：得到socket对象
在创建对象的过程中，需要传入两个参数
第一个参数：满足的是ipv4的规则(socket.AF_INET)
第二个参数：判断/确定到底是满足tcp协议还是udp协议的规则编程(socket.SOCK_STREAM)
面向连接的编程：
'''
#得到客户端的socket对象
tcp_cilent_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#定义服务器的ip和端口号(封装到一个元组对象中)
tcp_server = ('10.11.63.132',8888)

#连接服务器
tcp_cilent_socket.connect(tcp_server)
#循环发送和接受数据
while 1:
    #客户端从键盘输入数据(字符串)
    data = input('>>>：')
    #将客户端的数据发送给服务器，我们在这个过程中需要对数据进行编码操作(有一定的安全性保障)
    tcp_cilent_socket.send(data.encode('utf-8'))
    #接受服务器给客户端传递(发送)过来的数据并且进行解码操作
    recv_data = tcp_cilent_socket.recv(1024)
    print('服务器：' + recv_data.decode('gbk'))
    #关闭套接字对象
    tcp_cilent_socket.close()
