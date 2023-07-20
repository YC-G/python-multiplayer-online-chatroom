# -*- coding: utf-8 -*-
import datetime
from app.tools.orm import ORM
from app.models.models import User, Msg
from werkzeug.security import generate_password_hash


def dt():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class CRUD(object):
    @staticmethod
    # Certify uniqueness of user name, phone, and email
    def user_unique(data, method=1):
        session = ORM.db()
        user = None
        try:
            #crud
            model = session.query(User)
            if method == 1:
                user = model.filter_by(name=data).first()
            if method == 2:
                user = model.filter_by(email=data).first()
            if method == 3:
                user = model.filter_by(phone=data).first()
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()

        if user:
            return True
        else:
            return False


    # Save registered users
    @staticmethod
    def save_register_user(form):
        session = ORM.db()
        try:
            user = User(
                name=form.data['name'],
                pwd=generate_password_hash(form.data['pwd']),
                email=form.data['email'],
                phone=form.data['phone'],
                sex=None,
                zodiac=None,
                avatar=None,
                info=None,
                createdAt=dt(),
                updatedAt=dt()
            )
            session.add(user)
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return True


    @staticmethod
    def check_login(name, pwd):
        session = ORM.db()
        result = False
        try:
            user = session.query(User).filter_by(name=name).first()
            if user:
                if user.check_pwd(pwd):
                    result = True
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()

        return result


    # Get user by name
    @staticmethod
    def user(name):
        session = ORM.db()
        user = None
        try:
            user = session.query(User).filter_by(name=name).first()
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return user