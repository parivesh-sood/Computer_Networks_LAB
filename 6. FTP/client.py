import socket
flag = True
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Sending connection request")
s.connect(("127.0.0.1", 12000))
print("Connection established")
msg = ""
while flag:
    my = input("\nEnter the name of file: ")
    s.send(bytes(my, "utf-8"))
    msg = s.recv(1024)

    if (msg.decode("utf-8") != "File is not there"):
        print("Content of the files: ", msg.decode("utf-8"))
        edit = input("Content to be append: ")
        s.send(bytes(edit, "utf-8"))
        print("Content added successfully")
    else:
        print("File is not there")
    flag = False
