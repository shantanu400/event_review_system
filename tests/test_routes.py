# tests/test_routes.py

import unittest
from app import app, db
from models import User, Event, Review

class TestRoutes(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.create_all()

        # Create test data
        user = User(username='test_user')
        event = Event(name='Test Event')
        db.session.add(user)
        db.session.add(event)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_submit_review(self):
        response = self.app.post('/api/reviews', json={
            'user_id': 1,
            'event_id': 1,
            'registration_rating': 4,
            'event_experience_rating': 5,
            'breakfast_rating': 3
        })
        data = response.json
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Review submitted successfully')

    def test_get_reviews_for_event(self):
        response = self.app.get('/api/reviews/1')
        data = response.json
        self.assertEqual(response.status_code, 200)
        self.assertTrue('reviews' in data)
        self.assertEqual(len(data['reviews']), 1)

    def test_like_review(self):
        response = self.app.post('/api/reviews/1/like')
        data = response.json
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Review liked successfully')

    def test_report_review(self):
        response = self.app.post('/api/reviews/1/report')
        data = response.json
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Review reported successfully')

    def test_respond_to_review(self):
        response = self.app.post('/api/reviews/1/respond', json={'organizer_response': 'Thank you for your feedback!'})
        data = response.json
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Response added successfully')

    def test_generate_event_summary(self):
        response = self.app.get('/api/events/1/summary')
        data = response.json
        self.assertEqual(response.status_code, 200)
        self.assertTrue('summary' in data)

    def test_get_reviews(self):
        response = self.app.get('/api/reviews')
        data = response.json
        self.assertEqual(response.status_code, 200)
        self.assertTrue('reviews' in data)

if __name__ == '__main__':
    unittest.main()
