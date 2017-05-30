from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_script import Manager
import os

basedir  = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
manager = Manager(app)

registrations = db.Table('registrations',
                         db.Column('student_id', db.Integer, db.ForeignKey('students.id')),
                         db.Column('class_id', db.Integer, db.ForeignKey('classes.id')))
class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    class_id = db.Column(db.Integer, db.ForeignKey('classes.id'))
    def __repr__(self):
        return '<Student: %r>' %self.name
class Class(db.Model):
    __tablename__ = 'classes'
    id = db.Column(db.Integer, primary_key=True)
    students = db.relationship('Student',secondary=registrations, backref=db.backref('_class', lazy="joined"), lazy="dynamic")
    name = db.Column(db.String(64))
    def __repr__(self):
        return '<Class: %r>' %self.name

if __name__ == '__main__':
    manager.run()