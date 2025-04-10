import json
import os
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Load test data from JSON file
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        test_data_path = os.path.join(base_dir, 'test_data.json')
        with open(test_data_path, 'r') as file:
            data = json.load(file)

        # Connect to MongoDB
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Clear existing data by dropping collections
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Insert test data directly using pymongo, test data for users...
        db.users.insert_many([
            {"email": "john.doe@example.com", "name": "John Doe", "age": 30, "created_at": "2025-04-10T00:00:00Z"},
            {"email": "jane.smith@example.com", "name": "Jane Smith", "age": 25, "created_at": "2025-04-10T00:00:00Z"}
        ])

        db.teams.insert_one({
            "name": "Team Alpha",
            "members": ["john.doe@example.com", "jane.smith@example.com"],
            "created_at": "2025-04-10T00:00:00Z"
        })

        db.activity.insert_many([
            {"user": "john.doe@example.com", "activity_type": "Running", "duration": 30, "date": "2025-04-10"},
            {"user": "jane.smith@example.com", "activity_type": "Cycling", "duration": 45, "date": "2025-04-09"}
        ])

        db.leaderboard.insert_many([
            {"user": "john.doe@example.com", "score": 100},
            {"user": "jane.smith@example.com", "score": 150}
        ])

        db.workouts.insert_many([
            {"name": "Morning Yoga", "description": "A relaxing yoga session", "duration": 60},
            {"name": "HIIT", "description": "High-intensity interval training", "duration": 30}
        ])

        self.stdout.write(self.style.SUCCESS('Database populated with test data using pymongo'))
