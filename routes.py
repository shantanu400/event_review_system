# routes.py


from app import app, db
from flask import request, jsonify
from models import User, Event, Review

@app.route('/api/reviews', methods=['POST'])
def submit_review():

    pass

@app.route('/api/reviews/<int:event_id>', methods=['GET'])
def get_reviews_for_event(event_id):
    
    pass

@app.route('/api/reviews/<int:review_id>/like', methods=['POST'])
def like_review(review_id):
  
    pass

@app.route('/api/reviews/<int:review_id>/report', methods=['POST'])
def report_review(review_id):
   
    pass

@app.route('/api/reviews/<int:review_id>/respond', methods=['POST'])
def respond_to_review(review_id):
    pass

@app.route('/api/events/<int:event_id>/summary', methods=['GET'])
def generate_event_summary(event_id):

    pass

@app.route('/api/reviews', methods=['GET'])
def get_reviews():
    
    pass
