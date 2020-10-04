# -*- coding: utf-8 -*-

from django.db import connection
from django.test import TestCase

from tests.models.testmodel import TestModel


class TestBlankFields(TestCase):
    def get_db_value(self, field, model_id):
        cursor = connection.cursor()
        cursor.execute(
            u'select {0} from tests_testmodel where id = {1};'.format(
                field,
                model_id
            )
        )
        return cursor.fetchone()[0]

    def test_char_field_encrypted_custom(self):
        plaintext = ''

        model = TestModel()
        model.custom_crypto_char = plaintext
        model.save()

        ciphertext = self.get_db_value('custom_crypto_char', model.id)

        self.assertNotEqual(plaintext, ciphertext)
        self.assertTrue('test'.encode() not in ciphertext)

        fresh_model = TestModel.objects.get(id=model.id)
        self.assertEqual(fresh_model.custom_crypto_char, plaintext)

    def test_char_field_encrypted(self):
        plaintext = ''

        model = TestModel()
        model.char = plaintext
        model.save()

        ciphertext = self.get_db_value('char', model.id)

        self.assertNotEqual(plaintext, ciphertext)
        self.assertTrue('test'.encode() not in ciphertext)

        fresh_model = TestModel.objects.get(id=model.id)
        self.assertEqual(fresh_model.char, plaintext)

    def test_unicode_encrypted(self):
        plaintext = u''

        model = TestModel()
        model.char = plaintext
        model.save()

        ciphertext = self.get_db_value('char', model.id)

        self.assertNotEqual(plaintext, ciphertext)
        self.assertTrue('test'.encode() not in ciphertext)

        fresh_model = TestModel.objects.get(id=model.id)
        self.assertEqual(fresh_model.char, plaintext)

    def test_text_field_encrypted(self):
        plaintext = ''

        model = TestModel()
        model.text = plaintext
        model.save()

        ciphertext = self.get_db_value('text', model.id)

        self.assertNotEqual(plaintext, ciphertext)
        self.assertTrue('test'.encode() not in ciphertext)

        fresh_model = TestModel.objects.get(id=model.id)
        self.assertEqual(fresh_model.text, plaintext)

    def test_email_field_encrypted(self):
        plaintext = ''

        model = TestModel()
        model.email = plaintext
        model.save()

        ciphertext = self.get_db_value('email', model.id)

        self.assertNotEqual(plaintext, ciphertext)
        self.assertTrue('test'.encode() not in ciphertext)

        fresh_model = TestModel.objects.get(id=model.id)
        self.assertEqual(fresh_model.email, plaintext)
