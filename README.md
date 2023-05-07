# DRF-docker-template
DRF + Docker + docker-compose + Celery + Redis + knox auth template

DRF template with knox authorization, configured Celery, Redis (as broker and as storage), postgreSQL (as primary SQL database).

The docker-compose.yaml file includes services:
1) Web (Django Rest Framework App)
2) Redis (Broker + Storage)
3) Worker (Celery service)
4) Flower (Interface for displaying worker processes)
5) db (PostgreSQL database)

Several Views (viewsets) to handle user registration and authorization through knox and serializers to them.

Running docker-compose up --build
