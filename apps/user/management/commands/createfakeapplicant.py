from django.core.management.base import BaseCommand, CommandError
from faker import Faker
import faker.providers
locale_list = ['en-US']

from apps.jobsearch.models import *
from apps.user.models import *

class Command(BaseCommand):
    help = "Creating fake 100 applicant to your database"
    def handle(self, *args, **kwargs):
        fake = Faker(locale_list)
        user = User.objects.all()
        randome_users = [fake.unique.random_element(user) for i in range(100)]
        for u in randome_users:
            edu_level = fake.word(ext_word_list=EDUCATIONAL_LEVEL_CHOICES)[0]
            applicant = Applicant.objects.create(
                user = u,
                education_level=edu_level,
            )
            applicant.user.user_type = "APPLICANT"
            
            applicant.save()