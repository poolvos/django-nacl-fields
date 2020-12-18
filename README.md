# Django NaCl Encrypted Fields

![GitHub Actions: test](https://github.com/warpnet/django-nacl-fields/workflows/test/badge.svg)
![GitHub Actions: lint](https://github.com/warpnet/django-nacl-fields/workflows/lint/badge.svg)

This is a collection of Django Model Field classes that are encrypted using PyNaCl. This package is largely based on [django-encrypted-fields](https://github.com/defrex/django-encrypted-fields), which makes use of the outdated Keyczar library to encrypt fields. Besides that, it is inspired by [django-fernet-field](https://github.com/orcasgit/django-fernet-fields).


## About PyNaCl

[PyNaCl](https://github.com/pyca/pynacl) is a Python binding to [libsodium](https://github.com/jedisct1/libsodium), which is a fork of the [Networking and Cryptography library](https://nacl.cr.yp.to). These libraries have a stated goal of improving usability, security and speed.


## Getting Started

```sh
pip install django-nacl-fields
```

Create a key to be used for encryption:
```sh
$ python manage.py createkey
# put the following line in your settings.py:
NACL_FIELDS_KEY = b'p1Et2Rb@;^BYdo`ZRFi!Hc-MXu(^|bVqA-FGqffM'
```

In your `settings.py`:
```python
NACL_FIELDS_KEY = b'p1Et2Rb@;^BYdo`ZRFi!Hc-MXu(^|bVqA-FGqffM'
```

Then, in your `models.py`:
```python
from django.db import models
from nacl_encrypted_fields import NaClTextField


class MyModel(models.Model):
    text_field = NaClTextField()
```

Use the model as you would normally and the data will be stored encrypted in the database.

**Note:** Encrypted data cannot be used to query or sort. In SQL, these will all look like text fields with random text.

It is also possible to append the fields key to your settings file automatically upon creation, by using the `-f` flag:
```sh
python manage.py createkey -f settings.py
```

Where `settings.py` is the path to your settings file.


## Available Fields

Currently build-in and unit-tested fields.

- `NaClCharField`
- `NaClTextField`
- `NaClDateTimeField`
- `NaClIntegerField`
- `NaClFloatField`
- `NaClEmailField`
- `NaClBooleanField`


## Encrypt Your Own Fields

Making new fields can be done by using the provided `NaClFieldMixin`:
```python
from django.db import models
from nacl_encrypted_fields import NaClFieldMixin


class NaClIPAddressField(NaClFieldMixin, models.IPAddressField):
    pass
```

Please report any issues you encounter when trying this.

## References

- <https://github.com/defrex/django-encrypted-fields>
- <https://github.com/orcasgit/django-fernet-fields>
