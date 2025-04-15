import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_add="192.168.26.61" #reciver's
port=1234 #receiver's
complete = (ip_add,port)
message=input("hnji boliye")
encode_msg=message.encode('ascii')
s.sendto(encode_msg,complete)
s.close()