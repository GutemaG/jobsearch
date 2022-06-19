from django.core.management.base import BaseCommand, CommandError
from faker import Faker
import faker.providers
locale_list = ['en-US']

from apps.jobsearch.models import *
from apps.user.models import *

class Command(BaseCommand):
    help = "Creating fake 110 user to your database"
    def handle(self, *args, **kwargs):
        fake = Faker(locale_list)

        
        fake_user_names = [fake.unique.first_name() for i in range(110)]
        for username in fake_user_names:
            first_name = fake.first_name()
            last_name = fake.last_name()
            email = fake.email()
            gender = fake.word(ext_word_list=GENDER_CHOICES)[0]
            region = fake.word(ext_word_list=REGION_CHOICES)[0]
            phone = fake.phone_number()
            user_type = fake.word(ext_word_list=USER_TYPE_CHOICE)[0]
            u = User.objects.create(
            username = username,
            first_name=first_name,
            last_name = last_name,
            email = email,
            gender = gender,
            region = region,
            phone=phone,
            user_type = user_type
            )
            u.set_password("password")
            u.save()
        
        fake_user_names = [fake.unique.first_name() for i in range(100)]


"""
users = User.objects.all()
edu = fake.word(ext_word_list=EDUCATIONAL_LEVEL_CHOICES)

# Company
employee = User.objects.all()
name = fake.name()
# region
city = fake.word(ext_word_list=CITY_CHOICE)
description = fake.text()

# Job
company = Company.objects.all()

"""