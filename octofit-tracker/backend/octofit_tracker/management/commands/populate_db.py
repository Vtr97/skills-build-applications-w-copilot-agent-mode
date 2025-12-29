from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Workout, LeaderboardEntry

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        # Clear data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        LeaderboardEntry.objects.all().delete()
        Workout.objects.all().delete()

        # Users
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password')
        cap = User.objects.create_user(username='captainamerica', email='cap@marvel.com', password='password')
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='password')
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='password')

        # Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Activities (using correct field names from models.py)
        from datetime import date
        Activity.objects.create(user=ironman, activity_type='Running', duration=30, calories_burned=300, date=date.today())
        Activity.objects.create(user=cap, activity_type='Cycling', duration=45, calories_burned=450, date=date.today())
        Activity.objects.create(user=batman, activity_type='Swimming', duration=60, calories_burned=600, date=date.today())
        Activity.objects.create(user=superman, activity_type='Yoga', duration=20, calories_burned=200, date=date.today())

        # Leaderboard
        LeaderboardEntry.objects.create(user=ironman, score=100, rank=2)
        LeaderboardEntry.objects.create(user=cap, score=90, rank=4)
        LeaderboardEntry.objects.create(user=batman, score=95, rank=3)
        LeaderboardEntry.objects.create(user=superman, score=110, rank=1)

        # Workouts
        Workout.objects.create(name='Super Strength', description='Strength workout for heroes', suggested_for='Marvel')
        Workout.objects.create(name='Stealth Moves', description='Agility workout for heroes', suggested_for='DC')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
