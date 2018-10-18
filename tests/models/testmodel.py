
from django.db import models

from fields.fields import (
	NaClBooleanField,
	NaClCharField,
	NaClDateField,
	NaClDateTimeField,
	NaClEmailField,
	NaClFloatField,
	NaClIntegerField,
	NaClTextField,
)

from tests.backends.testcryptowrapper import TestCryptoWrapper


class TestModel(models.Model):
	boolean = NaClBooleanField(default=False, blank=True)
	char = NaClCharField(max_length=255, null=True, blank=True)
	date = NaClDateField(null=True, blank=True)
	datetime = NaClDateTimeField(null=True, blank=True)
	email = NaClEmailField(null=True, blank=True)
	floating = NaClFloatField(null=True, blank=True)
	integer = NaClIntegerField(null=True, blank=True)
	text = NaClTextField(null=True, blank=True)

	custom_crypto_char = NaClCharField(
		max_length=255, null=True, crypto_class=TestCryptoWrapper, blank=True)
