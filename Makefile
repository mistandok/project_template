start-unit-tests:
	pytest -vvs ./tests/unit_tests

start-unit-tests-no-slow:
	pytest -m "not slow" -vvs ./tests/unit_tests

local-down-app:
	docker-compose --env-file .env.local -f docker-compose.local.yaml down -v

local-start-app:
	docker-compose --env-file .env.local -f docker-compose.local.yaml up -d --build

prod-down-app:
	docker-compose --env-file .env.prod -f docker-compose.prod.yaml down -v

prod-start-app:
	docker-compose --env-file .env.prod -f docker-compose.prod.yaml up -d --build

init-alembic:
	alembic init migrations

create-migration:
	alembic revision -m "${name}"

local-migration-up:
	alembic -x env_path=".env.local" upgrade head

prod-migration-up:
	alembic -x env_path=".env.prod" upgrade head

local-migration-base:
	alembic -x env_path=".env.local" downgrade base

prod-migration-base:
	alembic -x env_path=".env.prod" downgrade base