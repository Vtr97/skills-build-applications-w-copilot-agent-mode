from django.test import TestCase
from .models import User, Team, Activity, Workout, LeaderboardEntry

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(username='testuser', email='test@example.com')
        self.assertEqual(user.username, 'testuser')

class TeamModelTest(TestCase):
    def test_create_team(self):
        user = User.objects.create(username='member', email='member@example.com')
        team = Team.objects.create(name='Test Team')
        team.members.add(user)
        self.assertEqual(team.name, 'Test Team')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(username='activityuser', email='activity@example.com')
        activity = Activity.objects.create(user=user, activity_type='Running', duration=30, calories_burned=300, date='2025-01-01')
        self.assertEqual(activity.activity_type, 'Running')

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Push Ups', description='Do 20 push ups', suggested_for='Strength')
        self.assertEqual(workout.name, 'Push Ups')

class LeaderboardEntryModelTest(TestCase):
    def test_create_leaderboard_entry(self):
        user = User.objects.create(username='leader', email='leader@example.com')
        entry = LeaderboardEntry.objects.create(user=user, score=100, rank=1)
        self.assertEqual(entry.rank, 1)
