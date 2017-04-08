import socket

# class Thread (threading.Thread):
#     def __init__(self, threadID, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name


def server_host():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostbyname(socket.gethostname())
    port = 9999
    client_dict = dict()
    print("Host Name: "+host)
    serversocket.bind((host,port))
    serversocket.listen(5)

    end = True
    while end:
        client, addr = serversocket.accept()
        print("Connection from %s" %str(addr))

        try:
            msg = client.recv(2048)
            msg = msg.decode("ascii")
            if msg == "quit":
                client.close()
            elif msg == "":
                pass
            elif addr[0] not in client_dict:
                client_dict[addr[0]] = msg
            else:
                client_dict[addr[0]] = msg
            # print(client_dict.values())
            # print(msg)
    
        except:
            client.close()
        for i in client_dict.keys().sort():
            print(i+":", client_dict[i])

server_host()