# Beneficiaries Backend App

## Setup

In order to run and deploy the project, you need to install the following dependencies:
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Python 3.8 64 bit](https://www.python.org/ftp/python/3.8.10/python-3.8.10-amd64.exe)

## Run app in development mode

In project root path, perform the following:
- Create `python venv` or simply run `pip install -r requirements.txt`
    - If you want to create a `python venv` run the following:
        - `python -m venv env`
        - `source env/Scripts/activate`
        - `pip install -r requirements.txt`
- Execute `docker compose -f docker-compose-dev.yml up --force-recreate` this will perform the following:
    - Recreate docker development containers if they already exist
    - Deploy container for SQL Server database and run setup scripts:
        - Create tables: `database\scripts\1_tables.sql`
        - Create default data: `database\scripts\2_inserts.sql`
        - Create stored procedures: `database\scripts\3_stored_procedures.sql`
    - Deploy container for Python Flask App with hot reload enabled

## Deploy production build

In project root path, perform the following:
- Execute `docker compose up -d` this will perform the following:
    - Deploy container for SQL Server database and run setup scripts:
        - Create tables: `database\scripts\1_tables.sql`
        - Create default data: `database\scripts\2_inserts.sql`
        - Create stored procedures: `database\scripts\3_stored_procedures.sql`
    - Deploy container for Python Flask App

## Connect to Database

If you want to connect to SQL Database, use the folloging info
- For development:
    - host: `localhost`
    - port: `1433`
    - schema: `master`
    - user: `SA`
    - password: `Password#12345`
- For production:
    - host: `localhost`
    - port: `1434`
    - schema: `master`
    - user: `SA`
    - password: `Password#12345`

Database scripts are located in `database\scripts` project path

## Try the API

If you want to try the API in postman, use the following info:
- Host for development: `http://localhost:8080`
- Host for production: `http://localhost:8081`

Get the `access token` in the route `/api/auth` with the default admin user created during deploy:
- username: `admin`
- password: `password`

See api documentation in `docs\index.html` project file