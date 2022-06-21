from django.core.management.base import BaseCommand, CommandError
from faker import Faker
import faker.providers
locale_list = ['en-US']

from apps.jobsearch.models import *
from apps.user.models import *

class Command(BaseCommand):
    help = "Creating fake 200 applicantions to your database"
    def handle(self, *args, **kwargs):
        fake = Faker(locale_list)
        applicants = Applicant.objects.filter(user__user_type="APPLICANT")
        jobs = Job.objects.all()
        for i in range(200):
            application = Application.objects.create(
                user = fake.random_element(applicants),
                job = fake.random_element(jobs),
                status = fake.random_element(["PENDING","DECLINED","INTERVIEW","HIRED"]),
                about_yourself=fake.paragraph(30),
                
            )
            application.save()