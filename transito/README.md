# Crear app - modulo
python manage.py startapp nombre-modulo
# Model
Crear un modelo y migrate a la BD con el contien Django ORM
1. python manage.py makemigrations snippets
2. python manage.py migrate

## <p style="color:#99cc99"> Permission </p>

configuracion setting de proyecto
```
REST_FRAMEWORK = {
'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}
```
En la vista clase base atributo ó parametros

```
permission_classes : [IsAuthenticated]

configurar : 
 AllowAny : Perimite todo 
 IsAuthenticated : esta autenticado
 IsAdminUser : administrador
 IsAuthenticatedOrReadOnly : acceso a GET lectura y POST autenciacion obligatoria

```
## <p style="color:#ee8597"> Response </p>

    HTTP 401 no autorizado
    Permiso HTTP 403 denegado


## <p style="color:#ee8597"> URLs </p>

```

*** ALL **
GET http://127.0.0.1:8000/transito/

*** Add ***
POST http://127.0.0.1:8000/transito/
content-type: application/json
Authorization: Basic admin:by123456

*** Detail ***
GET http://127.0.0.1:8000/transito/1

*** Edit ***
PUT http://127.0.0.1:8000/transito/1/
content-type: application/json
Authorization: Basic admin:by123456

```
