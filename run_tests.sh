docker compose build
docker compose down --remove-orphans
docker compose run server pytest -s -v src/tests