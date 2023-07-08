# -*- coding: utf-8 -*-
# Prevent CSRF attack by secret cookie (not viable based on the link below)
# https://www.freecodecamp.org/chinese/news/what-is-cross-site-request-forgery/
import os

root_path = os.path.dirname(__file__)
configs = dict(
    debug = True,
    template_path=os.path.join(root_path, "templates"),
    static_path=os.path.join(root_path, "static"),
    xsrf_cookies=True,
    # $ uuidgen
    cookie_secret="D1367935-8F59-40AC-BD8E-CBE91D98C5FC"
)

mysql_configs = dict(
    db_host="127.0.0.1",
    db_name="chatroom",
    db_port=3306,
    db_user="root",
    db_pwd="Gyc072503"
)

