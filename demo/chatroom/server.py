import socket
import select

def broadcastMsg(sock, message):
    for temp in CONNECTION_LIST:
        if temp != sock and temp != server_socket:
            try:
                temp.send(message)
            except:
                print 'xx'
                temp.close()
                CONNECTION_LIST.remove(temp)

port = 5000
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('0.0.0.0', port))
# begin TCP listen
server_socket.listen(10)
CONNECTION_LIST = []
# add server socket to list
CONNECTION_LIST.append(server_socket)
print 'chat server standing on port ', port
while True:
    read_sockets, write_sockets, error_sockets = select.select(CONNECTION_LIST, [], [])
    for sock in read_sockets:
        # new socket
        if sock == server_socket:
            new_socket, address = server_socket.accept()
            CONNECTION_LIST.append(new_socket)
            print 'connected by', address
            broadcastMsg(new_socket, "[%s:%s]has entered the room" %address)
        # incoming message from the client
        else:
            try:
                data = sock.recv(1024)
                if data:
                    broadcastMsg(sock, "\r" + '<' + str(sock.getpeername()) + '> ' + data)
            except:
                broadcastMsg(sock, "Client (%s:%s) is offline" % address)
                sock.close()
                CONNECTION_LIST.remove(sock)
                continue

print 'xxx'
server_socket.close()
