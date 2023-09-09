# -*- coding: utf-8 -*-
import os
import datetime
import uuid

from app.views.views_common import CommonHandler

class UploadHandler(CommonHandler):
    def check_xsrf_cookie(self):
        return True

    def post(self, *args, **kwargs):
        files = self.request.files["img"]
        imgs = []

        # assign image saving directory
        upload_path = os.path.join(
            os.path.dirname(
                os.path.dirname(
                    __file__
                )
            ), "static/uploads"
        )

        # determine if the directory exists, create if not exists
        if not os.path.exists(upload_path):
            os.makedirs(upload_path)

        for f in files:
            # format: time + unique identifier + postfix
            prefix_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            prefix_identifier = uuid.uuid4().hex
            newname = prefix_time + prefix_identifier + os.path.splitext(f['filename'])[-1]
            with open(os.path.join(upload_path, newname), "wb") as upload:
                upload.write(f['body'])
            imgs.append(newname)

        res =dict(
            code=1,
            image=imgs[0]
        )
        self.write(res)