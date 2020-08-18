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

#得到服务端的socket对象
tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#绑定服务端的ip和端口号(元祖)
tcp_server = ('10.11.63.132',8888)
tcp_server_socket.bind(tcp_server)

#开启监听
tcp_server_socket.listen()

#接受客户端的访问
new_socket,cilent_info = tcp_server_socket.accept()
# print(new_socket)
# print(cilent_info)

#循环接受和发送数据
while 1:
    #接受客户端发来的数据
    recv_date = new_socket.recv(1024)
    print('客户端：' + recv_date.decode('utf-8'))
    #给客户端发送数据
    data = input('>>>：')
    new_socket.send(data.encode('gbk'))
    #关闭两个套接字对象
    new_socket.close()
    tcp_server_socket.close()