# AdministradorST
                                              Plataforma de Administracion para Servicios Tecnicos



[==> Casos de Prueba <==](https://docs.google.com/spreadsheets/d/1XS3uoYypWx3NZjh3MMgHA_54NBxl6aaDTBgHDIhAgvY/edit?usp=sharing)



## Este proyecto tiene como objetivo crear un sistema para la administración de Servicios Tecnicos de Telefonia Celular y afines.
Cosas que puedes hacer::

[==> Video de Funcionalidades <==](https://www.loom.com/share/1c1dcbb136da460ab3ceed488ec58dd9)

### Ingresar a los siguientes servicios previo Login:
- Crear, leer, actualizar y eliminar Clientes.
- Buscar Clientes en Base de Datos
- Crear, leer, actualizar y eliminar Reparaciones.
- Crear, leer, actualizar y eliminar Accesorios.
- Crear, leer, actualizar y eliminar Herramientas.
- Crear, leer, actualizar y eliminar Proveedores.

# Instalar

Para instalar este software necesitas:

## Comprobar la versión de Python
Este proyecto se escribió con Python 3.10.5, por lo que le sugiero que pruebe con esta versión o superior para no tener problemas de compatibilidad.

Cómo verifico mi versión de python,

en sistemas *nix: 

```bash
> python --version
> Python 3.8.0
```

en windows:

```bash
c:\> py --version
c:\> Python 3.8.0
```

## Instalar dependencias
Para instalar las dependencias, debe ejecutar `pip install`, asegúrese de estar en la carpeta del proyecto y pueda ver el 'requirements.txt' archivo cuando haga 'ls' o 'dir':

```bash
> pip install -r requirements.txt
```
Este último instalara los requerimientos necesarios en la terminal..

`algunos sistemas operativos requieren el uso de  pip3 o pip `

## Configuración de la aplicación Django

Una vez que termine la instalación de las dependencias, debe ejecutar algunos comandos Django.

### Migraciones

Initialize the database
:
```bash
> python mananage.py migrate
```
windows:
```bash
c:\> py mananage.py migrate
```

### Ejecutar el servidor de prueba

```bash
> python mananage.py runserver
```
windows:
```bash
c:\> py mananage.py runserver
```
Go to localhost:8000/

para tener acceso a la aplicación.

'Aclaracion: es necesario contar con internet par la carga de imagenes de templates.

Si todo va bien, debería poder abrir el navegador y ver cómo se ejecuta la aplicación.

### Futuras actualizaciones
En la proximas actualizaciones incluiremos:

- Busqueda por categorias de Reparacion, Accesorios y herramientas.
- La posibilidad de una seccion para 'Postear' soluciones tecnicas a reparaciones especificas.
- Area para la Reserva y Compra de Repuestos, Herramientas y Accesorios.
- Acceso al Curso de Reparacion con mas de 100 Videos Disponibles.



### 'EnLinea' Siempre a Tu Servicio.-                                                                                             © 2022 by Christian Coria

