# -*- coding: utf-8 -*-
from sockjs.tornado import SockJSConnection
from app.models.crud import CRUD
import json
import datetime

"""
1. establish connection
2. full-duplex communication
3. disconnect
"""

class ChatRoomHandler(SockJSConnection):
    # collection of clients
    waiters = set()


    # establish connection
    def on_open(self, request):
        try:
            self.waiters.add(self)
        except Exception as e:
            print(e)


    # full-duplex communication
    def on_message(self, message):
        # broadcast the message to all clients
        try:
            data = json.loads(message)
            data["dt"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            content = json.dumps(data)
            if data['code'] == 2:
                CRUD.save_msg(content)
            self.broadcast(self.waiters, content)
        except Exception as e:
            print(e)


    # disconnect
    def on_close(self):
        try:
            self.waiters.add(self)
        except Exception as e:
            print(e)