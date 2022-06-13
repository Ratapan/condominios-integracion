# Condominios


## MySql
User: USER_API
User_Pass: user_api_admin

```sql
CREATE USER 'USER_API'@'%' IDENTIFIED VIA mysql_native_password USING '***';
GRANT ALL PRIVILEGES ON *.* TO 'USER_API'@'%' REQUIRE NONE WITH GRANT OPTION MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;
```
DB: API_REST

## Pasos
```
0- primero validar ultima versión de python.
0.1- instalar django con el comando: pip install django
1- crear una carpeta en escritorio llamada API.
2- abrir la carpeta con visual code en modo administrador.
3- instalar entorno virtual con el comando: pip install virtualenv
4- usa un nombre definido para el espacio de trabajo, usar comando: virtualenv API
5-activamos el entorno virtual con el comando: .\API\Scripts\activate
6- validamos si existen paquetes instalados en nuestro entorno con el comando: python --version
7- instalar django con el comando: pip install django
8- actualizar nuevamente pip con el comando: pip install --upgrade pip
9- validamos que este todo instalado con el comando: pip list
12- creamos un proyecto con el comando: django-admin startproject APIREST
13- accedemos al sub directorio con el comando: cd .\APIREST\
14- creamos una app con el comando: django-admin startapp api
15- debemos instalar el driver conector entre framework y la base de datos con el comando: pip install mysqlclient pymysql
16- editamos el archivo settings.py y agregamos a la linea 40 'api'
17- creamos los modelos con las siguientes lineas de codigo, dentro de la app en el archivo  models.py reemplazamos todo el codigo por esto:

from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=50)
    website = models.URLField(max_length=100)
    foundation = models.PositiveIntegerField()

18- en el archivo dentro de la app se llama admin.py debemos registrar nuestro modelo remplazar todo el codigo por lo siguiente:

    from django.contrib import admin
    from .models import Company

    # Register your models here.

    admin.site.register(Company)

19- debemos crear en PHP my admin un usuario llamado USER_API con todos los roles y ademas definirle una contraseña 12345.
20- debemos crear una base de datos con el siguiente nombre: API_REST

21- ademas debemos agregar la conexión a la BD en linea 77 del archivo settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'PORT': '3306',
        'USER': 'USER_API',
        'PASSWORD': '12345',
        'NAME': 'API_REST',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}

22- ejecutar migración de modelo a mysql con el comando: python manage.py migrate
23- crearemos un super user con el comando: python manage.py createsuperuser

name: USER_API
email: ingrese su mail
contraseña: asu elección

24- por ultimo generamos la migración de los modelos a my sql con el comando: python manage.py makemigrations
25- volvemos a ejecutar el comando: python manage.py migrate
26- por ultimo ejecutamos el comando: python manage.py runserver
27- acceda a la siguiente url: http://127.0.0.1:8000/admin
28- inicie sesión con sus credenciales de superuser.

29- en la hoja de views.py se debe agregar los siguientes codigos, reemplazando el total del codigo.

from django.views import View

# Create your views here.
class CompanyView(View):

    def get(self, request):
        pass

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass

30- dentro de nuestra aplicación crearemos un archivo llamado urls.py y dentro de el pondremos el siguiente codigo:

from django.urls import path
from .views import CompanyView

urlpatterns = [
    path('companies/', CompanyView.as_view(), name='companies_list')
]

31- en el archivo urls.py del directorio general debe modificar y remplazar en la linea 17 el siguiente codigo
from django.urls import path, include

y en la linea 20 debajo agregar la siguiente linea:

path('api/', include('api.urls'))

32- volvemos al archivo view.py debemos agregar nuevo codigo con esto haremos el desplique de información por metodo GET.

from django.http import JsonResponse
from django.views import View
from .models import Company

# Create your views here.
class CompanyView(View):

    def get(self, request):
        companies = list(Company.objects.values())
        if len(companies) > 0:
            datos = {'message':"Succes",'companies':companies}
        else:
            datos = {'message':"Companies not found..."}
        return JsonResponse(datos)

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass

33- deben ejecutar el comando run server y entrar al siguiente link.

http://127.0.0.1:8000/api/companies/

de este modo se desplegara la información en json.

34- deben validar el json en la pagina: https://jsonformatter.curiousconcept.com

35- deben instalar el addons thunder json para visual code.

36- deben generar una nueva colección llamada DJANGO_LIST

37- deben copiar la url del servicio y darle ejecutar y ver la magia.

38- ajustamos nuestro archivo views.py y modifcamos el codigo del archivo por el siguiente:

import json
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Company

# Create your views here.
class CompanyView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        companies = list(Company.objects.values())
        if len(companies) > 0:
            datos = {'message':"Succes",'companies':companies}
        else:
            datos = {'message':"Companies not found..."}
        return JsonResponse(datos)

    def post(self, request):
        #print(request.body)
        jd = json.loads(request.body)
        #print(jd)
        Company.objects.create(name=jd['name'], website=jd['website'], foundation=jd['foundation'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request):
        pass

    def delete(self, request):
        pass


39- para probar la inserción por metodo post, debe ejecutar en thunder o postman con el siguiente body:

{
    "name": "Twitter",
    "website": "http://twitter.com",
    "foundation": 2006
}

40- debemos ir a nuestro archivo custom de urls.py y cambiar el codigo por el siguiente:

from django.urls import path
from .views import CompanyView

urlpatterns = [
    path('companies/', CompanyView.as_view(), name='companies_list'),
    path('companies/<int:id>', CompanyView.as_view(), name='companies_list')
]

41- despues volvemos views.py modifcaremos nuestro archivo para que podamos hacer un get_list por ID, cambiamos el codigo por el siguiente:

import json
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Company

# Create your views here.
class CompanyView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request,id=0):
        if(id>0):
            companies = list(Company.objects.filter(id=id).values())
            if len(companies) > 0:
                company=companies[0]
                datos = {'message':"Succes",'companies':company}
            else:
                datos = {'message':"Companies not found..."}
            return JsonResponse(datos)
        else:
            companies = list(Company.objects.values())
            if len(companies) > 0:
                datos = {'message':"Succes",'companies':companies}
            else:
                datos = {'message':"Companies not found..."}
            return JsonResponse(datos)

    def post(self, request):
        # print(request.body)
        jd = json.loads(request.body)
        # print(jd)
        Company.objects.create(name=jd['name'], website=jd['website'], foundation=jd['foundation'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request):
        pass

    def delete(self, request):
        pass
```