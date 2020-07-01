import ast

from django.core.management.base import BaseCommand

from restaurants import repository


class Command(BaseCommand):
    help = 'Perform a generic query and print the result'

    sqlrepo = repository.RestaurantRepo()

    def add_arguments(self, parser):
        parser.add_argument('params', nargs='+', type=str)
        
        parser.add_argument(
            '--sql',
            action='store_true',
            help='Perform a generic query on the SQL database',
        )

        parser.add_argument(
            '--first',
            action='store_true',
            help='Return only the first result of the query',
        )


    def handle(self, *args, **options):
        result = "No options provided"
        params = ast.literal_eval(options["params"][0])
        
        if options["sql"]:
            if options["first"]:
                result = self.sqlrepo.query_restaurants_first(params=params)
            else:
                result = self.sqlrepo.query_restaurants(params=params)

        print(result)
