#！/usr/bin/env python
# Author:Hank
import socket
'''
使用udp编写服务端的程序：
核心：得到socket对象
在创建对象的过程中，需要传入两个参数：
第一个参数：满足(匹配)ipv4的规则(socket.AF_INET)
第二个参数：判断到底是满足tcp协议编程(socket.SOCK_STREAM)还是udp协议编程(socket.SOCK_DGRAM)
面向无连接的编程
'''
#得到服务端的socket对象
udp_server_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#绑定服务器的ip和端口号
udp_server=('10.11.63.132',6666)
udp_server_socket.bind(udp_server)

#循环接受和发送数据
while 1:
    #接受客户端发送过来的数据，返回两个对象：1).数据内容 2).客户端的信息(元祖对象)
    recv_data,cilent_info=udp_server_socket.recvfrom(1024)
    print(recv_data)
    print(cilent_info)
    print('客户端说：' + recv_data.decode('utf-8'))

    #发送数据给客户端
    data=input('>>>: ')
    udp_server_socket.sendto(data.encode('gbk'),cilent_info)

    #关闭套接字对象
    udp_server_socket.close()
