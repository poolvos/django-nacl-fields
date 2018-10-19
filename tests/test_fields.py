
import re

from django.db import connection
from django.test import TestCase
from django.utils import timezone

from tests.models.testmodel import TestModel


class TestFields(TestCase):
	def get_db_value(self, field, model_id):
		cursor = connection.cursor()
		cursor.execute(
			'select {0} from tests_testmodel where id = {1};'.format(field, model_id)
		)
		return cursor.fetchone()[0]

	def test_char_field_encrypted_custom(self):
		plaintext = 'Oh hi, test reader!'

		model = TestModel()
		model.custom_crypto_char = plaintext
		model.save()

		ciphertext = self.get_db_value('custom_crypto_char', model.id)

		self.assertNotEqual(plaintext, ciphertext)
		self.assertTrue('test' not in ciphertext)

		fresh_model = TestModel.objects.get(id=model.id)
		self.assertEqual(fresh_model.custom_crypto_char, plaintext)

	def test_char_field_encrypted(self):
		plaintext = 'Oh hi, test reader!'

		model = TestModel()
		model.char = plaintext
		model.save()

		ciphertext = self.get_db_value('char', model.id)

		self.assertNotEqual(plaintext, ciphertext)
		self.assertTrue('test' not in ciphertext)

		fresh_model = TestModel.objects.get(id=model.id)
		self.assertEqual(fresh_model.char, plaintext)

	def test_unicode_encrypted(self):
		plaintext = u'Oh hi, test reader! 🐱'

		model = TestModel()
		model.char = plaintext
		model.save()

		ciphertext = self.get_db_value('char', model.id)

		self.assertNotEqual(plaintext, ciphertext)
		self.assertTrue('test' not in ciphertext)

		fresh_model = TestModel.objects.get(id=model.id)
		self.assertEqual(fresh_model.char, plaintext)

	def test_text_field_encrypted(self):
		plaintext = 'Oh hi, test reader!' * 10

		model = TestModel()
		model.text = plaintext
		model.save()

		ciphertext = self.get_db_value('text', model.id)

		self.assertNotEqual(plaintext, ciphertext)
		self.assertTrue('test' not in ciphertext)

		fresh_model = TestModel.objects.get(id=model.id)
		self.assertEqual(fresh_model.text, plaintext)

	def test_datetime_field_encrypted(self):
		plaindate = timezone.now()

		model = TestModel()
		model.datetime = plaindate
		model.save()

		ciphertext = self.get_db_value('datetime', model.id)

		# Django's date serialization format
		self.assertTrue(re.search('^\d\d\d\d-\d\d-\d\d', ciphertext) is None)

		fresh_model = TestModel.objects.get(id=model.id)
		self.assertEqual(fresh_model.datetime, plaindate)

	def test_integer_field_encrypted(self):
		plainint = 42

		model = TestModel()
		model.integer = plainint
		model.save()

		ciphertext = self.get_db_value('integer', model.id)

		self.assertNotEqual(plainint, ciphertext)
		self.assertNotEqual(plainint, str(ciphertext))

		fresh_model = TestModel.objects.get(id=model.id)
		self.assertEqual(fresh_model.integer, plainint)

	def test_date_field_encrypted(self):
		plaindate = timezone.now().date()

		model = TestModel()
		model.date = plaindate
		model.save()

		ciphertext = self.get_db_value('date', model.id)
		fresh_model = TestModel.objects.get(id=model.id)

		self.assertNotEqual(ciphertext, plaindate.isoformat())
		self.assertEqual(fresh_model.date, plaindate)

	def test_float_field_encrypted(self):
		plainfloat = 42.44

		model = TestModel()
		model.floating = plainfloat
		model.save()

		ciphertext = self.get_db_value('floating', model.id)

		self.assertNotEqual(plainfloat, ciphertext)
		self.assertNotEqual(plainfloat, str(ciphertext))

		fresh_model = TestModel.objects.get(id=model.id)
		self.assertEqual(fresh_model.floating, plainfloat)

	def test_email_field_encrypted(self):
		plaintext = 'test@test.nl'

		model = TestModel()
		model.email = plaintext
		model.save()

		ciphertext = self.get_db_value('email', model.id)

		self.assertNotEqual(plaintext, ciphertext)
		self.assertTrue('test' not in ciphertext)

		fresh_model = TestModel.objects.get(id=model.id)
		self.assertEqual(fresh_model.email, plaintext)

	def test_boolean_field_encrypted(self):
		plainbool = True

		model = TestModel()
		model.boolean = plainbool
		model.save()

		ciphertext = self.get_db_value('boolean', model.id)

		self.assertNotEqual(plainbool, ciphertext)
		self.assertNotEqual(True, ciphertext)
		self.assertNotEqual('True', ciphertext)
		self.assertNotEqual('true', ciphertext)
		self.assertNotEqual('1', ciphertext)
		self.assertNotEqual(1, ciphertext)
		self.assertTrue(not isinstance(ciphertext, bool))

		fresh_model = TestModel.objects.get(id=model.id)
		self.assertEqual(fresh_model.boolean, plainbool)
