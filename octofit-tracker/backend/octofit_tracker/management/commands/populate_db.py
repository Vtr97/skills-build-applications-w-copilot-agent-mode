from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

# Define models for test data population (if not already defined in models.py)
# If models exist, import them instead of defining here.

# Example models for demonstration (replace with actual models if available)
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    user_email = models.EmailField()
    team = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    duration = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    team = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50)
    class Meta:
        app_label = 'octofit_tracker'

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='test123'),
            User.objects.create_user(username='captainamerica', email='cap@marvel.com', password='test123'),
            User.objects.create_user(username='batman', email='batman@dc.com', password='test123'),
            User.objects.create_user(username='superman', email='superman@dc.com', password='test123'),
        ]

        # Create activities
        Activity.objects.create(user_email='ironman@marvel.com', team='Marvel', type='Running', duration=30)
        Activity.objects.create(user_email='cap@marvel.com', team='Marvel', type='Cycling', duration=45)
        Activity.objects.create(user_email='batman@dc.com', team='DC', type='Swimming', duration=25)
        Activity.objects.create(user_email='superman@dc.com', team='DC', type='Flying', duration=60)

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=75)
        Leaderboard.objects.create(team='DC', points=85)

        # Create workouts
        Workout.objects.create(name='Push Ups', difficulty='Easy')
        Workout.objects.create(name='Pull Ups', difficulty='Medium')
        Workout.objects.create(name='Squats', difficulty='Easy')
        Workout.objects.create(name='Deadlift', difficulty='Hard')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
