# -*- coding: utf-8 -*-
"""
Created on Sat May 10 12:46:34 2025

@author: marco
"""

import http.server
import datetime
import os

class CustomHandler(http.server.SimpleHTTPRequestHandler):

    def guess_type(self, path):
        if path.endswith(".html"):
            return "text/html"
        elif path.endswith(".css"):
            return "text/css"
        elif path.endswith(".jpg"):
            return "image/jpeg"
        elif path.endswith(".png"):
            return "image/png"
        else:
            return super().guess_type(path)

    def do_GET(self):
        if self.path == "/favicon.ico":
            self.send_response(204)  
            self.end_headers()
            return
        else:
            super().do_GET()
            self.log_message("GET %s - 200 OK", self.path)


    def log_message(self, format, *args):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  
        log_entry = f"[{timestamp}] {self.address_string()} - {format % args}\n"
        

        code_dir = os.path.dirname(os.path.abspath(__file__))
        log_path = os.path.join(code_dir, "server.log")  
        with open(log_path, "a+", encoding="utf-8") as log_file:
            log_file.write(log_entry)
            log_file.flush()