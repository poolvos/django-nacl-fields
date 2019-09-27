# -*- coding: utf-8 -*-

from django.db import connection
from django.test import TestCase

from tests.models.testmodel import TestModel


class TestNoneFields(TestCase):
    def get_db_value(self, field, model_id):
        cursor = connection.cursor()
        cursor.execute(
            u'select {0} from tests_testmodel where id = {1};'.format(field, model_id)
        )
        return cursor.fetchone()[0]

    def test_char_field_encrypted_custom(self):
        plaintext = None

        model = TestModel()
        model.custom_crypto_char = plaintext
        model.save()

        ciphertext = self.get_db_value('custom_crypto_char', model.id)
        self.assertIsNone(ciphertext)

        fresh_model = TestModel.objects.get(id=model.id)
        self.assertEqual(fresh_model.custom_crypto_char, plaintext)

    def test_char_field_encrypted(self):
        plaintext = None

        model = TestModel()
        model.char = plaintext
        model.save()

        ciphertext = self.get_db_value('char', model.id)
        self.assertIsNone(ciphertext)

        fresh_model = TestModel.objects.get(id=model.id)
        self.assertEqual(fresh_model.char, plaintext)

    def test_unicode_encrypted(self):
        plaintext = None

        model = TestModel()
        model.char = plaintext
        model.save()

        ciphertext = self.get_db_value('char', model.id)
        self.assertIsNone(ciphertext)

        fresh_model = TestModel.objects.get(id=model.id)
        self.assertEqual(fresh_model.char, plaintext)

    def test_text_field_encrypted(self):
        plaintext = None

        model = TestModel()
        model.text = plaintext
        model.save()

        ciphertext = self.get_db_value('text', model.id)
        self.assertIsNone(ciphertext)

        fresh_model = TestModel.objects.get(id=model.id)
        self.assertEqual(fresh_model.text, plaintext)

    def test_datetime_field_encrypted(self):
        plaindate = None

        model = TestModel()
        model.datetime = plaindate
        model.save()

        ciphertext = self.get_db_value('datetime', model.id)
        self.assertIsNone(ciphertext)

        fresh_model = TestModel.objects.get(id=model.id)
        self.assertEqual(fresh_model.datetime, plaindate)

    def test_integer_field_encrypted(self):
        plainint = None

        model = TestModel()
        model.integer = plainint
        model.save()

        ciphertext = self.get_db_value('integer', model.id)

        self.assertIsNone(ciphertext)

        fresh_model = TestModel.objects.get(id=model.id)
        self.assertEqual(fresh_model.integer, plainint)

    def test_date_field_encrypted(self):
        plaindate = None

        model = TestModel()
        model.date = plaindate
        model.save()

        ciphertext = self.get_db_value('date', model.id)
        fresh_model = TestModel.objects.get(id=model.id)

        self.assertIsNone(ciphertext)
        self.assertEqual(fresh_model.date, plaindate)

    def test_float_field_encrypted(self):
        plainfloat = None

        model = TestModel()
        model.floating = plainfloat
        model.save()

        ciphertext = self.get_db_value('floating', model.id)
        self.assertIsNone(ciphertext)

        fresh_model = TestModel.objects.get(id=model.id)
        self.assertEqual(fresh_model.floating, plainfloat)

    def test_email_field_encrypted(self):
        plaintext = None

        model = TestModel()
        model.email = plaintext
        model.save()

        ciphertext = self.get_db_value('email', model.id)
        self.assertIsNone(ciphertext)

        fresh_model = TestModel.objects.get(id=model.id)
        self.assertEqual(fresh_model.email, plaintext)
