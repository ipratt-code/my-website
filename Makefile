run: resolve_dependencies
	gunicorn --reload "main:app()"

resolve_dependencies: ./requirements.txt
	python3 -mpip install -r requirements.txt