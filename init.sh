sudo ln -sf /home/box/web/etc/gunicorn.conf.py   /etc/gunicorn.d/gunicorn.conf.py
# sudo /etc/init.d/gunicorn restart
sudo /etc/init.d/gunicorn stop
sudo gunicorn -c gunicorn.conf.py hello:wsgi_application