# Lesson 001

Examples of simple API autotests with Python and pytest. Builds for this test are available at https://travis-ci.com/victorkaplunov/QAA_training

How to install dependencies:
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```
How to run:
```
pytest -vv test_lesson_xx.py
```
Files description:
- test_lesson_01.py - basic test
-	test_lesson_01ddt.py - example of Data Driven Testing (DDT) paradigme
- test_lesson_01fuzzy.py - example of fuzzy testing and using JSON schema.

- country.csv - CSV file with country list for test_lesson_01ddt.py
- data.json - JSON file with data for DDT test for test_lesson_01ddt.py
- zone.csv - CSV file with list of time zones for test_lesson_01ddt.py
- json_schema.json - JSON schema for test_lesson_01fuzzy.py
