# -*- coding: utf-8 -*-
from app.views.views_register import RegisterHandler as register

urls = [
    (r"/register", register)
]