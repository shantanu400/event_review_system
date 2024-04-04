# models.py

from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    # Add more user fields as needed

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    # Add more event fields as needed

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))
    registration_rating = db.Column(db.Integer)
    event_experience_rating = db.Column(db.Integer)
    breakfast_rating = db.Column(db.Integer)
    likes = db.Column(db.Integer, default=0)
    reports = db.Column(db.Integer, default=0)
    flagged = db.Column(db.Boolean, default=False)
    organizer_response = db.Column(db.String(512))
