#!/bin/sh

echo "Esperant la base de dades..."
sleep 5

echo "Aplicant migracions..."
python manage.py migrate

echo "Iniciant el servidor..."
exec python manage.py runserver 0.0.0.0:8000