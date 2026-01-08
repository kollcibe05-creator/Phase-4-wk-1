# Superheroes

##### A data model of its kind!!!

##Description
Superheroes is Flask-SQLAlchemy + SQL  backend project aimed at resolving the complexity of organizing superheroes' data with consistency and persisting the changes to the Database. It implements flask-sqlalchemy, SQL and OOP to model the database and ensure accuracy while accessing the data

The ideological business requirements are:

1. A Hero has many  `Power`s through the  `Department`.
2. A Power has many `Hero`s through `HeroPower`.
3. A `HeroPower` belongs to a `Hero` and belongs to a  `Power`
_______
The ERD model of the relationships;
https://curriculum-content.s3.amazonaws.com/6130/code-challenge-2/domain.png
_______
The models incorporate serialize_rules and association_proxies to limit recursion depth and simplify cross-model data access.
## Tech Stack
- Python
- SQL
- Markdown

## File Structure

Take a look at the directory structure:

```console
.
├── LICENSE
├── app.py
├── instance
│   └── app.db
├── migrations
│   ├── README
│   ├── alembic.ini
│   ├── env.py
│   ├── script.py.mako
│   └── versions
│       └── 5e3d845ba64d_initial_migration.py
├── models.py
└── seed.py
        
```


## Generating Your Environment

You might have noticed in the file structure- there's  a Pipfile!

Install  the dependencies  you'll need to navigate the file by 
adding them to the `Pipfile`. Run the commands:

```console
pipenv install
pipenv shell
```

---

## Environment Configurations Setup
To start working with the data  you need to:
1. Navigate to */server* dir:
```

    cd server

```
2. Configure the flask environment commands:
    ```
    export FLASK_APP=app.py
    export FLASK_RUN_PORT=5555

    ```
This will allow you to start the server using :
```
flask run

```    
The commands below have been run for you:
```
flask db init
flask db migrate -m "Initial migration"
flask db upgrade head
python seed.py

```


## Functionality
# models.py
Our models import from `db.Model` and `SerializerMixin`.
The have similar constructors such as:
1. *__repr__*: In it is the modified output of a class instance to improve clarity.
2. *__tablename__*: Specifies the table in the database that the objects will be mapped to.
3. *serialize_rules*: It states the fields to be excluded to prevent recursion depth.
4. *association_proxy*: It simplifies access to the cross-model fields and data. 

The models are:
- Power
- HeroPower ~ The association object.
- Hero


# app.py
The views registered to the routes as depicted are:
1. (GET)*heroes()*: GET request to */heroes*.
2. (GET)*get_heroes(id)*: Takes id as an argument and implements GET to the */heroes/:id*.
3. (GET)*powers()*: GET request to */powers*.
4. (GET, PATCH)*get_powers(id)*: Takes id as an argument and implements GET and PATCH to the */powers/:id*.
5. (GET, POST)*post_hp()*: POST to */hero_powers*. 

# seed.py
It contains the data seeded to the `app.db`

# app.db
It holds our SQL database.





# Author
*Collins Kibet*

## [License](LICENSE)

MIT License
Copyright (c) 2025 Collins Kibet


# Contact info
* Email : kollcibe05@gmail.com


`(**Thank you**)`