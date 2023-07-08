# -*- coding: utf-8 -*-
from app.views.views_common import CommonHandler
from app.tools.forms import RegisterForm
from werkzeug.datastructures import MultiDict
from app.models.crud import CRUD

class RegisterHandler(CommonHandler):
    def get(self, *args, **kwargs):
        data = dict(
            title="register"
        )
        self.render("register.html", data=data)

    def post(self):
        # validate params passed by clients
        print("post")
        form = RegisterForm(MultiDict(self.params))
        res = dict(code=0)
        if form.validate():
            if CRUD.save_register_user(form):
                res["code"] = 1
        else:
            res = form.errors
            res["code"] = 0
        self.write(res)



