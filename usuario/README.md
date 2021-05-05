# Crear app - modulo
python manage.py startapp nombre-modulo
# Model
Crear un modelo y migrate a la BD con el contien Django ORM
1. python manage.py makemigrations snippets
2. python manage.py migrate
# URL
## POST
```
POST http://127.0.0.1:8000/usuario/
content-type: application/json

{
   "created"        : "2021-05-05 13:10:56.000000", 
   "nombre"         : "Byron Silva",
   "email"          : "byron@gmail.com",
   "fecha"          : "2021-05-05",
   "tiempoconectado": "2 horas",
   "fechaoff"       : "2021-05-05"
}

Status 200
```
### Result
```
{
  "id": 5,
  "created": "2021-05-05T13:10:56Z",
  "nombre": "Edwin Silva",
  "email": "edwin@gmail.com",
  "fecha": "2021-05-05",
  "tiempoconectado": "10 horas",
  "fechaoff": "2021-05-05"
}
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

{
   "created"        : "2021-05-05 13:10:56.000000", 
   "nombre"         : "Edwin Silva Olvera",
   "email"          : "edwin@gmail.com",
   "fecha"          : "2021-05-05",
   "tiempoconectado": "10 horas",
   "fechaoff"       : "2021-05-05"
}

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