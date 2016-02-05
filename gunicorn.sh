#!/bin/bash
cd /var/www/Bridal-Images-Mr-Tux


source /etc/environment
source venv/bin/activate

exec gunicorn --workers=3 --threads=3 LoveDb.wsgi -b localhost:8001
