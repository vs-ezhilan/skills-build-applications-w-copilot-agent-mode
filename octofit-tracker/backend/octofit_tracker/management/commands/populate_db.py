from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, User, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        # Skipping deletion due to Djongo ORM limitations

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = []
        user_data = [
            ('Iron Man', 'ironman@marvel.com', marvel),
            ('Captain America', 'cap@marvel.com', marvel),
            ('Spider-Man', 'spiderman@marvel.com', marvel),
            ('Batman', 'batman@dc.com', dc),
            ('Superman', 'superman@dc.com', dc),
            ('Wonder Woman', 'wonderwoman@dc.com', dc),
        ]
        for name, email, team in user_data:
            user = User(name=name, email=email, team=team)
            user.save()
            users.append(user)

        # Create workouts
        workouts = []
        workout_data = [
            ('Pushups', 'Upper body strength', 'Easy'),
            ('Running', 'Cardio endurance', 'Medium'),
            ('Deadlift', 'Full body strength', 'Hard'),
        ]
        for name, desc, diff in workout_data:
            workout = Workout(name=name, description=desc, difficulty=diff)
            workout.save()
            workouts.append(workout)

        # Create activities
        activity_data = [
            (users[0], 'Running', 30, 300, '2025-11-01'),
            (users[1], 'Pushups', 15, 100, '2025-11-02'),
            (users[3], 'Deadlift', 45, 400, '2025-11-03'),
        ]
        for user, typ, dur, cal, date in activity_data:
            activity = Activity(user=user, type=typ, duration=dur, calories=cal, date=date)
            activity.save()

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=500)
        Leaderboard.objects.create(team=dc, points=450)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
