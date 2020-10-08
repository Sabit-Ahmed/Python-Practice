import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

#Faker
import random
from AppTwo.models import user
from faker import Faker

fakegen = Faker()
"""topics = ['Search','Social','Marketplace','News','Games']

def add_topic():
    t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t"""

def populate(N=5):
    for entry in range(N):

        #top = add_topic()

        # create the fake data for that entry
        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()

        # create new entry
        usr = user.objects.get_or_create(first_name=fake_first_name,last_name=fake_last_name,email=fake_email)[0]

if __name__ == '__main__':
    print("Populating script!")
    populate(20)
    print("Populating complete!")
