from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    fname = db.Column('First Name',db.String(50))
    lname = db.Column('Last Name',db.String(50))
    username = db.Column('Username',db.String(50))
    password = db.Column('Password',db.String(50))
    contactno = db.Column('Contact No',db.Integer)
    location = db.Column('Location',db.String(50))
    role = db.Column('Role',db.String(20))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    deleted = db.Column('Deleted',db.Integer, default=0)

donations = db.Table('donations', db.Model.metadata,
                                      db.Column('id', db.Integer, primary_key=True),
                                      db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                                      db.Column('unit_id', db.Integer, db.ForeignKey('unit.id')),
                                      db.Column('amount', db.Float, primary_key=True),
                                      db.Column('created_at', db.DateTime, nullable=False, default=datetime.utcnow),
)



class Unit(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column('Unit Name',db.String(50))
    description = db.Column('Description', db.Text())
    user = db.relationship('user', secondary=donations, backref='unit')

centre_units = db.Table('centre_units', db.Model.metadata,
                                      db.Column('id', db.Integer, primary_key=True),
                                      db.Column('centre_id', db.Integer, db.ForeignKey('centre.id')),
                                      db.Column('unit_id', db.Integer, db.ForeignKey('unit.id'))
)


class Centre(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column('Centre Name',db.String(50))
    location = db.Column('Location',db.String(50))
    units = db.relationship('Units', secondary=centre_units, backref='centre')



class Patient(db.Model):
    uuid = db.Column('ID',db.Integer,primary_key= True)
    #uuid = db.Column('Patient User ID',db.Integer, unique=True)
    fname = db.Column('First Name',db.String(50))
    lname = db.Column('Last Name',db.String(50))
    contactno = db.Column('Contact No',db.Integer)
    location = db.Column('Location',db.String(50))
    unit = db.relationship('Unit', backref='patient', lazy=True)
    admitted_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    discharged_at = db.Column(db.DateTime, nullable=True)
    deleted = db.Column('Deleted',db.Integer, default=0)

class Category(db.Model):
    id = db.Column('ID',db.Integer,primary_key= True)
    name = db.Column('Category Name',db.String(50))


category_question = db.Table('category_question', db.Model.metadata,
                                      db.Column('id', db.Integer, primary_key=True),
                                      db.Column('centre_id', db.Integer, db.ForeignKey('centre.id')),
                                      db.Column('unit_id', db.Integer, db.ForeignKey('unit.id'))
)

class Question(db.Model):
    id = db.Column('ID',db.Integer,primary_key= True)
    question = db.Column('Question',db.String(50))
    category = db.relationship('Category', secondary=category_question, backref='question')

class Answer(db.Model):
    id = db.Column('ID',db.Integer,primary_key= True)
    answer = db.Column('Answer',db.Integer)
    category_question_id = db.relationship('Category Question ID', secondary=category_question, backref='category')
    uuid = db.Column(db.Integer, db.ForeignKey('patient.ID'), nullable=False)
    '''
        created_at to get monthly or yearly data
    '''
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

db.create_all()
