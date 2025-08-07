install:
	uv sync

build:
	uv build

package-install:
	uv tool install dist/*.whl


package-reinstall: build
	uv tool install --force dist/*.whl


lint:
	uv run ruff check brain_games


fix:
	uv run ruff check brain_games --fix