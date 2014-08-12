python manage.py syncdb
python manage.py collectstatic

chown apache:apache /var/www/html/djangoci -R

cat >> /etc/httpd/conf/httpd.conf << EOF
LoadModule python_module modules/mod_python.so
<VirtualHost *:80>
	<Location "/">
	    SetHandler python-program
	    PythonHandler django.core.handlers.modpython
	    SetEnv DJANGO_SETTINGS_MODULE djangoci.settings
	    PythonDebug Off
	    PythonPath "['/var/www/html/djangoci/'] + sys.path"
	</Location>
</VirtualHost>