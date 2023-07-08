# -*- coding: utf-8 -*-
from app.views.views_user import UserHandler


class UserProfileHandler(UserHandler):
    def get(self, *args, **kwargs):
        data = dict(
            title="userprofile"
        )
        self.render("userprofile.html", data=data)