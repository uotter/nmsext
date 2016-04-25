from werkzeug.security import generate_password_hash, check_password_hash
from app import db


class User(db.Model):
    __tablename__ = 'nsmusers'
    uid = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True)
    username = db.Column(db.String(120), unique=True)
    passwdhash = db.Column(db.String(54))

    def __init__(self,firstname,lastname,email,password,username):
        self.firstname = firstname.title()
        self.lastname = lastname.title()
        self.email = email.title()
        self.set_password(password)
        self.username = username.title()

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(str(self.uid))

    def set_password(self, password):
        self.passwdhash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.passwdhash, password)
