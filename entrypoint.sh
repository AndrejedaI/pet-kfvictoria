#!/bin/sh

echo "📦 Применяем миграции..."
python manage.py migrate

echo "🎨 Собираем статику..."
python manage.py collectstatic --noinput

echo "🚀 Запускаем Gunicorn..."
exec "$@"