# Crear app - modulo
python manage.py startapp nombre-modulo
# Model
Crear un modelo y migrate a la BD con el contien Django ORM
1. python manage.py makemigrations snippets
2. python manage.py migrate

# Descripcion
Agrego token  


# URL
## POST
```
POST http://127.0.0.1:8000/usuario/
content-type: application/json

Status 200
```

# GET
```
GET http://127.0.0.1:8000/usuario/
Status : HTTP/1.1 200 OK

GET http://127.0.0.1:8000/usuario/2
Status : HTTP/1.1 200 OK

```
# PUT
```
PUT http://127.0.0.1:8000/usuario/2/
content-type: application/json


Nota: es importante en usuario/2/

Status : HTTP/1.1 200 OK

Error : HTTP/1.1 404 Not Found
{
  "detail": "Not found."
}

```

# DELETE
```
DELETE http://127.0.0.1:8000/usuario/1/
```