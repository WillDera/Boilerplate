from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Renames the Django project"

    def add_arguments(self, parser):
        parser.add_argument('new_project_name', type=str,
                            help="The New Django Project Name")
