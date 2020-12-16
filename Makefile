first_run: resolve_dependencies
	chmod +x ./start
	./start

resolve_dependencies: ./requirements.txt
	python3 -mpip install -r requirements.txt