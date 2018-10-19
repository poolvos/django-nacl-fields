
from django.core.management.base import BaseCommand
from fields.backends import NaClWrapper


class Command(BaseCommand):
	help = 'Create a key for NaClWrapper.'

	def add_arguments(self, parser):
		parser.add_argument('-f', '--file', dest='filename',
			help='Path to settings.py. The key will be written to this file automatically.')

	def handle(self, *args, **options):
		key = NaClWrapper.createKey()
		output = 'NACL_FIELDS_KEY = \'%s\'' % key

		filename = options['filename']
		if filename:
			with open(filename, 'a') as file:
				file.write('%s\n' % output)
		else:
			print('# put the following line in your settings.py\n%s' % output)
