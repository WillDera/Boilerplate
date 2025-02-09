import os
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Renames the Django project"

    def add_arguments(self, parser):
        parser.add_argument('new_project_name', type=str,
                            help="The New Django Project Name")

    def handle(self, *args, **options):
        new_project_name = options['new_project_name']

        # logic to rename the project

        files_to_rename = ['boilerplate/settings/base.py',
                           'boilerplate/wsgi.py', 'manage.py']
        folder_to_rename = 'boilerplate'

        for f in files_to_rename:
            with open(f, 'r') as file:
                filedata = file.read()

            filedata = filedata.replace('boilerplate', new_project_name)

            with open(f, 'w') as file:
                file.write(filedata)

        os.rename(folder_to_rename, new_project_name)

        self.stdout.write(self.style.SUCCESS(
            "Project has been renamed to %s" % new_project_name))
