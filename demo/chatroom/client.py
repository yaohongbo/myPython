import socket
import select
import threading
import sys


def prompt():
    sys.stdout.write('<YOU> ')
    sys.stdout.flush()


def lis(sock):
    my = [sock]
    while True:
        r, w, e = select.select(my, [], [])
        if sock in r:
            try:
                data = sock.recv(1024)
                print data
                prompt()
            except socket.error:
                print 'socket is error'
                exit()


def talk(sock):
    while True:
        try:
            info = raw_input()
            sock.send(info)
            prompt()
        except:
            print 'cannot input'
            exit()


if __name__ == '__main__':
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 5000))
    print 'connect to the server success. you can send message....'
    prompt()
    t = threading.Thread(target=lis, args=(client_socket,))
    t.start()
    t1 = threading.Thread(target=talk, args=(client_socket,))
    t1.start()
