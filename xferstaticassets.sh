#!/bin/bash

# set the ownership to the current user temporary
sudo chown -R ubuntu:ubuntu /var/www

# collects static files for deployment environment
python manage.py collectstatic <<< yes

# reset the ownership back to root
sudo chown -R root:root /var/www

echo Done!
