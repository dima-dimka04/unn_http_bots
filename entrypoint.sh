#!/bin/sh
set -e

python -m bot.create_database_postgres
exec python -m bot