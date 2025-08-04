# Docker

## Описание

За основу взят проект созданный в рамках курса DRF

## Использование


-Запуск celery и worker : celery -A config worker --beat --scheduler django --loglevel=info

-Запуск Docker'а: docker-compose up -d —build