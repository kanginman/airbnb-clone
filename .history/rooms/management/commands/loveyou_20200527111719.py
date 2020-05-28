from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = "This command tells me that he loves me"

    def add_arguments(self, parser):
        parser.add_arguments(
            "--number",
            help="How many times do you want me to tell you that I love you?",
        )
