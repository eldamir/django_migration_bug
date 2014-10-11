django_migration_bug
====================

illustrates an issue with data migrations when doing functional tests


the issue at a glance
---------------------

look at `functional_tests/test_site.py` and `reproduction/tests/test_model`.
They both have two tests that count the TestModel, expecting to find 4, since 4
is created in the data migration in
`reproduction/migrations/0002_data_migration.py`.

The output of the tests are

```
 $ python3 manage.py test
Creating test database for alias 'default'...
...F
======================================================================
FAIL: test_models_are_there (functional_tests.test_site.TestModelTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/ruben/Dropbox/workspace/kwasi/migration_bug_repro/functional_tests/test_site.py", line 14, in test_models_are_there
    self.assertEqual(TestModel.objects.count(), 4)
AssertionError: 0 != 4

----------------------------------------------------------------------
Ran 4 tests in 0.507s

FAILED (failures=1)
Destroying test database for alias 'default'...
```

So the unittest finds all 4 TestModels each time, but the functional test wipes
the database clean after the first test is run
