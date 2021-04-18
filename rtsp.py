import socket
import hashlib
from urllib.parse import urlparse


url = urlparse("rtsp://admin:admin@192.168.1.6:8554/live")
address = (url.hostname, url.port)

sock = socket.create_connection(address, timeout=1)

def rtsp_request(method: str, headers: dict) -> bytes:
    request = method + b" / " + b"RTSP/1.0"
    request += b"\r\n".join(bytes(f"{key}: {repr(headers[key])}") for key in headers)
    request += b"\r\n"
    return request
    # return "\r\n".join(request + headers + ["\r\n"]).encode()


r1 = rtsp_request(b"OPTIONS",
                  {"CSeq": 1,
                   "Require": "implicit-play",
                   "Proxy-Require": "gzipped-messages"
                   }
                  )

sock.send(r1)
response = sock.recv(4096)
if response:
    status = response.decode().split("\r\n")[0].split(' ')[1]
    print(response.decode())


r2 = rtsp_request(b"DESCRIBE", {"CSeq": 2})

sock.send(r2)
res = sock.recv(4096)
if res:
    print(res.decode())
