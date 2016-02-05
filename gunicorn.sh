#!/bin/bash
cd /var/www/LoveDB


source /etc/environment
source env/bin/activate

exec gunicorn --workers=3 --threads=3 LoveDb.wsgi -b localhost:8002
