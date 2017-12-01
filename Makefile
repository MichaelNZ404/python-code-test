live: migrate
	docker-compose run --rm --service-ports code-test scripts/runserver

migrate: build
	docker-compose run --rm code-test scripts/migrate

build:
	docker-compose build
