# bbog-pl-find-connected-clients-function

Lambda encargada de consultar el estado de conexión de los clientes desde el archivo en excel de s3

## Cómo iniciar la lambda

### Pre requisitos

- Tener python instalado
- Crear un ambiente virtual 

### Instalación

#### 1. Instalar python en su maquina

Dirigirse a la documentación de python: https://docs.python.org/es/3/using/mac.html

#### 2. Crear un ambiente virtual 

```sh
python3 -m venv venv
```

#### 3. Activar ambiente virtual 

```sh
source venv/bin/activate
```
## Desarrollo

### Instalar dependencias

```sh
pip3 install -r requirements/dev.txt --use-feature=fast-deps
```

### Run server

```sh
python3 app/app.py
```
