from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from django.db.models import Q
import faker.providers
locale_list = ['en-US']

from apps.jobsearch.models import *
from apps.user.models import *

class Command(BaseCommand):
    help = "Creating fake 5 employer to your database"
    def handle(self, *args, **kwargs):
        fake = Faker(locale_list)
        user = User.objects.all()[:5]
        for u in user:
            employer = Employer.objects.create(
                user = u,
                approved=fake.random_element([True,False]),
            )
            
            u.user_type = "EMPLOYEE"
            u.save()
            employer.save()