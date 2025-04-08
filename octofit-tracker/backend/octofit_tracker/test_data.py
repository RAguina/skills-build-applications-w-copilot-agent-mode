from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from mongoengine import connect
from pymongo import MongoClient

# Initialize MongoDB connection
connect(
    db="octofit_db",
    host="localhost",
    port=27017
)

def populate_test_data():
    # Clear the database
    client = MongoClient(host="localhost", port=27017)
    client.drop_database("octofit_db")

    # Create test users
    user1 = User(username="john_doe", email="john@example.com", password="password123").save()
    user2 = User(username="jane_doe", email="jane@example.com", password="password123").save()

    # Create test teams
    team1 = Team(name="Team Alpha", members=[user1, user2])
    team1.save()

    # Create test activities
    Activity(user=user1, activity_type="Running", duration="00:30:00").save()
    Activity(user=user2, activity_type="Cycling", duration="01:00:00").save()

    # Create test leaderboard entries
    Leaderboard(user=user1, score=100).save()
    Leaderboard(user=user2, score=150).save()

    # Create test workouts
    Workout(name="Morning Yoga", description="A relaxing morning yoga session.").save()
    Workout(name="HIIT", description="High-intensity interval training.").save()

    print("Test data populated successfully!")

if __name__ == "__main__":
    populate_test_data()