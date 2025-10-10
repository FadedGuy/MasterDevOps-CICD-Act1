.PHONY: all $(MAKECMDGOALS)

# Argumentos por defecto: <archivo> <eliminar_duplicados> <orden>
ARGS ?= words.txt yes asc

run:
	docker run --rm \
		--volume "$$(pwd)":/opt/app \
		--env PYTHON_PATH=/opt/app \
		-w /opt/app \
		python:3.6-slim \
		python3 main.py $(ARGS)

run-local:
	python3 main.py $(ARGS)
