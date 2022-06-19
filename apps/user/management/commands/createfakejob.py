from random import random
from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from django.db.models import Q
from django.utils import timezone
import datetime
import faker.providers
locale_list = ['en-US']

from apps.jobsearch.models import *
from apps.user.models import *

class Command(BaseCommand):
    help = "Creating fake 5 employer to your database"
    def handle(self, *args, **kwargs):
        fake = Faker(locale_list)
        # user = User.objects.filter(~Q(user_type = "APPLICANT"))[:5]
        company = Company.objects.filter(status=True)
        num= [i for i in range(1,30)]
       
        for i in range(200):
            random_day = fake.random_element(num)
            start_date = timezone.now() - datetime.timedelta(days=random_day)
            end_date = timezone.now() + datetime.timedelta(days=random_day)
            category = fake.word(ext_word_list=JOB_CATEGORIES)[0]
            type = fake.word(ext_word_list=JOB_TYPE_CHOICES)[0]
            job = Job.objects.create (
                company = fake.random_element(company),
                start_date = start_date,
                end_date = end_date,
                title = fake.sentence(),
                description=fake.paragraph(30),
                category = category,
                salary = fake.random_int(3),
                type =type,
                region = fake.word(ext_word_list=REGION_CHOICES)[0],
                vacancy=fake.random_digit(),
                education_level = fake.word(ext_word_list=EDUCATIONAL_LEVEL_CHOICES)[0],
                requirement = fake.paragraph(20),
                experience=fake.paragraph(20),
                experience_year=fake.random_digit(),
                
            )
            job.save()