# -*- coding: utf-8 -*-
from app.views.views_common import CommonHandler


class ChatHandler(CommonHandler):
    def get(self, *args, **kwargs):
        data = dict(
            title="chatroom"
        )
        self.render("chat.html", data=data)