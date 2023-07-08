# -*- coding: utf-8 -*-
from app.views.views_common import CommonHandler


class UserHandler(CommonHandler):
    # pre-url loading
    def prepare(self):
        if not self.name:
            self.redirect("/login/")