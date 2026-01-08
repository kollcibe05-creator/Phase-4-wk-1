# Superheroes

##### A data model of its kind!!!

Superheroes is Flask-SQLAlchemy + SQL  backend project aimed at resolving the complexity of organizing superheroes' data with consistency and persisting the changes to the Database. It implements flask-sqlalchemy, SQL and OOP to model the database and ensure accuracy while accessing the data

The ideological business requirements are:

1. A Hero has many  `Power`s through the  `Department`.
2. A Power has many `Hero`s through `HeroPower`.
3. A `HeroPower` belongs to a `Hero` and belongs to a  `Power`
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

## Environment Configurations
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
It contains the model `Department` which has the following functionalitites.
1. *__repr__*: In it is the modified output of a class instance to improve clarity.
2. *__tablename__*: Species the table in the database that the objects will be mapped to.
   Below it are the constraints that restricts some field inputs to be of certain data types and length.
3. *get_all()*: A class method that returns all the departments mapped into the departments table.
4. *find_by_id()*: A class method that returns a department instance in the database of the id given.
5. *find_by_name()*: A class method that returns a department instance in the database of the name given.
6. *create()*: A class method that creates a new department instance and persists it to the database using sessions.
5. *update()*: A class method that updates the department instance and persists it to the database using sessions.
8. *delete()*: A class method that deletes a department instance and from the database using sessions.


# app.py
It contains the model `Employee` which has the functionalities:
1. *__repr__*: In it is the modified output of a class instance to improve clarity.
2. *__tablename__*: Species the table in the database that the objects will be mapped to.
    Below it are the constraints that restricts some field inputs to be of certain data types and length.
    Fields such as *received_reviews*, *given_reviews* and *department* have been used to create the relationship with the departments and reviews Models and tables. 
3. *get_all()*: A class method that returns all the employees mapped into the departments table.
4. *find_by_id()*: A class method that returns an employee instance in the database of the id given.
5. *find_by_full_name()*: A class method that returns an employee instance in the database of the names given.
6. *create()*: A class method that creates a new employee instance and persists it to the database using sessions.
5. *update()*: A class method that updates the employee instance details and persists it to the database using sessions.
8. *delete()*: A class method that deletes an employee instance and from the database using sessions.

# seed.py
It contains the model `Review` which has the functionalitites:
1. *__repr__*: In it is the modified output of a class instance to improve clarity.
2. *__tablename__*: Species the table in the database that the objects will be mapped to.
    Below it are the constraints that restricts some field inputs to be of certain data types and length.
    Fields *reviewee* and *reviewer*  have been used to create  relationship with the employee Model and table in the database. 
3. *get_all()*: A class method that returns all the reviews mapped into the departments table.
4. *find_by_id()*: A class method that returns a review instance in the database of the id given.
5. *create()*: A class method that creates a new review instance and persists it to the database using sessions.
6. *update()*: A class method that updates the review instance details and persists it to the database using sessions.
7. *delete()*: A class method that deletes a review instance and from the database using sessions.
<!-- 5. *find_by_name()*: A class method that returns a review instance in the database of the names given. -->

# app.db
It maps the Seeded data  to the database.
`recreate_db` drops all the tables and recreates it with the new seeded data.





# Author
*Collins Kibet*

## [License](LICENSE)

MIT License
Copyright (c) 2025 Collins Kibet


# Contact info
* Email : kollcibe05@gmail.com


`(**Thank you**)`