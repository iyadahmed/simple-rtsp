import socket
import hashlib
from urllib.parse import urlparse


url = urlparse("rtsp://admin:admin@192.168.1.6:8554/live")
address = (url.hostname, url.port)

def rtsp_request(method: str, headers: dict) -> bytes:
    request = [method + " / " + "RTSP/1.0"]
    headers = [f"{key}: {repr(headers[key])}" for key in headers]
    return "\r\n".join(request + headers + ["\r\n"]).encode()

    

lines = ["OPTIONS / RTSP/1.0",
         "CSeq: 1",
         #"Require: implicit-play",
         #"Proxy-Require: gzipped-messages",
         "\r\n"]
op_request = "\r\n".join(lines).encode()

r1 = rtsp_request("OPTIONS",
                   {"CSeq": 1,
                    "Require": implicit-play,
                    "Proxy-Require": gzipped-messages
                    }
                   )

sock = socket.create_connection(address, timeout=1)

sock.send(op_request)
response = sock.recv(4096)
if response:
    status = response.decode().split("\r\n")[0].split(' ')[1]
    print(response.decode())


lines = ["DESCRIBE / RTSP/1.0",
         "CSeq: 2",
         "\r\n"]

r = "\r\n".join(lines).encode()
sock.send(r)
res = sock.recv(4096)
if res:
    print(res.decode())
