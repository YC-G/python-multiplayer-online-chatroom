# -*- coding: utf-8 -*-
from app.models.crud import CRUD
from app.views.views_common import CommonHandler
import json

class MSGHandler(CommonHandler):
    def check_xsrf_cookie(self):
        return True

    def post(self, *args, **kwargs):
        data = CRUD.latest_msg()
        result = []
        for v in data:
            result.append(json.loads(v.content))
        self.write(dict(data=result[::-1]))


