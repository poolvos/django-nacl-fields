from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.db import models
from django.utils.encoding import force_bytes, force_text
from django.utils.functional import cached_property

from nacl_encrypted_fields.backends.naclwrapper import NaClWrapper


class NaClFieldMixin(object):
    """
    NaClFieldMixin will use PyNaCl to encrypt/decrypt data that is
    being put in/out of the database into application Django model fields. This
    package is largely based on the django-encrypted-fields package, which makes
    use of the outdated Keyczar library to encrypt fields.

    The only way to use this mixin is to set the NACL_FIELDS_KEY in settings.py
    to a base64 encoded key that matches the key size of the crypto_class used.
    The default crypto class - NaCl's SecretBox - takes a 32 byte key.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the NaClFieldMixin with the optional setting:
        * crypto_class: A custom class that is extended from CryptoWrapper.
        """
        crypto_class = kwargs.pop('crypto_class', NaClWrapper)

        key = settings.NACL_FIELDS_KEY
        if not key:
            raise ImproperlyConfigured(
                'You must set settings.NACL_FIELDS_KEY to use this library.'
            )

        self._crypto_box = crypto_class(key)

        super(NaClFieldMixin, self).__init__(*args, **kwargs)

    def get_internal_type(self):
        return 'BinaryField'

    def from_db_value(self, value, expression, connection, *args, **kwargs):
        if value is not None:
            value = bytes(value)
            if value != b'':
                value = self._crypto_box.decrypt(value)

            return super(NaClFieldMixin, self).to_python(force_text(value))

    def get_db_prep_save(self, value, connection):
        value = super(NaClFieldMixin, self).get_db_prep_save(value, connection)
        if value is not None:
            value = force_bytes(value)
            if value != b'':
                value = self._crypto_box.encrypt(value)

            return connection.Database.Binary(value)


class NaClBooleanField(NaClFieldMixin, models.BooleanField):
    pass


class NaClCharField(NaClFieldMixin, models.CharField):
    pass


class NaClDateTimeField(NaClFieldMixin, models.DateTimeField):
    pass


class NaClDateField(NaClFieldMixin, models.DateField):
    pass


class NaClEmailField(NaClFieldMixin, models.EmailField):
    pass


class NaClFloatField(NaClFieldMixin, models.FloatField):
    pass


class NaClIntegerField(NaClFieldMixin, models.IntegerField):
    @cached_property
    def validators(self):
        # Temporarily pretend to be an IntegerField to pass validation. Changing
        # `get_internal_type` on the fly to prevent fail in django>=1.7.
        self.get_internal_type = lambda: 'IntegerField'
        return models.IntegerField.validators.__get__(self)


class NaClTextField(NaClFieldMixin, models.TextField):
    pass
