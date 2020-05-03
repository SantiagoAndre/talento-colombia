# Talento Colombia:
    Este es el software de la empresa Talento Colombia dedicada a la gestión de talento humano, que permite la sistematizacion del proceso de seleccion y reclutamiento. Este cuenta con los siguientes modulos:

    • Sistema de autenticación
    • Gestión de usuarios
    • Gestión de convocatorias
    • Gestionar las aplicaciones de los aspirantes
    • API para las empresas
## Usuarios:
    - Administrador
    - Usario empresarial
    - Usuario aspirante
## Funcionalidades del sofware: 
    A continuacion se listan lass funcionalidades del sistema relacionadas a las HE Y HU:

    - Visitante de la pagina(HU-001):
        - 01 visualizar las ofertas de trabajo
        - 02 aplicar a una oferta de trabajo

    - Usuario del sistema(Cualquier Rol):
        - HU-002 gestion de la sesion
            - 01 Iniciar sesion
            - 02 Recuperar contrasena
            - 03 Cerrar sesion
    - Administrador del sistema(Rol1)
        - HU-003 gestionar  usuarios
            - 01 listar usuarios
            - 02 registrar usuarios
            - 03 actualizar usuario
            - 04 ver informacion de usuario
            - 05 eliminar usuario
    - usuario Empresarial(Rol2)
        - HU-004 gestionar mis ofertas laborales:
            - 01 listar mis convocatorias laborales
            - 02 registrar convocatorias laborales
            - 03 ver informacion de un aspirante a una de mis convocatorias

        - HU-006  interfaz de integracion para registrar y ver convocatorias(API)
            - 01 Crear convocatorias
            - 02 Consultar convocatoria
            - 03 autenticares
    - Usuario aspirante(Rol3):
        - HU-005 ver convocatoria a las que aplique y su estado
            - 01 ver convocatorias
## Contenido:
* `src`: El codigo fuente se encuentra en la carpeta src, este esta hecho en el framework Django de python.
* `design`: Diseños del software.

## Codigo fuente
    
### Ejecutar
    Para ejecutar el proyecto django en local ejecuta los siguientes comandos en una terminal dentro del directorio del proyecto.
         ```pipenv install
            pipenv shell
            python manage.py migrate
            python manage.py createsuperuser
            python manage.py runserver
            python manage.py loaddata fixture.json```
    
    

