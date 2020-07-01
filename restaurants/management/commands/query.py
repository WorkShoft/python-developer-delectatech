import ast

from django.core.management.base import BaseCommand

from restaurants.repositories import sqlrepository, mongorepository


class Command(BaseCommand):
    help = 'Perform a generic query and print the result'

    sqlrepo = sqlrepository.SqlRestaurantRepo()
    mongorepo = mongorepository.MongoRestaurantRepo()

    def add_arguments(self, parser):
        parser.add_argument('params', nargs='+', type=str)
        
        parser.add_argument(
            '--mongo',
            action='store_true',
            help='Perform a generic query on the Mongo database',
        )

        parser.add_argument(
            '--first',
            action='store_true',
            help='Return only the first result of the query',
        )

        parser.add_argument(
            '--as_dict',
            action='store_true',
            help='Return results in dict format',
        )


    def handle(self, *args, **options):
        """
        Queries the MongoDB database when the --mongo option is passed,
        otherwise queries the SQL database
        """
        
        result = "No options provided"
        params = ast.literal_eval(options["params"][0])

        if options["mongo"]:
            if options["first"]:
                result = self.mongorepo.query_restaurants_first(params=params)
            else:
                result = self.mongorepo.query_restaurants(params=params)
            
        else:
            if options["first"]:
                result = self.sqlrepo.query_restaurants_first(params=params, as_dict=options["as_dict"])
            else:
                result = self.sqlrepo.query_restaurants(params=params, as_dict=options["as_dict"])

        print(result)
