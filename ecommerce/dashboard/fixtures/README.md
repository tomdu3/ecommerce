# Fixtures

In order to have a correct data in the database fixture, the password needs to be hashed.

1. run `./manage.py shell`
2. this is the code to hash the password:
```python
from django.contrib.auth.hashers import make_password
make_password('password')
# the output will be something like this: 'pbkdf2_sha256$870000$bLPMSU2YgZ4xe3w3kBJSU9$sti1OkNGjyCOJ2hdkqI4/mNdfPFI2bWdo47tOjfDlJU='
```
3. copy the hashed password and replace it in the db_admin_fixture.json