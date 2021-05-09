import socket


def readMyFile(fname):
    try:
        f = open(fname, 'r')
        str = ""
        for x in f:
            str += x
        f.close()
        return str
    except:
        return "File is not there"


def openSesame(fname):
    try:
        f = open(fname, 'r')
        str = ""
        for x in f:
            str += x
        f.close()
        return str
    except:
        return "File is not there"


def addContent(fname, content):
    f = open(fname, 'a')
    f.write(content)
    print("Content added successfully")
    f.close()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 12000))
s.listen(5)
while True:
    cs, add = s.accept()
    print(f"connection from {add} has been established")
    val = "n"

    while val != "y":
        msg = cs.recv(1024)
        fname = str(msg.decode("utf-8"))
        print("client requesting: " + msg.decode("utf-8"))

        val = readMyFile(fname)
        cs.send(bytes(val, "utf-8"))
        if (val != "FILE DOESNT EXIST ON SERVER"):
            msg = cs.recv(1024)
            content = str(msg.decode("utf-8"))
            addContent(fname, content)

        val = input("Would you like to check the file yes/no: ")

    openFile = input("Enter name of file: ")
    contents = openSesame(openFile)
    print("File contents: ", contents)
    exit()
