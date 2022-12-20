# Ilara
Checkout system  for managing inventory items and a way to sell said inventory items.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Ensure you have [docker-desktop](https://www.docker.com/products/docker-desktop/) and [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed.

### Installing

Clone this repo

```
git clone https://github.com/jimmykamau/ilara.git
```

Create an `.env` file inside the `web` directory with the contents of `.env.example`.

Follow [these instructions](https://www.freecodecamp.org/news/how-to-get-https-working-on-your-local-development-environment-in-5-minutes-7af615770eec/) to create a trusted local SSL certificate. Create a `certs` directory inside `proxy `and copy `server.key` and `server.crt` to it.

Build the containers
```
docker compose -f docker-compose.yml -f docker-compose.dev.yml build 
```

Start the `db` service
```
docker compose -f docker-compose.yml -f docker-compose.dev.yml up -d db
```

Grab a `psql` shell from the `db` service
```
docker compose -f docker-compose.yml -f docker-compose.dev.yml exec db psql -U postgres -h db -p 5432
```

Create a database with the name you specified in the `couscous.env` file
```
CREATE DATABASE ilara;
```

Exit the shell
```
\q
```

Start the remaining services
```
docker compose -f docker-compose.yml -f docker-compose.dev.yml up
```

Visit the [https://localhost/](https://localhost/) URL to ensure everything is running properly.

Create a Django superuser
```
docker compose -f docker-compose.yml -f docker-compose.dev.yml exec web ./manage.py createsuperuser
```
Log into the [admin](https://localhost/admin/) site with the superuser credentials you just created. From here you can create users and assign them to groups with role-based permissions.

## Running the tests

You can run automated tests by executing the command below
```
docker compose -f docker-compose.yml -f docker-compose.dev.yml exec web ./manage.py test
```
