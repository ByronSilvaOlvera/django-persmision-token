
<h3 align="center">Project Tarea</h3>

## 🧐 Entorno Virtual <a name = "about"></a>

### Paquetes.
pip install virtualenv <br>
pip install virtualenvwrapper-win

Activar entorno virtual => Workon nombreentorno

### Paquetees en Project <a name = "getting_started"></a>
asgiref==3.3.4<br>
Django==3.2.1<br>
djangorestframework==3.12.4<br>
mysqlclient==2.0.3<br>
pytz==2021.1<br>
sqlparse==0.4.1<br>
sqlparse==0.4.1<br>
django-cors-headers==3.7.0<br>


## 🏁 Nuevo Proyecto <a name = "deployment"></a>

1. django-admin startproject tutorial <br>
2. python manage.py migrate

3. python manage.py createsuperuser <br>--email: byronsjimb@gmail.com --username admin pss:by123456

### CORE

Trabaje simultaneamente los dos servidores

```
pip install django-cors-headers
INSTALLED_APPS = [
    ...
    # CORS
    'corsheaders',
]

MIDDLEWARE = [
    ...
    # CORS
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
    'http://localhost:8081',
)


```

### Installing

concepto

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo.

## 🔧 Running the tests <a name = "tests"></a>

Explain how to run the automated tests for this system.

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## 🎈 Usage <a name="usage"></a>

Add notes about how to use the system.

## 🚀 Deployment <a name = "deployment"></a>

Add additional notes about how to deploy this on a live system.

## ⛏️ Built Using <a name = "built_using"></a>

- [MongoDB](https://www.mongodb.com/) - Database
- [Express](https://expressjs.com/) - Server Framework
- [VueJs](https://vuejs.org/) - Web Framework
- [NodeJs](https://nodejs.org/en/) - Server Environment

## ✍️ Authors <a name = "authors"></a>

- [@kylelobo](https://github.com/kylelobo) - Idea & Initial work

See also the list of [contributors](https://github.com/kylelobo/The-Documentation-Compendium/contributors) who participated in this project.

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Hat tip to anyone whose code was used
- Inspiration
- References
