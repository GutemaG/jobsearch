from faker import Faker
locale_list = ['en-US']
fake = Faker(locale_list)
from .models import *

# user

# Applicant
users = User.objects.all()
gender = fake.word(ext_word_list=GENDER_CHOICES)[0]
phone = fake.phone_number()
region = fake.word(ext_word_list=REGION_CHOICES)
edu = fake.word(ext_word_list=EDUCATIONAL_LEVEL_CHOICES)

# Company
employee = User.objects.all()
name = fake.name()
# region
city = fake.word(ext_word_list=CITY_CHOICE)
description = fake.text()

# Job
company = Company.objects.all()