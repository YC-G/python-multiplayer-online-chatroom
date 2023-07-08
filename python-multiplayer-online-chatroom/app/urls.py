# -*- coding: utf-8 -*-
from sockjs.tornado import SockJSRouter
from app.views.views_register import RegisterHandler as register
from app.views.views_chat import ChatHandler as chat
from app.views.views_login import LoginHandler as login
from app.views.views_userprofile import UserProfileHandler as userprofile
from app.views.views_chatroom import ChatRoomHandler as chatroom
from app.views.views_logout import LogoutHandler as logout


urls = [
    (r"/", chat),
    (r"/register/", register),
    (r"/login/", login),
    (r"/logout/", logout),
    (r"/userprofile/", userprofile)
] + SockJSRouter(chatroom, "/chatroom").urls
