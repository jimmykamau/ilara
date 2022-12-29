# Ilara
Checkout system  for managing inventory items and a way to sell said inventory items. It provides a front-end system that can be used by both clients for self-checkout, and by staff for both checkout and admin management.

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

## Running tests

You can run automated tests by executing the command below
```
docker compose -f docker-compose.yml -f docker-compose.dev.yml exec web ./manage.py test
```

## Admin Usage

### User Management

Visit the [admin](https://localhost/admin/) site with a superuser/staff account. On the left sidebar, click `AUTHENTICATION AND AUTHORIZATION`.

#### Creating and assigning roles

Click on `Groups -> ADD GROUP` and give the group a suitable name. Under `Permissions`, click on the required permissions for the group. For instance, if creating a pharmacy administrator role that can create, update and delete inventory items, filter the `Available permissions` by `inventory`. Select all the permissions shown and click the `right arrow` ➡️ highlighted. The `Chosen permissions` table will be populated with the selected permissions. Click `Save`.
To assign a role to a user, go to `Users` under `AUTHENTICATION AND AUTHORIZATION` and select the user. Under `Groups` on their profile, filter for the group desired and move it to the `Chosen groups` section. Save your changes.
If you want the user to be able to log into the Admin site, make sure you've marked the `Staff status` checkbox on their profile. They will then only see the items they're authorized to.

#### Fine-grained permissions

You can also give specific users specific permissions. Click on their username under `Users`, scroll to `User permissions` and choose the permissions you want to grant. Remember to check their `Staff status` checkbox if you want them to be able to log into the admin site.

### Inventory Management

Visit the [admin](https://localhost/admin/) site with a staff account. On the left sidebar, click `Inventory Items` under `Inventory`.
#### Adding new items

Click `ADD INVENTORY ITEM` on the top-right of the page. Fill all fields and make sure to check `Active` in order for the item to appear in the storefront.

#### Updating stock quantities

Click on the desired inventory item and update its `Stock quantity` field.
