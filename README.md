# Historia de Transacciones IOL

## Requisitos previos

- Docker
- Docker Composer

## Configuración

Crea un archivo llamado .secrets.toml en el directorio principal del repositorio con tus propias credenciales y configuraciones:

```toml
[iol.credentials]

username = "tu_nombre_de_usuario"
password = "tu_contraseña"

[db.credentials]
POSTGRES_USER="usuario_postgres"
POSTGRES_PASSWORD="contraseña_postgres"
POSTGRES_DB="nombre_base_de_datos"
POSTGRES_HOST="db"
POSTGRES_PORT="5432"
```

Asegúrate de reemplazar los valores con tus propias credenciales y configuraciones.

## Construir e iniciar los servicios

Para construir e iniciar los servicios definidos en el archivo docker-compose.yml, utiliza los siguientes comandos:

```bash
make build
make up
```

Esto construirá las imágenes de Docker y ejecutará la base de datos PostgreSQL y otros servicios definidos en el archivo docker-compose.yml.

## Ejecutar el servicio Python a demanda

Para ejecutar el servicio etl a demanda (sin iniciarlo automáticamente al iniciar Docker Compose), ejecuta el siguiente comando:

```bash
make run-etl
```

## Detener los servicios

Para detener y eliminar los servicios definidos en el archivo docker-compose.yml, ejecuta el siguiente comando:

```bash
make down
```

Esto detendrá y eliminará todos los servicios en ejecución.

## Licencia

Este proyecto está licenciado bajo la licencia MIT - consulta el archivo LICENSE para obtener más detalles.
