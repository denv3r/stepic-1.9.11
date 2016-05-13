sudo ln -sf /home/box/web/etc/gunicorn.conf.py   /etc/gunicorn.d/gunicorn.conf.py
# sudo /etc/init.d/gunicorn restart
sudo /etc/init.d/gunicorn stop
sudo gunicorn hello:wsgi_application