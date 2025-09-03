install:
	uv sync

build:
	uv build

package-install:
	uv tool install dist/*.whl


package-reinstall: build
	uv tool install --force dist/*.whl


lint:
	uv run ruff check gendiff


fix:
	uv run ruff check gendiff --fix

coverage:
	uv run pytest --cov --cov-report xml

test:
	uv run pytest tests