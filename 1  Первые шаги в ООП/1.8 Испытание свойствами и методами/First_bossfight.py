class Router:
    def __init__(self):
        self.buffer = []
        self.servers = {}

    def link(self, server):
        self.servers[server.ip] = server
        server.router = self

    def unlink(self, server):
        delete = self.servers.pop(server.ip, False)
        if delete:
            delete.router = None

    def send_data(self):
        for i in self.buffer:
            if i.ip in self.servers:
                self.servers[i.ip].buffer.append(i)
        self.buffer.clear()

class Server:
    n = 1
     
    def __init__(self):
        self.ip = Server.n
        Server.n += 1
        self.router = None
        self.buffer = []

    def send_data(self, data):
        if self.router:
            self.router.buffer.append(data)

    def get_data(self):
        b = self.buffer.copy()
        self.buffer.clear()
        return b
    
    def get_ip(self):
        return self.ip

class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip
