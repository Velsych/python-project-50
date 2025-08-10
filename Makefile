install:
	uv sync

build:
	uv build

package-install:
	uv tool install dist/*.whl


package-reinstall: build
	uv tool install --force dist/*.whl


lint:
	uv run ruff check difference_calculator


fix:
	uv run ruff check difference_calculator --fix

coverage:
	uv run pytest --cov

test:
	uv run pytest test