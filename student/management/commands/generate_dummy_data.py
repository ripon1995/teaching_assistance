import random
from faker import Faker
from django.core.management.base import BaseCommand

from course.models import Course
from student.models import Student

class Command(BaseCommand):
    help = 'Generate dummy data for MyModel'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of dummy records to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        faker = Faker()
        course = Course.objects.filter(pk=1).first()
        for _ in range(total):
            # Generate fake data using Faker
            fake_data = {
                'name': faker.name(),
                'father_name': faker.name(),
                'mother_name': faker.name(),
                'institution': faker.name(),
                'start_date': faker.date(),
                'course': course,
                'contact_number': faker.unique.phone_number(),
                'father_contact_number': faker.unique.phone_number()
            }

            # Create an instance of MyModel with fake data
            Student.objects.create(**fake_data)

        self.stdout.write(self.style.SUCCESS(f'Successfully generated {total} dummy records for Student model'))
