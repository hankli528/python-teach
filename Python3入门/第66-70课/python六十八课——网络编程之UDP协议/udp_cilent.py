#！/usr/bin/env python
# Author:Hank

import socket
'''
使用udp编写客户端的程序：
核心：得到socket对象
在创建对象的过程中，需要传入两个参数：
第一个参数：满足(匹配)ipv4的规则(socket.AF_INET)
第二个参数：判断到底是满足tcp协议编程(socket.SOCK_STREAM)还是udp协议编程(socket.SOCK_DGRAM)
面向无连接的编程
'''
#创建客户端的socket对象
udp_cilent_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#定义服务器的ip和端口号封装到元组对象中
udp_server=('10.11.63.132',66666)

#循环发送和接受数据
while 1:
    data=input('>>>: ')
    #客户端给服务器发送数据
    udp_cilent_socket.sendto(data.encode('utf-8'),udp_server)

    #接受服务器给客户端的数据
    recv_data=udp_cilent_socket.recvfrom(1024)

    #得到一个元组对象，我们需要的服务端发送过来的数据信息存储在此对象的第一个元素位上
    # print(recv_data)

    print('服务器说：'+recv_data[0].decode('gbk'))

    #关闭套接字对象
    udp_cilent_socket.close()