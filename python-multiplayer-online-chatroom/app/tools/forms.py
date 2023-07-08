# -*- coding: utf-8 -*-
from wtforms import Form
from wtforms.fields import StringField, PasswordField, IntegerField
from wtforms.validators import DataRequired, Regexp, Email, EqualTo, ValidationError
from app.models.crud import CRUD


"""
sign-up form
name
password
confirm password
phone
email
"""

class RegisterForm(Form):
    name = StringField(
        "name",
        validators=[
            DataRequired(u"Name can't be empty.")
        ]
    )

    pwd = PasswordField(
        "password",
        validators=[
            DataRequired(u"Password can't be empty.")
        ]
    )

    conpwd = PasswordField(
        "confirm password",
        validators=[
            DataRequired(u"Confirmation password can't be empty."),
            EqualTo("pwd", message="Confirmation password doesn't match your password.")
        ]
    )

    phone = StringField(
        "phone",
        validators=[
            DataRequired(u"Phone number can't be empty."),
            Regexp("^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$", message="Wrong phone number format.")
        ]
    )

    email = StringField(
        "email",
        validators=[
            DataRequired(u"Email can't be empty."),
            Email("Wrong email format.")
        ]
    )


    def validate_name(self, field):
        data = CRUD.user_unique(field.data, 1)
        if data:
            raise ValidationError("Name already exists.")


    def validate_email(self, field):
        data = CRUD.user_unique(field.data, 2)
        if data:
            raise ValidationError("Email already exists.")


    def validate_phone(self, field):
        data = CRUD.user_unique(field.data, 3)
        if data:
            raise ValidationError("Phone number already exists.")


class LoginForm(Form):
    name = StringField(
        "name",
        validators=[
            DataRequired(u"Name can't be empty.")
        ]
    )

    pwd = PasswordField(
        "password",
        validators=[
            DataRequired(u"Password can't be empty.")
        ]
    )

    def validate_name(self, field):
        data = CRUD.user_unique(field.data)
        if not data:
            raise ValidationError("This account name doesn't exist.")

    def validate_pwd(self, field):
        if not CRUD.check_login(self.name.data, field.data):
            raise ValidationError("The password is incorrect.")


class UserEditForm(Form):
    id = IntegerField(
        "id",
        validators=[
            DataRequired(u"Id can't be empty.")
        ]
    )

    name = StringField(
        "name",
        validators=[
            DataRequired(u"Name can't be empty.")
        ]
    )

    phone = StringField(
        "phone",
        validators=[
            DataRequired(u"Phone number can't be empty."),
            Regexp("^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$", message="Wrong phone number format.")
        ]
    )

    email = StringField(
        "email",
        validators=[
            DataRequired(u"Email can't be empty."),
            Email("Wrong email format.")
        ]
    )

    avatar = StringField(
        "avatar",
        validators=[]
    )

    info = StringField(
        "signature",
        validators=[]
    )

    sex = IntegerField(
        "sex",
        validators=[]
    )

    zodiac = IntegerField(
        "zodiac",
        validators=[]
    )


