# Local Development

## Setup
  `rm -rf venv`<br/>
  `python3 -m venv venv` <br/>
  `source venv/bin/activate` <br/>
  `pip3 install -r requirements.txt`

## Migrations
  `python3 manage.py makemigrations`<br/>
  `python3 manage.py migrate`

## Collect Static Files
`python3 manage.py collectstatic`

## Create Superuser
`python3 manage.py createsuperuser`
<br/>Server emails will be sent to the mail address configured here.

## Enable Debugging
`DEBUG=True` in `abijith/settings.py`

## Start Server
`python3 manage.py runserver`

# Production Deployment

`sudo systemctl stop apache2.service`

Make a backup of `db.sqlite3` before deploying the latest changes

## Build virtual environment
`rm -rf venv`<br/>
`python3 -m venv venv` <br/>
  `source venv/bin/activate` <br/>
  `pip3 install -r requirements.txt`

Copy original DB from backup folder

## Migrations
`python3 manage.py makemigrations`<br/>
  `python3 manage.py migrate`

## Create Superuser (only if starting fresh)
`python3 manage.py createsuperuser`
<br/>Server emails will be sent to the mail address configured here.

## Provide permission for Apache to write to DB
`sudo chown www-data:www-data .`<br/>
`sudo chown www-data:www-data db.sqlite3`<br/>
`sudo chmod 777 .`<br/>
`sudo chmod 777 db.sqlite3`

## Restart Apache
`sudo systemctl start apache2.service`

# DevOps Changes
Stop the server if running

`web.conf` changes
```
	ServerAdmin admin@abijith.net
        DocumentRoot /var/www/web

        Alias /static /var/www/web/staticfiles
        <Directory /var/www/web/staticfiles>
                Require all granted
        </Directory>

        <Directory /var/www/web/abijith>
                <Files wsgi.py>
                        Require all granted
                </Files>
        </Directory>

        <Directory /var/www/web>
                Require all granted
        </Directory>

        WSGIDaemonProcess abijith python-path=/var/www/web python-home=/var/www/web/venv
        WSGIProcessGroup abijith
        WSGIScriptAlias / /var/www/web/abijith/wsgi.py
```
`a2ensite web` to add the host.<br/>
Restart the server
