# -*- coding: utf-8 -*-

from app import db

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120))
    message = db.Column(db.Text())
    date = db.Column(db.DateTime())

    def __repr__(self):
        return '<User {}>'.format(self.date)    
    
    