make lint:
	poetry run flake8 brain_games

install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl	

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even
