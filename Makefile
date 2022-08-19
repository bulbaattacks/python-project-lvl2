install:
	poetry install


build:
	poetry build


publish:
	poetry publish --dry-run


package-install:
	python3 -m pip install --user dist/*.whl


gendiff:
	poetry run gendiff


lint:
	poetry run flake8 gendiff


test:
	poetry run pytest


package-reinstall:

	python3 -m pip install dist/*.whl --force-reinstall


test-coverage:
	 poetry run pytest --cov=gendiff tests/ --cov-report xml

