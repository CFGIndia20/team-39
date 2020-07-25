from app import db


class Users(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    fname = db.Column('First Name',db.String(50))
    lname = db.Column('Last Name',db.String(50))
    username = db.Column('Username',db.String(50))
    password = db.Column('Password',db.String(50))
    contactno = db.Column('Contact No',db.Integer)
    location = db.Column('Location',db.String(50))
    role = db.Column('Role',db.String(20))


class Units(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column('Unit Name',db.String(50))


class Patients(db.Model):
    id = db.Column('ID',db.Integer,primary_key= True)
    uuid = db.Column('Patient User ID',db.String(50))
    fname = db.Column('First Name',db.String(50))
    lname = db.Column('Last Name',db.String(50))
    username = db.Column('Username',db.String(50))
    password = db.Column('Password',db.String(50))
    contactno = db.Column('Contact No',db.Integer)
    location = db.Column('Location',db.String(50))
