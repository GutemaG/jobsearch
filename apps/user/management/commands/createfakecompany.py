from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from django.db.models import Q
import faker.providers
locale_list = ['en-US']

from apps.jobsearch.models import *
from apps.user.models import *

class Command(BaseCommand):
    help = "Creating fake 5 company to your database"
    def handle(self, *args, **kwargs):
        fake = Faker(locale_list)
        user = Employer.objects.all()[:5]
        for u in user:
            region = fake.word(ext_word_list=REGION_CHOICES)[0]
            city = fake.word(ext_word_list=CITY_CHOICE)[0]
            company = Company.objects.create(
                employee = u,
                name=fake.company(),
                region = region,
                city = city,
                description =fake.paragraph(10),
                email=fake.email(),
                status=fake.random_element([True,False]),
            )
            company.save()