import os
MYSQL_LOCAL={
  'default':{
  'ENGINE':'django.db.backends.mysql',
  'NAME':'proyecto_tienda_eccomerce', #nombre de la base de datos
  'USER':'root',
  'PASSWORD':'root',
  'HOST':'127.0.0.1', #servidor local o también puede ser 'localhost'
  'PORT':'3306'
  }
}
MYSQL_AZURE={
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DBNAME'),
        'HOST': os.environ.get('DBHOST'),
        'USER': os.environ.get('DBUSER'),
        'PASSWORD': os.environ.get('DBPASS'),
    }
}