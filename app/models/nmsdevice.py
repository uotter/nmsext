from werkzeug.security import generate_password_hash, check_password_hash
from app import db


class Device(db.Model):
    __tablename__ = 'devices'
    iid = db.Column(db.BigInteger, primary_key = True)
    devicename = db.Column(db.String(100))
    deviceip = db.Column(db.String(100))
    devicebrand = db.Column(db.String(100))
    devicetype = db.Column(db.String(100))
    username = db.Column(db.String(100))
    passwdhash = db.Column(db.String(100))
    status = db.Column(db.String(100))
    note = db.Column(db.String(100))

    def __init__(self,devicename,deviceip,devicebrand,devicetype,username,password,status,note):
        self.firstname = devicename.title()
        self.lastname = deviceip.title()
        self.email = devicebrand.title()
        self.devicetype = devicetype.title()
        self.username = username.title()
        self.status = status.title()
        self.set_password(password)
        self.note = note.title()

    def get_id(self):
        return unicode(str(self.uid))

    def set_password(self, password):
        self.passwdhash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.passwdhash, password)
