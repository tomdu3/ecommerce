# TESTING

## Excluding Selenium

```bash
pytest -m "not selenium"
```

## Dump data into json

- after adding category records into the database
- dump the data for the category model into a json file

```bash
./manage.py dumpdata inventory.category --indent 2 > ecommerce/inventory/fixtures/db_category_fixture.json
```
