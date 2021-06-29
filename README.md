# Algusic Algorithm

## Commands

+ Testing
  + `pipenv run python -m unittest discover` - Run testing suite
  + `pipenv run coverage run -m unittest discover` - Run testing suite with coverage
  + `pipenv run coverage report` - Output report of coverage
+ Tools
  + `pipenv run flake8 algorithm` - run Flake8 on the `algorithm` module
  + `pipenv run mypy --ignore-missing-imports algorithm` - run Mypy on the `algorithm` module
  + `pipenv run black algorithm` - run Black on the `algorithm` module
