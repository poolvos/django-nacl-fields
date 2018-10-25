
from django.core.management.base import BaseCommand

import base64


class Command(BaseCommand):
    help = 'Convert a v1.x to a v2.x key for NaClWrapper.'

    def add_arguments(self, parser):
        parser.add_argument('-k', '--key', dest='key', help='v1.x key, base64 encoded', required=True)

    def handle(self, *args, **options):
        key = base64.b85encode(base64.b64decode(options['key']))
        output = 'NACL_FIELDS_KEY = %s' % key

        print('# replace the old line with the following line in your settings.py\n%s' % output)
