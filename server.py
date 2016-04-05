#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Serve a directory listing from the directory it is called from.
Usage:
    python{3} server.py
"""

import threading, socket
from http.server import HTTPServer, SimpleHTTPRequestHandler

server = None


def start_server():
    global server
    server_address = ('', 8000)
    handler_class = SimpleHTTPRequestHandler
    server = HTTPServer(server_address, handler_class)
    t = threading.Thread(target=server.serve_forever)
    t.daemon = True
    print("Starting server at http://localhost:8000/")
    t.start()


def stop_server():
    global server
    print("Closing server at http://localhost:8000/")
    server.server_close()


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


start_server()
ip_address = get_ip_address()
print("                   http://" + ip_address + ":8000/")
input("Press Enter to stop.\n>")
stop_server()






