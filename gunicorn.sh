#!/bin/bash
cd /var/www/LoveDb


source /etc/environment
source env/bin/activate

exec gunicorn --workers=3 --threads=3 LoveDb.wsgi -b localhost:8001
